#!/usr/bin/env python3
"""Validate a single-track editorial plan, without reading or generating media."""

import argparse
import json
import math
import re
from fractions import Fraction
from pathlib import Path


LIMITATIONS = [
    "Checks declared timeline structure and arithmetic only.",
    "Does not inspect media, aesthetics, readability, continuity, sound or provenance.",
    "Does not validate current model capabilities, cost or authorization.",
    "Source frame counts must already be conformed to the declared timeline rate.",
]
ROUTES = {"generate", "capture", "animate", "composite", "edit", "hold"}
KINDS = {"cut", "dissolve", "wipe", "custom"}


def _integer(value, minimum=0):
    return type(value) is int and value >= minimum


def _string(value):
    return isinstance(value, str) and bool(value.strip())


def _string_list(value):
    return isinstance(value, list) and bool(value) and all(_string(x) for x in value)


def _reject_constant(value):
    raise ValueError(f"Non-finite JSON number is not allowed: {value}")


def _finite_float(value):
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ValueError(f"Non-finite JSON number is not allowed: {value}")
    return parsed


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_plan(path):
    """Read strict JSON, rejecting ambiguous duplicate keys and NaN/Infinity."""
    return json.loads(
        Path(path).read_text(encoding="utf-8"),
        parse_constant=_reject_constant,
        parse_float=_finite_float,
        object_pairs_hook=_unique_object,
    )


