# Quality review and bounded repair

## Contents

- [Set observable acceptance](#set-observable-acceptance)
- [Inspect at three scales](#inspect-at-three-scales)
- [Classify defects and choose a repair](#classify-defects-and-choose-a-repair)
- [Record evidence](#record-evidence)
- [Run the repair loop](#run-the-repair-loop)
- [Verify the delivered file](#verify-the-delivered-file)
- [Sources and limits](#sources-and-limits)

## Set observable acceptance

Evaluate the intended production style. Stop-motion stepping, stylized anatomy, a motivated jump cut, a clean product surface, or intentional chromatic abstraction can be valid. Ask whether an observation violates the brief, continuity or the scene's own rules before calling it a defect.

Define critical and major failures before expensive production. Example: "The clasp opens with consistent hinge topology; the hand maintains contact; the brand mark is exact; the final pose remains readable for the agreed hold." Avoid "100% cinematic," "zero AI score," or "indistinguishable from reality" as testable gates.

Keep production quality and origin separate. A fully generated shot can pass its visual brief; real footage can fail continuity or finishing. Preserve original files and provenance, including known generation/edit history. Use the AI Detector companion's actual schema for origin assessments. [S1, S2]

## Inspect at three scales

| Pass | Inspect | Can establish | Cannot establish alone |
| --- | --- | --- | --- |
| Whole sequence, normal speed, intended display size | Story clarity, primary attention, rhythm, transitions, screen direction, comfort, actual sound | What a viewer can follow and perceive in that presentation | Native pixel detail, provenance, every one-frame defect |
| Native frame and contextual crop | Anatomy, contacts, edges, type, speculars, light direction, textures and composition | Spatial evidence in the frames examined | Temporal coherence or lip sync across the clip |
| Consecutive frames around incidents | Identity, topology, occlusion order, reflection motion, shape persistence, cuts and sync | Reproducible temporal behavior in the inspected interval | Uninspected footage or authentic origin |

Inspect the full accessible sequence, then sample every shot's start, action peak and landing. Add dense consecutive frames around risky contacts, fast movement, occlusions, generated transitions and reported incidents. Sampling is triage; state uncovered intervals. A sparse contact sheet cannot prove absence of flicker between its samples.

Use `ffprobe` or an equivalent available tool to identify actual dimensions, stream frame rates, duration, color metadata and audio tracks. Treat variable-frame-rate timestamps and edit timecodes carefully: preserve presentation timestamps or document the conformed mapping. Do not multiply an approximate frame index by a nominal rate and report false millisecond precision. Use the companion's incident inspector if available. [S1, S4]

Keep the original immutable. Label proxies, resizes, crops, stabilization and transcodes. Record the coordinate mapping so a reported region can be reproduced on the original. Do not use generative upscale as evidence of original detail.

If playback or audio inspection is unavailable, perform the available checks and mark pacing, temporal continuity or sync as **not assessed**, as appropriate. Do not substitute a model's written scene description for viewing the pixels or hearing the track.

## Classify defects and choose a repair

| Defect | First diagnostic question | Preferred local repair | Acceptance check |
| --- | --- | --- | --- |
| Hand or prop topology changes | Is the grip ambiguous in the source, or does the change happen during occlusion? | Fix the anchor/pose; regenerate the short incident or composite a validated element | Joint count, contact, occlusion and shadow persist through neighboring frames |
| Identity/wardrobe drift | Did references conflict, or did the view expose unseen design? | Build consistent views; replace the outlier shot/region while preserving approved features | Same stable design across angles and joins |
| Unwanted background morphing | Is parallax feasible for the anchored image and camera move? | Reduce move; use a modeled background, tracked patch, or stronger controlled reference | Rigid world geometry and coherent parallax at real-time speed |
| Camera movement feels weightless | Is acceleration arbitrary, perspective inconsistent, or the camera crossing solid geometry? | Block a feasible path and meaningful landing; simplify or animate deterministically | Plausible clearance, speed, inertia and attention |
| Scene feels flat | Does the key fail to describe form, or do subject/background values merge? | Restage or relight the actual relationship; adjust selective contrast after correction | Clear hierarchy without crushed features or false rim light |
| Skin looks waxy | Is it lighting/makeup, denoising, a generated texture, or compression? | Correct the cause locally; recover natural variation without an indiscriminate pore overlay | Appropriate skin detail at intended size and native crop |
| Logo or type is malformed | Is exact artwork available? | Typeset or composite approved artwork with perspective/lighting/occlusion | Exact characters and geometry in the delivered frame |
| Grade breaks between shots | Are inputs, exposure or transforms mismatched? | Correct transforms and base balance, then match the shared look | Plausible cut-to-cut brightness, hue and skin/material response |
| Grain shimmers or muddies the encode | Is scale/strength wrong for delivery or temporal grain incompatible with compression? | Reduce or reposition the effect; test the real codec at delivery scale | Texture supports the look without obscuring information |
| Shake hides the subject | Is there a motivated impulse and stable reading interval? | Reduce amplitude/frequency; shorten decay; stabilize or change the shot | Intended energy with readable action and stable horizon when required |
| Edit feels rushed | Is the viewer still identifying the subject or reading text? | Reallocate hold/action/reaction time or simplify the information | First-time viewer can understand the beat at normal playback |
| Mouth and sound disagree | Is this a mux/timeline offset or incorrect articulation? | Correct offset first, then repair only the performance if necessary | Speech closures and phrase timing align across the full utterance |

Severity is contextual:

- **Critical:** the shot fails its purpose, violates required identity/product geometry, depicts impossible central action, or omits mandatory content. Block acceptance.
- **Major:** visible continuity, legibility, lighting, sync or motion error materially distracts or miscommunicates. Repair or explicitly obtain acceptance of the limitation.
- **Minor:** cosmetic difference that does not damage the brief. Fix only when justified by delivery needs and remaining resources.

Do not average a critical failure away with attractive color or music. Do not use darkness, grain, blur, fast cuts or crop to conceal a defect the deliverable still requires the viewer to understand. A reframing or edit is valid when it intentionally changes coverage and still satisfies the brief.

## Record evidence

Use a compact incident ledger. Follow the AI Detector's report schema when handing work to it; this director's ledger is not a substitute for that schema.

```text
ID / asset and version:
Location: timestamp interval, frame/PTS convention, optional original-pixel bbox
Observation: what actually changes or fails, without a cause claim
Severity and impact on the brief:
Hypothesis and plausible alternative explanation:
Repair: affected region/shot and one proposed change
Preserve: identity, geometry, light, framing, audio and accepted neighbors
Acceptance: same inspection interval plus surrounding context
Evidence: original/proxy mapping, crops/frames and playback coverage
Status: open / repaired-and-rechecked / accepted limitation / not assessed
```

Example: "Between 1.40 and 1.56 seconds, the ring becomes part of the finger silhouette during the grasp. The adjacent frames do not show a plausible occluder." This is more useful than "AI hands." A second reviewer should be able to reproduce the observation without trusting the first reviewer's adjective.

## Run the repair loop

1. Preserve the baseline and mark accepted shots or regions.
2. Select the highest-impact reproducible defect. Form one testable cause hypothesis.
3. Choose the smallest effective operation: source correction, mask/track, retime, local regenerate, deterministic replacement, or revised coverage. Account for how it affects neighboring frames and sound.
4. Execute within the existing authorization, budget and attempt cap. Recover unknown job state before another submission.
5. Compare repaired and baseline versions using the same view, scale, color transform and interval. Inspect the repaired area and neighboring areas/frames for regression.
6. Review the whole edited sequence at normal speed. A locally good patch may break the larger cut.
7. Stop when critical/major failures are resolved and the brief is met. After two unsuccessful attempts on the same defect, change the route or report the limitation, subject to any lower cap.

When possible, ask a fresh reviewer to inspect without being told which version should win. Share the brief and actual media, not the desired verdict. Keep comparative claims scoped to the versions and settings tested.

## Verify the delivered file

Inspect the **export**, not only the timeline preview. Check duration/frame count or actual timestamps, framing in every required ratio, color transform/tagging, no accidental letterbox/crop, correct titles and subtitles, audible intelligible dialogue, sync, intended start/end, and absence of accidental black/frozen frames or missing media. Reopen on the actual destination when accessible.

Check grain, fine text, gradients and rapid motion in the final compression. Verify the required caption and reduced-motion versions separately. Record which checks were actually performed and which remain for the delivery environment.

## Sources and limits

Accessed 2026-11-18:

- **S1:** [AI Detector inspection workflow](https://github.com/MikeyNu/agent-ai-detector/blob/main/SKILL.md) and [report contract](https://github.com/MikeyNu/agent-ai-detector/blob/main/references/report-template.md).
- **S2:** [AI Detector remediation playbook](https://github.com/MikeyNu/agent-ai-detector/blob/main/references/remediation-playbook.md).
- **S3:** [Runway I2V guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide), for source-image artifacts, motion cues and limits of prompted stillness.
- **S4:** [FFmpeg ffprobe documentation](https://ffmpeg.org/ffprobe.html), for inspecting actual stream and frame metadata.

The severity framework, example ledger and bounded repair sequence are production recommendations synthesized for this skill. They are not an authenticity classifier or a validated aesthetic benchmark.
