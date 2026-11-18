# Pacing and editing

Research snapshot: 18 November 2026. Numerical examples are editorial examples, not recipes or promised AI controls.

## Contents

- [Build rhythm from information](#build-rhythm-from-information)
- [Plan coverage and continuity](#plan-coverage-and-continuity)
- [Choose the join](#choose-the-join)
- [Protect transition handles](#protect-transition-handles)
- [Edit picture and sound together](#edit-picture-and-sound-together)
- [Keep time and sampling distinct](#keep-time-and-sampling-distinct)
- [Deliver readable and accessible motion](#deliver-readable-and-accessible-motion)
- [Review under real constraints](#review-under-real-constraints)
- [Sources](#sources)

## Build rhythm from information

For each beat, state what the audience knows, what changes, and what they should feel afterward. Choose duration from performance, information density, recognition, reading, and adjacent beats. A fixed cut interval cannot account for these needs.

Make a beat table before production:

| Beat | New information | Exit condition | Possible revision |
|---|---|---|---|
| Folded lamp on a crowded desk | The object is compact | Viewer recognizes its size against a familiar object | Simplify the background before extending duration |
| Hinge opens | Its transformation is the feature | Opening completes and the silhouette reads | Shorten an idle lead-in; preserve the decisive action |
| Lamp illuminates a notebook | The feature has a practical benefit | Light change and usable area are understood | Hold the result instead of adding another camera move |
| Product name and invitation | Identify product and next action | Message can be read at target display size | Reduce copy before compressing the reading interval |

Reserve reading time after type becomes legible. Entrance animation is not automatically usable reading time. Test captions and copy in the intended language and composition; no single reading-speed value fits every audience or scene.

**Firsthand workflow: Walter Murch.** Murch describes choosing edit points during real-time playback and beginning with image alone. Adapt this diagnostically: watch without scrubbing, mark the felt transition, then test nearby frames. A silent pass exposes visual organization; restore sound before judging the final cut. ([ASC interview][murch])

**Firsthand workflow: motion design.** Van Dijk uses editing to explore timing and music quickly, choosing cuts when complex transitions exceed available time. Ordinary Folk considers sound early and composes against an animatic. Test a board edit with provisional sound before detailed animation. ([Van Dijk][sander], [Ordinary Folk][ordinary])

## Plan coverage and continuity

Request coverage that resolves a storytelling or editorial need. Nearly identical AI clips may provide little usable choice.

| Coverage purpose | Capture or generation requirement | Continuity check |
|---|---|---|
| Orient | Show the meaningful relationship between subject, destination, and obstacle | Establish the action axis and geography |
| Show action | Preserve the complete decisive gesture with room to trim | Match action phase, hand, prop, and direction |
| Reveal detail | Isolate the mechanism, clue, or result | Keep scale, identity, lighting, and physical state consistent |
| Show response | Capture a readable reaction or consequence | Match gaze target, emotional state, and timing |
| Connect | Provide a neutral view, cutaway, or motivated change of viewpoint | Reorient clearly when crossing the established axis |

Track eyelines and screen direction. Avoid an unexplained reversal when cutting between angles. Establish intentional orientation changes through visible movement or an orienting shot. Match gaze direction, height, and target location.

Inspect eye trace: where is the viewer looking before and after the cut? Make the new focal point easy to locate or allow time for a deliberate shift. Match action trajectory and momentum in playback; mechanically matching poses can still repeat or skip movement.

## Choose the join

| Join | Narrative purpose | Failure to check |
|---|---|---|
| Cut | Change information or viewpoint directly | Arbitrary angle change, continuity jump, or no new information |
| Match on action | Carry one action across viewpoints | Duplicated contact, missing movement, changed speed or direction |
| Graphic match | Connect shapes or ideas | A visually clever link that suggests the wrong causal relationship |
| J-cut | Let incoming audio begin before its picture | New voice or location becomes confusing without context |
| L-cut | Let outgoing audio continue after the picture changes | Audio implies the wrong speaker or an unintended time relationship |
| Dissolve or fade | Suggest passage, association, or separation | Unreadable overlap, accidental double image, or weakened emphasis |
| Occlusion, whip, or motion transition | Hide or motivate a spatial handoff | Incompatible direction, blur, scale, exposure, or camera momentum |

Adjust audio and picture boundaries independently while retaining synchronization. Place audio edges using the waveform and sentence meaning; avoid accidentally sliding synchronized dialogue. ([Apple split edits][split])

## Protect transition handles

Retain source material around the edit. A centered 12-frame dissolve needs six outgoing frames beyond the cut and six incoming frames before it. Other alignments need different coverage. Count at the actual timeline rate. Trimming clips creates these available source frames. ([Adobe transitions][transitions])

For generated footage, retain a stable lead-in, complete action, and usable tail within verified duration choices. Inspect the clip before assuming handles exist. If missing, shorten or realign the transition, cut directly, or obtain additional approved media. Frozen frames and generated extensions require inspection.

For a seamless join, specify outgoing and incoming subject position, scale, direction, light, occluder, and camera velocity. Matching is a production task; “seamless cinematic transition” does not guarantee it.

## Edit picture and sound together

Keep dialogue, ambience, music, and effects separately adjustable. Let meaning and performance determine thought boundaries. Preserve expressive breaths and reactions. Use room tone for continuity and short fades to prevent audio clicks.

Let music and effects support event hierarchy. A phrase, accent, or silence can organize a sequence; every cut need not hit a beat or receive a whoosh. Mute music to test comprehension, then restore it and check emphasis and intelligibility on ordinary speakers.

Place captions against the final audio timing. A J-cut can require a speaker label before that speaker appears. Do not move captions to the picture cut if that misrepresents when words are heard.

## Keep time and sampling distinct

| Variable | What it changes | Practical consequence |
|---|---|---|
| Capture or generation frame rate | Available temporal samples | It does not itself specify exposure blur or playback speed |
| Timeline and export frame rate | Playback cadence and frame boundaries | Preserve exact rates, including fractional rates; verify conversion |
| Shutter / exposure interval | Motion accumulated inside each captured or rendered frame | Shorter exposure generally gives sharper movement samples |
| Retiming | Mapping from source time to timeline time | Changes action duration and may require interpolation |
| Interpolation | How unavailable output frames are constructed | Inspect synthetic frames, especially around occlusions and cuts |

For physical capture, `exposure_seconds = shutter_angle / (360 * capture_fps)`. Thus 180 degrees at 24 fps gives 1/48 second. ARRI documents this relationship. It does not establish one mandatory “cinematic” shutter angle, and prompt wording cannot prove a generated clip used that exposure. ([ARRI manual][arri])

Conforming 60 captured frames to play at 24 frames per second produces 2.5 seconds from one captured second, or 40% speed. Converting the same source to 24 fps while preserving real-time duration is a different operation. Keep audio synchronization and pitch requirements explicit.

Adobe distinguishes frame sampling, which repeats or removes frames, from optical flow, which estimates intermediate motion. Frame blending mixes adjacent images. Check hands, thin edges, fast pans, reflections, smoke, and newly revealed surfaces after retiming. Never assume optical flow can reconstruct unseen action reliably or safely interpolate across a scene cut. ([Adobe interpolation][interpolation])

For deterministic animation, calculate event timing in seconds and quantize important contacts to the intended frame boundaries. Render subframe motion samples when the renderer supports blur. Increasing export fps cannot repair a poorly staged action or guarantee additional genuine detail.

## Deliver readable and accessible motion

Provide synchronized captions for speech and meaningful non-speech audio, including speaker identification where needed. Keep them clear of faces, demonstrations, product labels, and platform controls. W3C distinguishes captions from dialogue-only subtitles and warns against obscuring relevant visual information. ([W3C captions][captions])

For interactive delivery, honor reduced-motion preferences and provide a way to disable nonessential interaction-driven movement. Replace a large camera journey or parallax effect with an equivalent readable state change. For a linear video, prepare a calmer alternate version or appropriate playback controls when the delivery calls for them; a video file alone does not implement a web preference. Inspect rapid flashes separately. ([W3C motion][motion])

## Review under real constraints

Watch the complete export at normal speed and intended size. Inspect joins, fastest movement, identity, text, captions, audio peaks, and final hold. Verify rate, duration, crop, and synchronization. Proxies help editing responsiveness, but inspect the final render for concealed artifacts.

Under time or budget pressure, preserve essential action and a readable result. Simplify coverage, remove transitions, or hold a clean composition. Avoid repeated generations when a direct cut communicates the beat. Tie revisions to observable failures and describe remaining limitations honestly.

## Sources

- [ASC, Walter Murch: Editing in Real Time][murch]: original editor interview.
- [School of Motion, Sander van Dijk interview][sander] and [Ordinary Folk, Process][ordinary]: firsthand motion workflows.
- [Apple, Create split edits][split]: official audio/video boundary behavior.
- [Adobe, Transitions overview][transitions]: source-frame availability for transitions.
- [ARRI, ALEXA 35 user manual][arri]: sensor rate and shutter equation, HOME screen section.
- [Adobe, Apply time interpolation methods][interpolation]: official sampling, blending, and optical-flow choices.
- [W3C, Captions (Prerecorded)][captions] and [Animation from Interactions][motion]: accessibility guidance and scope.

[murch]: https://theasc.com/post/the-film-book/walter-murch-2-real-time-cuts-image-editing/
[sander]: https://schoolofmotion.com/blog/sander-van-dijk-podcast
[ordinary]: https://www.ordinaryfolk.co/process
[split]: https://support.apple.com/en-ke/guide/final-cut-pro/ver1632d82c/mac
[transitions]: https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/transitions-overview.html
[arri]: https://www.arri.com/resource/blob/284044/2bb86cd6a6d3af1f881acd2a15002f0b/alexa-35-user-manual-data.pdf
[interpolation]: https://helpx.adobe.com/sg/premiere/desktop/edit-projects/change-clip-speed/apply-time-interpolation-methods-to-adjust-clip-speed.html
[captions]: https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html
[motion]: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
