# Local verification on 2026-11-18

These are actual offline tool outputs. They do not report hosted CI or media quality.

## Skill creator validation

Exit code: 0

```text
Skill is valid!
```

## Repository structure

Exit code: 0

```text
{
  "ok": true,
  "errors": [],
  "markdown_files": 13,
  "entrypoint_words": 1629,
  "entrypoint_lines": 94
}
```

## Timeline checker tests

Exit code: 0

```text
test_cli_from_other_directory (test_check_plan.CliTests.test_cli_from_other_directory) ... ok
test_duplicate_key (test_check_plan.CliTests.test_duplicate_key) ... ok
test_duplicate_nested_key (test_check_plan.CliTests.test_duplicate_nested_key) ... ok
test_error_with_escaped_surrogate_stays_json (test_check_plan.CliTests.test_error_with_escaped_surrogate_stays_json) ... ok
test_invalid_json (test_check_plan.CliTests.test_invalid_json) ... ok
test_missing_file (test_check_plan.CliTests.test_missing_file) ... ok
test_nonfinite_numbers (test_check_plan.CliTests.test_nonfinite_numbers) ... ok
test_bool_frames_rejected (test_check_plan.PlanTests.test_bool_frames_rejected) ... ok
test_bool_version_rejected (test_check_plan.PlanTests.test_bool_version_rejected) ... ok
test_cut_cannot_overlap (test_check_plan.PlanTests.test_cut_cannot_overlap) ... ok
test_duplicate_ids (test_check_plan.PlanTests.test_duplicate_ids) ... ok
test_duplicate_transition (test_check_plan.PlanTests.test_duplicate_transition) ... ok
test_empty_shots (test_check_plan.PlanTests.test_empty_shots) ... ok
test_end_mismatch (test_check_plan.PlanTests.test_end_mismatch) ... ok
test_example_exact_duration (test_check_plan.PlanTests.test_example_exact_duration) ... ok
test_gap_requires_explicit_hold (test_check_plan.PlanTests.test_gap_requires_explicit_hold) ... ok
test_input_not_mutated (test_check_plan.PlanTests.test_input_not_mutated) ... ok
test_insufficient_handles (test_check_plan.PlanTests.test_insufficient_handles) ... ok
test_leading_gap (test_check_plan.PlanTests.test_leading_gap) ... ok
test_malformed_shot (test_check_plan.PlanTests.test_malformed_shot) ... ok
test_misordered_shots (test_check_plan.PlanTests.test_misordered_shots) ... ok
test_missing_handle_field (test_check_plan.PlanTests.test_missing_handle_field) ... ok
test_missing_purpose (test_check_plan.PlanTests.test_missing_purpose) ... ok
test_missing_source_reports_unassessed (test_check_plan.PlanTests.test_missing_source_reports_unassessed) ... ok
test_nonadjacent_transition (test_check_plan.PlanTests.test_nonadjacent_transition) ... ok
test_noncut_needs_overlap (test_check_plan.PlanTests.test_noncut_needs_overlap) ... ok
test_numeric_rate_rejected (test_check_plan.PlanTests.test_numeric_rate_rejected) ... ok
test_overlap_requires_declaration (test_check_plan.PlanTests.test_overlap_requires_declaration) ... ok
test_ratio_mismatch (test_check_plan.PlanTests.test_ratio_mismatch) ... ok
test_rational_rate_exact (test_check_plan.PlanTests.test_rational_rate_exact) ... ok
test_resolution_types (test_check_plan.PlanTests.test_resolution_types) ... ok
test_root_must_be_object (test_check_plan.PlanTests.test_root_must_be_object) ... ok
test_rounded_rate_rejected (test_check_plan.PlanTests.test_rounded_rate_rejected) ... ok
test_text_hold_exceeds_shot (test_check_plan.PlanTests.test_text_hold_exceeds_shot) ... ok
test_triple_overlap (test_check_plan.PlanTests.test_triple_overlap) ... ok
test_unhashable_route_and_transition (test_check_plan.PlanTests.test_unhashable_route_and_transition) ... ok
test_unknown_creative_fields_allowed (test_check_plan.PlanTests.test_unknown_creative_fields_allowed) ... ok
test_valid_dissolves (test_check_plan.PlanTests.test_valid_dissolves) ... ok
test_wrong_overlap_count (test_check_plan.PlanTests.test_wrong_overlap_count) ... ok
test_zero_denominator_rejected (test_check_plan.PlanTests.test_zero_denominator_rejected) ... ok
test_zero_length_shot (test_check_plan.PlanTests.test_zero_length_shot) ... ok

----------------------------------------------------------------------
Ran 41 tests in 0.846s

OK
```

## Fresh-agent Brief I plan

Exit code: 0

```text
{
  "valid_structure": true,
  "errors": [],
  "warnings": [
    "shots[0].source omitted; available source frames and handles were not checked.",
    "shots[1].source omitted; available source frames and handles were not checked."
  ],
  "summary": {
    "fps_exact": "24/1",
    "total_frames": 288,
    "duration_seconds_exact": "12/1",
    "duration_seconds_decimal": "12.000000000",
    "shot_count": 3
  },
  "limitations": [
    "Checks declared timeline structure and arithmetic only.",
    "Does not inspect media, aesthetics, readability, continuity, sound or provenance.",
    "Does not validate current model capabilities, cost or authorization.",
    "Source frame counts must already be conformed to the declared timeline rate."
  ]
}
```

## Bundled example plan

Exit code: 0

```text
{
  "valid_structure": true,
  "errors": [],
  "warnings": [],
  "summary": {
    "fps_exact": "24/1",
    "total_frames": 288,
    "duration_seconds_exact": "12/1",
    "duration_seconds_decimal": "12.000000000",
    "shot_count": 3
  },
  "limitations": [
    "Checks declared timeline structure and arithmetic only.",
    "Does not inspect media, aesthetics, readability, continuity, sound or provenance.",
    "Does not validate current model capabilities, cost or authorization.",
    "Source frame counts must already be conformed to the declared timeline rate."
  ]
}
```
