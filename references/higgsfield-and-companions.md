# Tools and companion skills

## Contents

- [Resolve the execution surface](#resolve-the-execution-surface)
- [Pass a concrete directing brief](#pass-a-concrete-directing-brief)
- [Compile for the supported mode](#compile-for-the-supported-mode)
- [Protect continuity and execution state](#protect-continuity-and-execution-state)
- [Collaborate with AI Detector](#collaborate-with-ai-detector)
- [Collaborate with speech and scroll skills](#collaborate-with-speech-and-scroll-skills)
- [Capability snapshot and sources](#capability-snapshot-and-sources)

## Resolve the execution surface

Read any relevant skill explicitly supplied in the user's prompt. Resolve names from installed skill metadata, not guessed filesystem paths. The user's current constraints and existing authorization govern the task; preserve the executing tool's real permissions and spending gates. Do not request approval again for a step already covered.

Use the user's **Higgsfield Director**, name `higgsfield-director`, for model routing, supported inputs, generation, editing, cost allocation and recovery. Use the Higgsfield plugin's routing skill when available, especially for exact slash commands and preset workflows. These can coexist: the personal skill carries production discipline, while the plugin supplies live execution instructions.

| Requested work | Discover or inspect | Produce |
| --- | --- | --- |
| Plan only | Available media and requested tool constraints | Treatment, shot cards, edit/QA plan; no generation job |
| Generate a shot | Current model catalog, exact selected model, input mode, parameter schema and quote | Supported request and bounded job tracking |
| Execute a named preset or slash command | Exact `get_preset_instructions` lookup, if exposed | That workflow with its required inputs and session |
| Edit existing footage | Actual editor capability, media location/permissions, current timeline | Localized edit with preserved source and tested export |
| Inspect footage | Actual accessible media, decoding/analysis tools and playback | Observations with coverage and limitations |

Do not replace an unavailable editor with a different environment silently. Higgsfield's Video Editor/Katana, Blender and After Effects routes can have environment-specific instructions. Fetch those only when executing that route. Finding documentation does not mean the editor is installed or a render completed.

## Pass a concrete directing brief

Send a compact contract, not a general request to "make it cinematic":

```text
Intent: generate one product shot within the already approved allocation.
Delivery: 16:9, editorial use of 96 frames at 24 fps, clean label landing.
Beat: reveal the hinge design, then let the viewer inspect it.
Subject action: lid opens once and settles; hinge stays mechanically coherent.
Camera: stable close three-quarter viewpoint, a restrained lateral translation,
        level horizon, ending with the logo unobscured.
References: approved product image = geometry/material; frame sketch = staging.
Invariants: exact proportions, hinge count, wordmark, finish and background light.
Focus/light: hinge and label remain readable; broad reflected key defines metal.
Execution: supported I2V anchor; current duration control; logo composite if needed.
Acceptance: plausible contact/hinge motion, stable geometry, legible final label,
            no unrequested cut, usable head/tail material for the edit.
```

The executor must resolve a real model ID, mode, reference roles and supported values. Never turn a desired lens, aperture or camera name into an invented API field. Treat a millimeter value in a prompt as a requested visual relationship unless the runtime exposes an actual camera model.

For a generated clip longer than the edit requires, reserve enough usable action and trim in the editor. Distinguish requested generation seconds, actual output duration and editorial frames. Plan extra handles only within the selected model's support and the approved allocation. If an exact event must happen on frame 72, use deterministic animation/editing or supported keyframes and verify the result.

## Compile for the supported mode

| Mode | Keep stable | Describe or control |
| --- | --- | --- |
| Text to image/video | The intended scene, subject identity and material hierarchy | Staging, light, one principal event and motivated camera behavior |
| Image to video | The inspected appearance/composition anchor | What changes: subject action, camera motion, environment response and landing |
| Reference to video | Explicit identity/location/style roles | The action and relations across the accepted references |
| First/end frame | Both frame designs and continuity assumptions | A feasible path; intermediate geometry still requires inspection |
| Motion transfer | Approved appearance and a suitable driving performance | The actual exposed motion reference mode, framing and limb visibility |
| Masked or localized edit | Accepted surrounding pixels, identity and timing | One defect, its scope, the requested change and preserved properties |
| Deterministic animation/composite | Scene geometry, camera and approved source graphics | Exact trajectories, timing, tracked logos, type, mattes and color pipeline |

For I2V, fix malformed hands, ambiguous contacts or conflicting motion cues in the still first. Do not redescribe a new scene that contradicts the anchor. Runway's current I2V guide supports this motion-focused approach, but its controls are specific to its model. Transfer the reasoning to another provider only after checking that provider's actual mode. [S3]

Use references only for their supported roles. Upload order is not a universal identity syntax. Keep private media URLs, tokens and client references out of public plans. An estimate that imports a remote image is not a purely observational lookup; follow the actual tool's data-handling instructions.

## Protect continuity and execution state

Maintain a small continuity bible across shots: stable subject features, proportions, costume/props, key direction and exposure relationships, world layout, screen travel, eyelines, audio atmosphere and intended stylistic discontinuities. Attach only relevant references to a shot. A large conflicting reference set can obscure the invariant.

Start with a representative shot or cheap blockout when it resolves a specific uncertainty. A cheap model's successful result does not prove a different final model will behave identically. Keep the selected take, its media identifier, actual settings, provenance and acceptance notes.

Before any paid operation, let the execution skill apply the authorized total, stage allocation, attempt cap and payment path. Do not interpret a retry as free. Keep pending or ambiguous jobs reserved against that allocation. If the response is lost, recover status through the existing job/session or request fingerprint before deciding whether resubmission is safe. Do not substitute credits when the user asked to use a free or unlimited entitlement and the tool rejects it.

If the same defect persists after two targeted attempts, change the route: simplify the shot, revise the anchor, composite a reliable element, use a deterministic scene, or explain the constraint. Respect any lower cap. Do not regenerate already accepted material merely because another take might look nicer.

## Collaborate with AI Detector

Use the user's `agent-ai-detector` in its **quality** lane for visual improvement. Supply:

- Original or best available media, lineage, intended style and delivery context.
- Known generation/capture origin as evidence, without fabricating cryptographic verification.
- Invariants and a prioritized suspected incident with context, when already observed.
- Requested inspection coverage: full playback, native stills, consecutive frames, audio sync.

Let that skill emit its real report schema and validate it with its own validator. Do not invent a generic detector score or translate a beautiful image into a claim of camera capture.

Its quality labels are `passes_visual_qa`, `needs_revision` and `not_assessed`. Its origin labels are `confirmed_ai_origin`, `verified_capture_provenance`, `suspected_ai_involvement`, `no_ai_evidence_found` and `indeterminate`. Its strict schema requires verified binding/trust information for confirmed provenance labels. Record known tool generation in the production record, and let the detector choose a schema-valid label based on the evidence it actually verifies. [S5]

For each finding, retain the detector's observation, location, alternative explanation and severity. Return a repair brief to the appropriate executor. After repair, request the same checks on the affected region, neighboring frames and sequence context. Accept quality when the observable brief is satisfied; preserve truthful provenance. "No AI evidence found" is a bounded inspection outcome, not proof of capture.

If the detector is unavailable, perform the [local quality workflow](quality-and-repair.md), label it as a director's inspection, and state the missing independent pass. Do not claim that a companion skill ran.

## Collaborate with speech and scroll skills

For `elevenlabs-speech`, pass the dialogue/voiceover's purpose, relationship to the listener, performance arc, required pronunciation, and available time. Request the actual approved take before final timing. Keep exact spoken copy separate from camera direction. Do not compress speech to meet a locked cut if it harms intelligibility; revise the edit or the agreed copy.

For `cinematic-scroll-director`, pass scene topology, opening/landing compositions, visual beat order, camera path intent, settled reading positions and identity/light invariants. Keep website copy semantic and readable, plan mobile framing and reduced motion, and leave browser presentation/frame-delivery validation to that skill. A cinematic background does not justify unreadable interface text or inaccessible motion.

## Capability snapshot and sources

Checked **2026-11-18**. Treat this as a reason to discover current support, not as a permanent model recommendation:

- Higgsfield's website guide describes Cinema Studio 4.0 with UI lens/aperture/director controls and a separate API route. [S1]
- In the connected catalog inspected for this skill, a search for cinema camera controls returned `cinematic_studio_video_v2`, with 3 to 12 second duration and image/start/end image roles. The inspected schema exposed genre, mode, sound, speed ramp and multi-shot settings, but no dedicated focal-length or aperture fields. A separate search for Cinema Studio 4 returned no result in that catalog at that moment. This narrow observation does not establish platform-wide unavailability.
- Resolve the live catalog and preset route again when executing. Do not mix website labels, another provider's API, and the connected tool's request schema.

Sources, accessed 2026-11-18:

- **S1:** [Higgsfield, Cinema Studio 4.0 complete guide](https://higgsfield.ai/blog/cinema-studio-4-0-complete-guide). First-party UI/API overview; marketing examples are not measured optical guarantees.
- **S2:** [Higgsfield, camera control workflow](https://higgsfield.ai/blog/ai-video-camera-control). Use motion vocabulary and planning ideas, not unsupported claims of perfect physical simulation.
- **S3:** [Runway, Image to Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide). Current page identifies Gen-4.5 as its optimization target.
- **S4:** [User's Higgsfield Director skill](https://github.com/MikeyNu/agent-higgsfield/blob/main/skills/higgsfield-director/SKILL.md) and [shot planning](https://github.com/MikeyNu/agent-higgsfield/blob/main/skills/higgsfield-director/references/shot-planning.md). Read the installed version at execution time.
- **S5:** [User's AI Detector skill](https://github.com/MikeyNu/agent-ai-detector/blob/main/SKILL.md) and [report contract](https://github.com/MikeyNu/agent-ai-detector/blob/main/references/report-template.md). Keep its quality and origin decisions independent.

The brief, role boundaries and recovery examples above are workflow synthesis. The catalog observation is from the connected tools, not a copied website promise. No account balances or private media identifiers are needed to use it.
