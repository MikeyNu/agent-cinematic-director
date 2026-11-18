# Camera, lenses, focus, and coverage

Research snapshot: 18 November 2026. Turn story beats into shots with these starting points, then verify the image.

## Contents

- [Define the camera contract](#define-the-camera-contract)
- [Choose size and angle](#choose-size-and-angle)
- [Separate viewpoint from focal length](#separate-viewpoint-from-focal-length)
- [Choose lens construction and character](#choose-lens-construction-and-character)
- [Motivate movement and lens changes](#motivate-movement-and-lens-changes)
- [Design depth of field and focus](#design-depth-of-field-and-focus)
- [Build useful coverage](#build-useful-coverage)
- [Apply a firsthand workflow](#apply-a-firsthand-workflow)
- [Example and verification](#example-and-verification)
- [Sources](#sources)

## Define the camera contract

Write what the viewer must discover, feel, or anticipate, and when. Specify subject, blocking, start/end framing, duration, viewpoint, field of view, movement, and focus.

| Execution | Controls to specify | Evidence to verify |
|---|---|---|
| Physical camera | Active sensor area, lens, camera position/height, subject distance, aperture, focus marks, support and route | Rehearsal and recorded take |
| 3D camera | Filmback/sensor fit, projection, focal length, transform, focus target, aperture, shutter, world scale | Rendered framing, parallax, occlusion, focus and motion |
| Generative image/video | Visible framing, spatial relationships, one principal camera move, focus destination, timed action | Actual generated frames and playback |

In AI prompts, millimeters are descriptive cues unless documented optical controls exist. A “50 mm” label does not demonstrate accurate optics. Pair it with observable intent: “medium close-up from across the table, restrained background expansion.”

## Choose size and angle

Name the size relative to the subject. “Wide” describes coverage; it does not necessarily mean a wide-angle lens.

| Size | Choose it when | Avoid or verify |
|---|---|---|
| Extreme wide / establishing | Geography, scale, isolation, destination matters | The important person or landmark survives delivery resolution |
| Wide / full | Body language, choreography, spatial relationships carry the beat | Feet, hands, entrances and exits remain readable |
| Medium / waist-up | Gesture and expression need comparable weight | Cropping does not remove the decisive action |
| Medium close-up | A face and some physical context carry dialogue | Leave room for the actual performance |
| Close-up | Recognition, hesitation, or reaction changes the scene | The expression earns the emphasis |
| Extreme close-up / insert | A small detail supplies necessary evidence | Establish ownership and geography elsewhere |
| Two-shot / over-shoulder / POV | Relationship, conversational alignment, or subjective access matters | Eyelines and whose perspective is represented are clear |

Try eye level for an unforced relationship, low/high viewpoints for spatial emphasis, overhead for geography, and canting for instability. Test in context: low/high angles do not automatically convey power/weakness. Distinguish height from tilt: a low, level camera differs from an upward-looking camera at head height.

## Separate viewpoint from focal length

**Set camera position for perspective; set focal length for framing.** At a fixed viewpoint, changing focal length changes the captured angle, not foreground/background perspective. A crop of a wider image can match a longer-lens image's perspective. Moving backward and using a longer lens to preserve subject size changes relative distances, producing the familiar compressed arrangement. Lens distortion is a separate optical property. [S1]

Record active sensor dimensions and delivery crop. A 50 mm lens remains 50 mm on different sensors; captured angle changes. Match horizontal framing approximately with `f2 = f1 × active_width2 / active_width1`. Super 35 has no universal crop factor. [S2]

The following examples assume a **rectilinear spherical lens and 36 mm active image width**. Approximate horizontal angle is `2 × atan(width / (2 × focal_length))`, ignoring close-focus effects. State another format explicitly.

| Starting lens | Approximate horizontal angle | Useful experiment |
|---|---|---|
| 24 mm | 74° | Include environment; approach only if exaggerated near/far relationships help |
| 35 mm | 54° | Connect a character to a room while retaining workable proximity |
| 50 mm | 40° | Frame a person with selective context from a considered distance |
| 85 mm | 24° | Isolate details from farther away; verify room, stability and eyelines |

For equal framing, 50 mm on a 36 mm active width corresponds approximately to 33 mm on a 24 mm active width. These are framing equivalents, not blanket equivalence of noise, blur, distortion or lens character. Test faces, backgrounds, flare and near-focus behavior with the actual lens or render.

## Choose lens construction and character

Treat these as overlapping properties: an anamorphic lens may be a prime or a zoom. Choose the actual optical behavior and production constraints, not a prestige label.

| Choice | Useful when | Check before committing |
| --- | --- | --- |
| Prime, with fixed focal length | Blocking and a deliberate viewpoint/framing relationship can be established | Actual speed, size, minimum focus, matching between lenses and time for swaps; primes are not automatically superior |
| Zoom | Reframing speed or an intentional in-shot focal-length change serves the production | Focus retention during zoom, exposure behavior, breathing, image quality across the range and rig balance |
| Rectilinear spherical | Clean geometry, flexible crops, product accuracy or restrained optical character matters | Real distortion, flare, breathing and close-focus behavior; spherical does not mean characterless |
| Anamorphic | Its spatial rendering, focus behavior or characteristic highlights serve the scene | Squeeze factor, active sensor coverage, correct monitoring/de-squeeze, crop, faces near edges, focus and compositing needs |
| Macro / close-focus setup | A small mechanism, material or clue must carry the frame | Working distance, magnification, light access, focus tolerance and subject movement |

Anamorphic capture squeezes one image axis and requires the corresponding de-squeeze. A wide crop or added black bars does not reproduce that optical process. Oval out-of-focus highlights and horizontal flares are familiar characteristics, but design, orientation and lighting affect them; not every anamorphic lens produces the same signature. Test the actual lens, and do not infer anamorphic capture from those cues alone. [S7, S8]

For vintage character, compare flare, contrast, sharpness falloff, distortion and color on the actual subject. Keep required geometry and legibility intact. In AI workflows these names remain appearance cues unless a verified camera system exposes the relevant controls. In deterministic compositing, preserve a clean base and match lens distortion when integrating artwork. Canon's cinema-lens explanations illustrate why breathing suppression and mechanical behavior must be checked by lens family. [S4]

## Motivate movement and lens changes

Write a trigger and a destination for each move. If neither changes the information or relationship, test a locked frame.

| Technique | Motivation and observable result | Avoid / verify |
|---|---|---|
| Locked camera | Let blocking, duration or offscreen events create pressure | Accidental drift; an unreadable action |
| Pan / tilt | Follow attention or reveal adjacent information from one position | Confusing rotation with translation; abrupt endpoints |
| Dolly / push / pull | Approach a realization, retreat from intimacy, reveal context | A digital scale-up cannot reproduce translational parallax |
| Truck / lateral track | Follow action or expose foreground/background layers | Occluders hiding the essential beat |
| Crane / boom | Change height to discover scale or join levels | Unmotivated altitude changes and impossible rig paths |
| Orbit | Reveal changing relationships around a subject | Crossing eyelines unintentionally; repetitive scenery |
| Handheld / stabilized follow | Express an observer's physical relation to action | Random shake or excessive floating without purpose |
| Optical zoom | Change framing from a fixed position, possibly suggesting examination | Calling it a dolly; untested focus or exposure shifts |

A cut permits a purposeful lens and viewpoint change between shots. A continuous zoom changes focal length during a shot. A dolly zoom combines camera translation with opposing zoom to hold subject scale while changing spatial relationships. Plan that as a conspicuous effect with a narrative reason. In generative video, specify its visible result and check for warping rather than assuming the term guarantees execution.

## Design depth of field and focus

Choose what must be readable simultaneously. Use deeper focus for relationships across depth, choreography, evidence, or viewer exploration. Use selective focus to prioritize a person or withhold information. Shallow depth of field is not a universal cinematic requirement.

At otherwise fixed settings, opening the aperture, increasing focal length, or focusing closer generally reduces depth of field. Comparisons at matched subject size need additional care because camera distance also changes. Acceptable sharpness depends on viewing conditions; focus calculators are estimates, and bokeh character is distinct from the measured depth range. [S3]

At matched viewpoint, framing, f-number and output viewing conditions, a larger format generally gives shallower depth of field through its longer focal length. State these conditions when comparing formats. [S2]

Specify focus distances and aperture. Distinguish geometric f-number from transmission-adjusted exposure T-stop. [S6] Check software semantics, compensate exposure for iris changes, and verify diffraction and available light before stopping down further.

Plan a focus pull as a miniature reveal:

1. Establish an identifiable starting subject.
2. Cue the shift through gaze, motion, dialogue, or a new event.
3. Name the destination and the desired arrival time.
4. Hold long enough for the new information to register.

Measure and rehearse physical focus marks. Check breathing, the framing change that can accompany refocusing, across the actual distance range. [S4] For AI, describe “focus leaves the foreground hand and settles on the doorway figure”; inspect whether both endpoints, timing, and identity remain coherent.

## Build useful coverage

Map editorial beats to shots. Start with a geographic master, relationship shot, necessary singles/reactions, and evidence inserts. Remove redundant coverage when a sustained composition carries the scene.

Draw the action axis; record screen direction, camera side/height, eyelines, props and movement phase. An axis crossing can work when a visible move, neutral view or fresh geography reorients viewers. Avoid framings so similar that their cut feels accidental. Capture usable lead-in and tail time.

## Apply a firsthand workflow

For *1917*, Roger Deakins describes rehearsing action to determine set dimensions, testing camera systems, and finding positions that could reveal reactions within the choreography. Playback helped match actor position and camera speed across joins. Transfer the method: rehearse the required information, design the route and support around it, then check transitions. Do not copy the production's lens or rig list as a universal recipe. [S5]

## Example and verification

**Beat: a courier recognizes someone at the door.** Start with a 35 mm medium-wide, using the format assumption above, establishing courier, parcel and door. Hold during the knock. Cut to a 50 mm medium close-up for recognition, matching eyeline. Insert the parcel's name only if essential. Alternatively, retain the first composition and pull focus from parcel to doorway as the visitor appears. Choose the clearest timing.

Review start, midpoint, end and full-speed playback. Check framing, actual parallax, stable proportions, focus arrival, motion blur, screen direction and transition handles. Test at delivery size. Select frame rate, shutter, aspect ratio and lens type for the project: 24 fps, anamorphic optics and black bars are not mandatory ingredients of cinema.

## Sources

- **S1:** American Cinematographer, [Understanding Lens Distortion](https://theasc.com/article/understanding-lens-distortion/). Demonstrations separating viewpoint and optical distortion.
- **S2:** ARRI, [ALEXA LF FAQ](https://www.arri.com/en/learn/camera-systems/frequently-asked-questions/alexa-lf-faq). Focal length, active area and angle of view.
- **S3:** ZEISS, [Depth of Field and Bokeh](https://lenspire.zeiss.com/photo/app/uploads/2022/02/technical-article-depth-of-field-and-bokeh.pdf). Geometric models, viewing assumptions and lens behavior.
- **S4:** Canon, [The World of Cinema Lenses](https://files.canon-europe.com/files/webcontent/rf-lens-world/cinemalens/index.html). Focus breathing and lens controls.
- **S5:** Rachael Bosley's firsthand Roger Deakins interview, [Lives Under Siege: The Goldfinch and 1917](https://theasc.com/article/lives-under-siege-the-goldfinch-and-1917/).
- **S6:** Sony, [What is a T-stop?](https://www.sony.com/electronics/support/articles/00347434). Transmission-adjusted lens exposure.
- **S7:** Cooke Optics, [An introduction to anamorphic lenses](https://cookeoptics.com/news-and-events/an-introduction-to-anamorphic-lenses/). Lens construction, characteristic rendering and design-dependent behavior.
- **S8:** ARRI, [Anamorphic de-squeeze white paper](https://www.arri.com/resource/blob/178026/228c1a0523ed25947174567833cd8fb4/anamorphic-de-squeeze-white-paper-data.pdf). Optical squeeze and correct image geometry in monitoring and postproduction.