def validate_plan(plan):
    """Return diagnostics without mutating the supplied object."""
    result = {
        "valid_structure": False,
        "errors": [],
        "warnings": [],
        "summary": {},
        "limitations": list(LIMITATIONS),
    }
    errors, warnings = result["errors"], result["warnings"]
    if not isinstance(plan, dict):
        errors.append("Plan must be a JSON object.")
        return result
    if type(plan.get("schema_version")) is not int or plan["schema_version"] != 1:
        errors.append("schema_version must be integer 1.")
    if not _string(plan.get("title")):
        errors.append("title must be a nonempty string.")

    fps = None
    fps_text = plan.get("fps")
    if isinstance(fps_text, str) and re.fullmatch(r"[1-9][0-9]*(?:/[1-9][0-9]*)?", fps_text):
        try:
            fps = Fraction(fps_text)
        except (ValueError, ZeroDivisionError):
            pass
    if fps is None:
        errors.append("fps must be an exact positive integer or rational string, such as '24' or '24000/1001'.")

    resolution = plan.get("resolution")
    resolution_ok = (
        isinstance(resolution, list)
        and len(resolution) == 2
        and all(_integer(x, 1) for x in resolution)
    )
    if not resolution_ok:
        errors.append("resolution must contain two positive integers: [width, height].")
    if "aspect_ratio" in plan:
        ratio = plan["aspect_ratio"]
        if not isinstance(ratio, str) or not re.fullmatch(r"[1-9][0-9]*:[1-9][0-9]*", ratio):
            errors.append("aspect_ratio must be a positive w:h string.")
        elif resolution_ok:
            width, height = map(int, ratio.split(":"))
            if Fraction(*resolution) != Fraction(width, height):
                errors.append("aspect_ratio does not exactly match resolution; declare the intended square-pixel delivery size.")

    total = plan.get("total_frames")
    total_ok = _integer(total, 1)
    if not total_ok:
        errors.append("total_frames must be a positive integer.")
    if fps is not None and total_ok:
        duration = Fraction(total) / fps
        result["summary"].update({
            "fps_exact": f"{fps.numerator}/{fps.denominator}",
            "total_frames": total,
            "duration_seconds_exact": f"{duration.numerator}/{duration.denominator}",
            "duration_seconds_decimal": format(float(duration), ".9f"),
        })

    shots = plan.get("shots")
    if not isinstance(shots, list) or not shots:
        errors.append("shots must be a nonempty ordered list.")
        return result
    result["summary"]["shot_count"] = len(shots)
    ids, timing = set(), []
    for index, shot in enumerate(shots):
        path = f"shots[{index}]"
        if not isinstance(shot, dict):
            errors.append(f"{path} must be an object.")
            timing.append(None)
            continue
        shot_id = shot.get("id")
        if not _string(shot_id):
            errors.append(f"{path}.id must be a nonempty string.")
        elif shot_id in ids:
            errors.append(f"{path}.id duplicates {shot_id!r}.")
        else:
            ids.add(shot_id)
        for field in ("purpose", "primary_focus"):
            if not _string(shot.get(field)):
                errors.append(f"{path}.{field} must be a nonempty string.")
        for field in ("invariants", "checks"):
            if not _string_list(shot.get(field)):
                errors.append(f"{path}.{field} must be a nonempty list of nonempty strings.")
        if not isinstance(shot.get("route"), str) or shot["route"] not in ROUTES:
            errors.append(f"{path}.route must be one of {', '.join(sorted(ROUTES))}.")

        start, end = shot.get("start_frame"), shot.get("end_frame")
        duration = None
        if not _integer(start) or not _integer(end, 1):
            errors.append(f"{path} requires integer start_frame >= 0 and end_frame > 0.")
            timing.append(None)
        elif end <= start:
            errors.append(f"{path}.end_frame must be greater than start_frame.")
            timing.append(None)
        else:
            timing.append((start, end))
            duration = end - start
            if total_ok and end > total:
                errors.append(f"{path}.end_frame exceeds total_frames.")

        if "text_hold_frames" in shot:
            hold = shot["text_hold_frames"]
            if not _integer(hold) or (duration is not None and hold > duration):
                errors.append(f"{path}.text_hold_frames must be an integer from 0 through the shot duration.")

        if "source" not in shot:
            warnings.append(f"{path}.source omitted; available source frames and handles were not checked.")
        elif not isinstance(shot["source"], dict):
            errors.append(f"{path}.source must be an object.")
        else:
            source = shot["source"]
            fields = ("available_frames", "head_handle_frames", "tail_handle_frames")
            source_ok = True
            for field in fields:
                if not _integer(source.get(field)):
                    errors.append(f"{path}.source.{field} must be a nonnegative integer at the conformed timeline rate.")
                    source_ok = False
            if source_ok and duration is not None:
                needed = duration + source["head_handle_frames"] + source["tail_handle_frames"]
                if source["available_frames"] < needed:
                    errors.append(f"{path}.source has {source['available_frames']} frames; duration plus reserved handles requires {needed}.")

    if timing[0] is not None and timing[0][0] != 0:
        errors.append("The first shot must start at frame 0; use an explicit hold/black shot for leading space.")
    if total_ok and timing[-1] is not None and timing[-1][1] != total:
        errors.append("The last shot must end at total_frames.")

    adjacent = set()
    for left, right in zip(shots, shots[1:]):
        if isinstance(left, dict) and isinstance(right, dict) and _string(left.get("id")) and _string(right.get("id")):
            adjacent.add((left["id"], right["id"]))
    transition_map = {}
    transitions = plan.get("transitions", [])
    if not isinstance(transitions, list):
        errors.append("transitions must be a list when supplied.")
        transitions = []
    for index, transition in enumerate(transitions):
        path = f"transitions[{index}]"
        if not isinstance(transition, dict):
            errors.append(f"{path} must be an object.")
            continue
        left, right = transition.get("from"), transition.get("to")
        if not _string(left) or not _string(right):
            errors.append(f"{path}.from and .to must be nonempty shot IDs.")
            continue
        pair = (left, right)
        if pair not in adjacent:
            errors.append(f"{path} must connect adjacent shots in their listed order.")
        if pair in transition_map:
            errors.append(f"{path} duplicates transition {left!r} to {right!r}.")
        transition_map[pair] = transition
        kind, overlap = transition.get("kind"), transition.get("overlap_frames")
        if not isinstance(kind, str) or kind not in KINDS:
            errors.append(f"{path}.kind must be cut, dissolve, wipe or custom.")
        if not _integer(overlap):
            errors.append(f"{path}.overlap_frames must be a nonnegative integer.")
        elif kind == "cut" and overlap != 0:
            errors.append(f"{path}: a cut must have zero overlap_frames.")
        elif isinstance(kind, str) and kind in KINDS - {"cut"} and overlap == 0:
            errors.append(f"{path}: a non-cut transition requires positive overlap_frames in this contract.")

    for index in range(1, len(shots)):
        previous, current = timing[index - 1], timing[index]
        if previous is None or current is None:
            continue
        if current[0] <= previous[0] or current[1] <= previous[1]:
            errors.append(f"shots[{index}]: shot start and end positions must increase strictly.")
        if current[0] > previous[1]:
            errors.append(f"Gap before shots[{index}]; represent intended black/hold frames as a shot.")
        overlap = max(0, previous[1] - current[0])
        left, right = shots[index - 1].get("id"), shots[index].get("id")
        transition = transition_map.get((left, right)) if _string(left) and _string(right) else None
        if transition is None:
            if overlap:
                errors.append(f"shots[{index}]: {overlap} overlapping frames require an explicit non-cut transition.")
        elif _integer(transition.get("overlap_frames")) and transition["overlap_frames"] != overlap:
            errors.append(f"Transition before shots[{index}] declares {transition['overlap_frames']} overlapping frames; timeline has {overlap}.")
        if index >= 2 and timing[index - 2] is not None and current[0] < timing[index - 2][1]:
            errors.append(f"shots[{index}]: triple overlap is outside this single-track contract.")

    result["valid_structure"] = not errors
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", help="Path to a shot-plan JSON file")
    args = parser.parse_args(argv)
    try:
        result = validate_plan(read_plan(args.plan))
    except (OSError, UnicodeError, ValueError, OverflowError, RecursionError) as exc:
        result = {
            "valid_structure": False,
            "errors": [f"Could not read or validate plan: {exc}"],
            "warnings": [],
            "summary": {},
            "limitations": list(LIMITATIONS),
        }
    print(json.dumps(result, indent=2, ensure_ascii=True, allow_nan=False))
    return 0 if result["valid_structure"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
