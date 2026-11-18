# Animation and motion

Research snapshot: 18 November 2026. Treat the applications and examples below as craft synthesis. Verify current software controls before execution.

## Contents

- [Define the motion](#define-the-motion)
- [Apply all twelve principles](#apply-all-twelve-principles)
- [Build motion in passes](#build-motion-in-passes)
- [Make camera shake coherent](#make-camera-shake-coherent)
- [Separate executable controls from prompt intent](#separate-executable-controls-from-prompt-intent)
- [Inspect the result](#inspect-the-result)
- [Sources](#sources)

## Define the motion

Give each shot one primary action and an observable result. Specify its cause, reference space, path, acceleration, stopping behavior, and revealed information. “Cinematic, dynamic, smooth” leaves these decisions unresolved.

Use a motion contract:

| Field | Original example |
|---|---|
| Story change | Reveal that the portable lamp folds flat |
| Primary action | Hinge closes while the camera stays still |
| Preparation | Brief pause with the hinge clearly visible |
| Consequence | Soft base compresses slightly; rigid housing retains shape |
| Completion | Closed lamp settles before the size comparison appears |
| Readability | Product label and comparison remain stable during the reading interval |

Distinguish **timing**, the duration and placement of events, from **spacing**, the distribution of positions between them. Inspect both path and speed graph: a smooth path can still have an unwanted speed jump. ([Adobe speed][speed])

## Apply all twelve principles

Use the principles diagnostically, not as requirements for every shot. Disney describes physical and performance foundations; Gene Deitch lists the traditional set and allows greater freedom in graphics. The camera and type applications below are adaptations. ([Disney][disney], [Deitch][deitch])

| Principle | Operational meaning | Camera and scene application | Motion graphics and type application |
|---|---|---|---|
| **1. Squash and stretch** | Express flexibility under force while preserving plausible volume. | Deform a soft prop where contact occurs. Keep rigid architecture and camera geometry stable; communicate a camera impact through movement. | Deform a supporting shape or container. Preserve brand glyphs, counters, and readable proportions unless deformation is an approved design choice. |
| **2. Anticipation** | Prepare attention and energy for the main action. | Let a gaze, sound, framing pause, or restrained move establish what will happen. A reverse move is optional. | Signal the next reveal through hierarchy or a small preparation. Avoid delaying every interaction with a decorative windup. |
| **3. Staging** | Make the intended idea unambiguous. | Choose viewpoint, light, blocking, depth, and background motion around the subject's action. | Reveal information in priority order. Let the sentence being read dominate competing movement. |
| **4. Straight ahead and pose to pose** | Choose sequential discovery, planned key states, or a combination. | Block camera and subject endpoints first when continuity matters; explore organic movement between them. | Plan readable layouts and transition endpoints; develop particles or drawn flourishes sequentially. These are planning methods, not easing modes. |
| **5. Follow through and overlapping action** | Let connected parts continue and respond on different schedules. | Offset a coat, suspended cable, or supported rig's settling according to inertia. Do not make every object stop together. | Let an accent trail the main shape or settle later. Preserve the reading hold; delayed letters must not keep the message unresolved. |
| **6. Slow in and slow out** | Shape acceleration through spacing near starts and stops. | Design the rig's acceleration and braking. Keep a sustained tracking segment steady if that serves the shot. | Ease an arrival when appropriate; preserve a sharp contact or a constant-speed crawl. Avoid applying one symmetric ease to every property. |
| **7. Arcs** | Give movement a coherent spatial trajectory. | Use plausible pivots and orbits. Inspect subject framing throughout the path; mechanical slides may properly remain straight. | Curve a gesture or ornament when expressive. Keep a word's baseline and orientation deliberate while it follows a path. |
| **8. Secondary action** | Add a subordinate action that supports the main idea. | A glance toward the newly revealed exit can reinforce the reveal. Background activity must not become a second focal event. | Add a restrained underline or icon response to reinforce meaning. Distinguish this supporting action from inertial follow through. |
| **9. Timing** | Use duration to communicate force, scale, intention, and thought. | Give a heavy door and a light latch different temporal behavior; allow recognition after a reveal. | Separate entrance time from reading time. Relate stagger length to comprehension and tone rather than a favorite preset. |
| **10. Exaggeration** | Clarify the essential quality of an action. | Strengthen one reaction, pose, or reveal relative to the scene's baseline. Keep its cause legible. | Emphasize the decisive number or transformation. Increasing every scale, bounce, and blur weakens hierarchy. |
| **11. Solid drawing / form** | Maintain convincing construction, balance, volume, and perspective. | Preserve contact, occlusion, support, and coherent depth as objects or cameras turn. Check silhouettes and intersections. | Keep extrusion, lighting, anchor points, and projected letterforms consistent. A three-dimensional title still needs readable faces. |
| **12. Appeal** | Create clear, engaging, intentional design and performance. | Choose a compelling viewpoint and readable action with personality. Appeal can be severe, strange, or threatening. | Use distinctive rhythm, proportion, hierarchy, and restraint that fit the brand. Appeal does not require cuteness or constant movement. |

For approximately constant-volume three-dimensional deformation, keep the product of scale factors near one. Preserving area in a flat graphic is a visual analogy, not physical volume. Judge material and silhouette. ([Adobe principles][principles])

## Build motion in passes

1. **Block meaning.** Establish key poses, camera framings, readable layouts, contacts, and screen direction.
2. **Block time.** Cut an animatic with provisional audio. Test comprehension and the final hold.
3. **Shape movement.** Refine paths, acceleration, and weight. Evaluate whole phrases before individual curves.
4. **Add support.** Introduce justified overlap, secondary action, and exaggeration. Remove competing activity.
5. **Finish sampling.** Set blur after motion works. Check the rendered delivery rate, crop, and smallest display.

**Firsthand workflow: Ordinary Folk.** The studio moves from message and script to design and storyboards, then animation. Sound is considered throughout, with composers receiving an animatic. Adapt this by establishing story and editable timing before detailed motion. ([Studio process][ordinary])

**Firsthand workflow: Sander van Dijk.** Van Dijk evaluates possible connections between planned frames and their meaning, then uses editing to explore timing and music quickly. Adapt this by testing two animatic alternatives before building a complex morph. ([Interview][sander])

## Make camera shake coherent

Identify the operator, support, and force. Breathing, vehicle vibration, and an impact require different motion. Barry Ackroyd describes human viewpoints and responsive operating that reveals the story. Ask what motivates this camera's movement. ([ASC interview][ackroyd])

| Component | Construction and inspection |
|---|---|
| Base move | Establish the deliberate tracking, pan, or hold before adding disturbance. |
| Operator drift | Use restrained, continuous corrections with a recognizable target. Avoid independent random offsets on every frame. |
| Impact | Start a disturbance at its visible or audible cause; choose a dominant axis and a finite decay. |
| Horizon | Inspect roll separately. Keep it restrained unless instability is the point of the shot. |
| Parallax | Move an actual camera through depth when depth change matters. A whole-frame two-dimensional transform cannot reveal hidden surfaces. |
| Framing | Reserve overscan and inspect every edge. Repeated corrective cropping can make apparent scale pump. |

For a small deterministic perturbation, try `delta(t) = A * exp(-lambda * tau) * sin(2*pi*f*tau)` for `tau = t - impact_time >= 0`, and zero beforehand. This illustrative model requires coordinated axis weights, frequency, and decay. Use scene units for translation and angular units for rotation; do not add arbitrary values to a quaternion.

Evaluate shake with intended exposure and blur. Shorter exposure gives crisper motion samples; blur cannot correct a discontinuous path. Rolling shutter records image rows at different times, potentially causing skew. Repair can preserve intentional camera movement. Do not add this distortion automatically for realism. ([Adobe blur][blur], [Adobe rolling shutter][rolling])

## Separate executable controls from prompt intent

| Deterministic scene or compositor | AI video direction, including Higgsfield |
|---|---|
| Set exact transforms, keyframe times, curves, seeds, and layer relationships supported by the actual tool. | Describe observable movement, subject continuity, cause, restraint, and desired beginning/end states. |
| Add a timed impulse to an existing stable camera. | Request “one brief downward jolt at the impact, then a controlled recovery,” and inspect whether it occurs. |
| Preserve a supplied wordmark as a separate composited layer. | Request a clean plate and add exact typography afterward when accuracy matters. |

Treat prompt timing as intent until verified. Do not invent Higgsfield amplitude, easing, shutter, or seed fields. Discover current model controls. If a precise beat remains unreliable, simplify the shot or adjust timing in editing.

## Inspect the result

Play at normal speed, then inspect contact, fastest movement, reversal, landing, and final hold. Check comprehension silently and rhythm with sound restored. Verify identity, form, type, horizon, and crop. Use the pacing reference for captions and accessible alternatives.

## Sources

- [Disney Animation, Animation process][disney]: studio foundations.
- [Gene Deitch, The Mighty Principles of Animation][deitch]: creator-authored principles.
- [Adobe, Understanding the 12 principles of animation][principles]: definitions and volume.
- [Adobe, Speed][speed]: spacing and graphs.
- [Ordinary Folk, Process][ordinary]: firsthand workflow.
- [School of Motion, Sander van Dijk interview][sander]: firsthand planning.
- [ASC, A House of Dynamite][ackroyd]: original Barry Ackroyd interview.
- [Adobe, Assorted animation tools][blur] and [Rolling Shutter Repair][rolling]: official technical distinctions.

[disney]: https://www.disneyanimation.com/process/animation/
[deitch]: https://www.awn.com/animationworld/mighty-principles-animation
[principles]: https://www.adobe.com/creativecloud/animation/discover/principles-of-animation.html
[speed]: https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/speed-between-keyframes/speed.html
[ordinary]: https://www.ordinaryfolk.co/process
[sander]: https://schoolofmotion.com/blog/sander-van-dijk-podcast
[ackroyd]: https://theasc.com/article/a-house-of-dynamite-cinematography/
[blur]: https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/assorted-animation-tools/assorted-animation-tools.html
[rolling]: https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/rolling-shutter-repair.html
