# Shot contract and editorial timeline

## Contents

- [Write the directing card](#write-the-directing-card)
- [Separate the three kinds of control](#separate-the-three-kinds-of-control)
- [Use the machine-readable plan when timing matters](#use-the-machine-readable-plan-when-timing-matters)
- [Represent cuts and overlaps](#represent-cuts-and-overlaps)
- [Conform source counts before checking handles](#conform-source-counts-before-checking-handles)
- [Run the checker](#run-the-checker)
- [Interpret the result](#interpret-the-result)

## Write the directing card

Use a compact card for each shot, whether it will be captured, generated, animated or edited. Record only decisions that constrain the result.

```text
Shot ID / purpose / change in viewer understanding:
Opening: subject position, framing, background and point of attention
Action: principal subject event, secondary response, meaningful landing
Camera: viewpoint, height, move/path, focus target, lens intent and assumptions
Light/color: motivated source, contrast, palette roles, protected skin/brand colors
Timing: editorial interval, action/hold, needed source handles, sound cue
Continuity: identity, geometry, costume, props, eyeline, screen travel and light
Execution: actual tool/mode; reference roles; supported controls; post requirements
Acceptance: observable checks and hard failures
```

Example: "Reveal the lamp's hinge, show one plausible adjustment, then hold its final pose." Choose a medium-wide introduction, a close contact shot, and a settled product composition only if each adds useful information. A continuous shot may be better when uninterrupted action is the point.

## Separate the three kinds of control

| Kind | Example | Verification |
| --- | --- | --- |
| Hard control exposed by the tool | Delivery size, supported clip duration, actual start/end reference, deterministic keyframe | Inspect the real request/schema and output |
| Soft intent in a prompt | Restrained push-in, shallow focus, warm practical lighting, an action near a stated second | View the resulting frames and motion; do not assume compliance |
| Postproduction requirement | Exact wordmark, frame-accurate cut, subtitle hold, tracked overlay | Implement in the editor/compositor and inspect the export |

Do not turn desired optics into unsupported API parameters. Do not treat prose timestamps as guaranteed keyframes. The timeline below describes the edit; it is not a generation request, cost allocation or authorization document.

## Use the machine-readable plan when timing matters

Copy [the example](../assets/shot-plan.example.json) and adapt it. Use contract version 1 for a single ordered picture track with adjacent overlaps. Keep titles, graphics and complex multilayer work inside a shot's creative fields or in the actual editor. The checker intentionally does not model a full nonlinear editing timeline.

| Field | Requirement |
| --- | --- |
| `schema_version` | Integer `1`. |
| `title` | Nonempty descriptive string. |
| `fps` | Exact positive integer/rational string, such as `"24"` or `"24000/1001"`. A rounded decimal such as `"23.976"` is rejected. |
| `resolution` | Two positive integers `[width, height]`, interpreted as square-pixel delivery. |
| `aspect_ratio` | Optional positive `"w:h"` string that exactly matches the resolution. Omit if the workflow uses a different pixel-aspect contract. |
| `total_frames` | Positive integer number of frames on the editorial timeline. |
| `shots` | Nonempty ordered list of shot objects. |
| `transitions` | Optional list of explicit adjacent transitions. An omitted adjacent transition means a cut. |

Each shot requires:

| Field | Requirement |
| --- | --- |
| `id` | Unique nonempty string. |
| `purpose`, `primary_focus` | Nonempty strings stating what this shot does and where attention belongs. |
| `start_frame`, `end_frame` | Integers defining `[start_frame, end_frame)`. The end is exclusive. Both positions must increase strictly across shots. |
| `route` | One of `generate`, `capture`, `animate`, `composite`, `edit`, `hold`. This is planning metadata, not a tool command. |
| `invariants`, `checks` | Nonempty lists of nonempty strings. |
| `source` | Optional object with all three nonnegative integers: `available_frames`, `head_handle_frames`, `tail_handle_frames`. |
| `text_hold_frames` | Optional integer from zero through this shot's timeline duration. It does not prove readable text. |

Add creative fields such as `camera`, `subject_action`, `lighting`, `audio`, `references` or `notes` as needed. Unknown fields are retained and ignored by the checker. Review their spelling and meaning manually. JSON must not contain duplicate keys, `NaN` or infinities. Boolean values are not accepted as integer frame counts.

Begin the first shot at frame zero and end the last shot at `total_frames`. Represent intentional black, pauses, or still holds as explicit shots with appropriate purpose and route. A gap is otherwise an error. This contract permits only adjacent two-shot overlap, not nested or triple overlap.

## Represent cuts and overlaps

For a cut, shot A's exclusive end equals shot B's start. The optional transition has `kind: "cut"` and `overlap_frames: 0`.

For a dissolve, wipe or custom adjacent overlap, declare its length explicitly. Example at 24 fps:

```json
{
  "shots": [
    {"id": "A", "start_frame": 0, "end_frame": 108},
    {"id": "B", "start_frame": 96, "end_frame": 204},
    {"id": "C", "start_frame": 192, "end_frame": 288}
  ],
  "transitions": [
    {"from": "A", "to": "B", "kind": "dissolve", "overlap_frames": 12},
    {"from": "B", "to": "C", "kind": "dissolve", "overlap_frames": 12}
  ]
}
```

This timing excerpt spans 288 frames, or 12 seconds. The shot intervals sum to 312 frames because 24 frames are shared in overlaps. Add the other required shot and plan fields before validating. A non-cut transition with zero overlap is outside this contract; represent a dip through black as explicit shots or model it inside an editor-managed shot.

Overlap frames already belong to each shot interval. Do not add them a second time when computing the required source span. Reserved head/tail handles are extra available material outside that interval, useful for changing the edit later.

## Conform source counts before checking handles

The checker compares all counts at the declared timeline rate. For a shot covering 96 timeline frames with 12 head and 12 tail handle frames, declare at least 120 available conformed frames. If the source has not been inspected or conformed, omit `source`; the checker will report that this check was not performed.

Do not insert the raw frame count from a variable-frame-rate clip or a different source rate. First determine its actual timestamps, intended speed/retiming and editorial conform. A 120-frame source captured at 60 fps does not automatically provide 120 frames of ordinary-speed action on a 24 fps timeline. Frame repetition or interpolation changes the time mapping and must be evaluated in the actual editor.

Distinguish generation duration, downloaded duration and selected editorial span. If a tool produces only allowed whole-second clip lengths, generate a supported span with enough usable action and trim it. The checker does not determine those live model limits or whether retiming is visually acceptable.

## Run the checker

Use the script's absolute path so it works from any working directory:

```bash
python3 /absolute/path/to/cinematic-director/scripts/check_plan.py /absolute/path/to/shot-plan.json
```

No dependency installation, network call, media upload or paid generation is required. The input file is read only. Exit code `0` means valid declared structure; `2` means invalid structure or unreadable/invalid JSON. The result is JSON with `valid_structure`, `errors`, `warnings`, `summary` and `limitations`.

The summary reports the reduced exact frame rate, total frames, exact seconds and a rounded decimal display. Use the exact value for arithmetic. At `24000/1001` fps, 288 frames last `3003/250` seconds, or 12.012 seconds; they are not exactly 12 seconds.

## Interpret the result

Correct errors before passing the timeline onward. Review warnings about source availability as missing checks, not failures of the creative plan. A valid structure does not prove that a shot has enough readable text time, that a source contains the intended action, or that the edit feels good.

Inspect actual media, normal-speed playback, continuity, sound, delivery cropping and the final encode separately. Let the execution skill validate current tool parameters, spending authority and job state. The contract and checker are original workflow aids for this skill, not a vendor API schema or aesthetic scoring system.
