"""Boundary tests for the installed skill's offline editorial checker."""

import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SKILL = Path(os.environ.get("CINEMATIC_SKILL_PATH", Path(__file__).resolve().parents[1]))
SCRIPT = SKILL / "scripts" / "check_plan.py"
SPEC = importlib.util.spec_from_file_location("check_plan", SCRIPT)
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)
EXAMPLE = json.loads((SKILL / "assets" / "shot-plan.example.json").read_text())


class PlanTests(unittest.TestCase):
    def setUp(self):
        self.plan = copy.deepcopy(EXAMPLE)

    def result(self):
        return CHECKER.validate_plan(self.plan)

    def invalid(self, text):
        result = self.result()
        self.assertFalse(result["valid_structure"])
        self.assertTrue(any(text in error for error in result["errors"]), result)

    def test_example_exact_duration(self):
        result = self.result()
        self.assertTrue(result["valid_structure"], result)
        self.assertEqual(result["summary"]["duration_seconds_exact"], "12/1")
        self.assertEqual(result["warnings"], [])

    def test_rational_rate_exact(self):
        self.plan["fps"] = "24000/1001"
        result = self.result()
        self.assertTrue(result["valid_structure"])
        self.assertEqual(result["summary"]["duration_seconds_exact"], "3003/250")
        self.assertEqual(result["summary"]["duration_seconds_decimal"], "12.012000000")

    def test_rounded_rate_rejected(self):
        self.plan["fps"] = "23.976"
        self.invalid("fps must be")

    def test_numeric_rate_rejected(self):
        self.plan["fps"] = 24
        self.invalid("fps must be")

    def test_zero_denominator_rejected(self):
        self.plan["fps"] = "24/0"
        self.invalid("fps must be")

    def test_bool_frames_rejected(self):
        self.plan["shots"][0]["start_frame"] = False
        self.invalid("integer start_frame")

    def test_bool_version_rejected(self):
        self.plan["schema_version"] = True
        self.invalid("schema_version")

    def test_resolution_types(self):
        self.plan["resolution"] = [1920, True]
        self.invalid("resolution must")

    def test_ratio_mismatch(self):
        self.plan["aspect_ratio"] = "9:16"
        self.invalid("does not exactly match")

    def test_unknown_creative_fields_allowed(self):
        self.plan["mood"] = {"concept": "quiet confidence"}
        self.plan["shots"][0]["lighting"] = "Broad soft key"
        self.assertTrue(self.result()["valid_structure"])

    def test_input_not_mutated(self):
        original = copy.deepcopy(self.plan)
        self.result()
        self.assertEqual(self.plan, original)

    def test_gap_requires_explicit_hold(self):
        self.plan["shots"][1]["start_frame"] = 97
        self.invalid("Gap before")

    def test_leading_gap(self):
        self.plan["shots"][0]["start_frame"] = 1
        self.invalid("first shot must start")

    def test_end_mismatch(self):
        self.plan["total_frames"] = 289
        self.invalid("last shot must end")

    def test_zero_length_shot(self):
        self.plan["shots"][1]["end_frame"] = 96
        self.invalid("greater than start_frame")

    def test_duplicate_ids(self):
        self.plan["shots"][1]["id"] = "S01"
        self.invalid("duplicates")

    def test_misordered_shots(self):
        self.plan["shots"][0], self.plan["shots"][1] = self.plan["shots"][1], self.plan["shots"][0]
        self.invalid("increase strictly")

    def test_overlap_requires_declaration(self):
        self.plan.pop("transitions")
        self.plan["shots"][0]["end_frame"] = 108
        self.invalid("explicit non-cut transition")

    def test_valid_dissolves(self):
        self.plan["shots"][0]["end_frame"] = 108
        self.plan["shots"][1]["end_frame"] = 204
        for shot in self.plan["shots"][:2]:
            shot["source"]["available_frames"] = 132
        for transition in self.plan["transitions"]:
            transition.update(kind="dissolve", overlap_frames=12)
        self.assertTrue(self.result()["valid_structure"], self.result())

    def test_wrong_overlap_count(self):
        self.plan["shots"][0]["end_frame"] = 108
        self.plan["transitions"][0].update(kind="dissolve", overlap_frames=8)
        self.invalid("timeline has 12")

    def test_cut_cannot_overlap(self):
        self.plan["transitions"][0]["overlap_frames"] = 12
        self.invalid("cut must have zero")

    def test_noncut_needs_overlap(self):
        self.plan["transitions"][0]["kind"] = "wipe"
        self.invalid("requires positive")

    def test_nonadjacent_transition(self):
        self.plan["transitions"][0]["to"] = "S03"
        self.invalid("connect adjacent")

    def test_duplicate_transition(self):
        self.plan["transitions"].append(copy.deepcopy(self.plan["transitions"][0]))
        self.invalid("duplicates transition")

    def test_triple_overlap(self):
        self.plan["shots"][0]["end_frame"] = 220
        self.plan["shots"][1]["end_frame"] = 240
        self.plan["transitions"][0].update(kind="dissolve", overlap_frames=124)
        self.plan["transitions"][1].update(kind="dissolve", overlap_frames=48)
        self.invalid("triple overlap")

    def test_insufficient_handles(self):
        self.plan["shots"][0]["source"]["available_frames"] = 119
        self.invalid("requires 120")

    def test_missing_source_reports_unassessed(self):
        self.plan["shots"][0].pop("source")
        result = self.result()
        self.assertTrue(result["valid_structure"])
        self.assertTrue(any("were not checked" in x for x in result["warnings"]))

    def test_missing_handle_field(self):
        self.plan["shots"][0]["source"].pop("tail_handle_frames")
        self.invalid("tail_handle_frames")

    def test_text_hold_exceeds_shot(self):
        self.plan["shots"][2]["text_hold_frames"] = 97
        self.invalid("text_hold_frames")

    def test_missing_purpose(self):
        self.plan["shots"][0].pop("purpose")
        self.invalid("purpose must")

    def test_malformed_shot(self):
        self.plan["shots"][1] = None
        self.invalid("must be an object")

    def test_unhashable_route_and_transition(self):
        self.plan["shots"][0]["route"] = []
        self.plan["transitions"][0]["kind"] = {}
        self.invalid("route must")

    def test_root_must_be_object(self):
        self.plan = []
        self.invalid("Plan must be")

    def test_empty_shots(self):
        self.plan["shots"] = []
        self.invalid("nonempty ordered")


class CliTests(unittest.TestCase):
    def run_text(self, text):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "plan.json"
            path.write_text(text, encoding="utf-8")
            process = subprocess.run([sys.executable, str(SCRIPT), str(path)], cwd=folder, text=True, capture_output=True)
            self.assertEqual(path.read_text(), text)
            self.assertNotIn("Traceback", process.stderr)
            return process, json.loads(process.stdout)

    def test_cli_from_other_directory(self):
        process, result = self.run_text(json.dumps(EXAMPLE))
        self.assertEqual(process.returncode, 0)
        self.assertTrue(result["valid_structure"])
        self.assertTrue(result["limitations"])

    def test_invalid_json(self):
        process, result = self.run_text("{broken")
        self.assertEqual(process.returncode, 2)
        self.assertFalse(result["valid_structure"])

    def test_duplicate_key(self):
        process, result = self.run_text('{"schema_version": 1, "schema_version": 2}')
        self.assertEqual(process.returncode, 2)
        self.assertIn("Duplicate JSON key", result["errors"][0])

    def test_nonfinite_numbers(self):
        for value in ("NaN", "Infinity", "-Infinity", "1e9999", "-1e9999"):
            with self.subTest(value=value):
                process, result = self.run_text('{"extra": ' + value + '}')
                self.assertEqual(process.returncode, 2)
                self.assertIn("Non-finite", result["errors"][0])

    def test_duplicate_nested_key(self):
        process, result = self.run_text('{"camera": {"move": "pan", "move": "tilt"}}')
        self.assertEqual(process.returncode, 2)
        self.assertIn("Duplicate JSON key", result["errors"][0])

    def test_error_with_escaped_surrogate_stays_json(self):
        process, result = self.run_text('{"\\ud800": 1, "\\ud800": 2}')
        self.assertEqual(process.returncode, 2)
        self.assertIn("Duplicate JSON key", result["errors"][0])

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            process = subprocess.run([sys.executable, str(SCRIPT), str(Path(folder) / "missing.json")], text=True, capture_output=True)
        self.assertEqual(process.returncode, 2)
        self.assertFalse(json.loads(process.stdout)["valid_structure"])
        self.assertNotIn("Traceback", process.stderr)


if __name__ == "__main__":
    unittest.main()
