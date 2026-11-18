# Composition, visual attention, and lighting

Research snapshot: 18 November 2026. Build readable images with composition and light; verify them over time at delivery size.

## Contents

- [Assign attention before decoration](#assign-attention-before-decoration)
- [Choose a compositional structure](#choose-a-compositional-structure)
- [Use Fibonacci and the golden ratio carefully](#use-fibonacci-and-the-golden-ratio-carefully)
- [Design light from the scene](#design-light-from-the-scene)
- [Control exposure, color and continuity](#control-exposure-color-and-continuity)
- [Apply firsthand workflows](#apply-firsthand-workflows)
- [Translate into physical, 3D and AI controls](#translate-into-physical-3d-and-ai-controls)
- [Example and verification](#example-and-verification)
- [Sources](#sources)

## Assign attention before decoration

For each beat, write “look first at X, then notice Y, because Z.” Identify what should remain uncertain. Give the desired target a readable combination of position, scale, contrast, focus, motion, sound or gaze. Avoid making every element equally prominent.

Plan attention through time. A face can remain stationary while a glance, moving hand, sound or changing light transfers attention. Tim J. Smith's attentional account of continuity identifies such cues and the viewer's expectations as important to transitions between shots. Treat that as a reason to review the sequence, not just attractive isolated frames. [S1]

Map attention at the start, change point and end. Does the incoming shot provide the information anticipated by the outgoing shot? Deliberate searching can create suspense; accidental searching obscures the beat. Test these hypotheses with viewers rather than claiming to predict everyone's gaze.

## Choose a compositional structure

| Structure | What / when / why | Avoid / verify |
|---|---|---|
| Center and symmetry | Concentrate attention, emphasize architecture, ritual or confrontation | Symmetry that disguises an important asymmetry in the story |
| Thirds or off-center balance | Distribute subject and context; leave meaningful look room | Moving every face to a grid intersection mechanically |
| Negative space | Reserve room for a threat, absence, destination or title | Empty area without readable purpose; text colliding with movement |
| Foreground, middle, background | Establish relationships, concealment, distance and parallax | Foreground clutter masking an expression or action |
| Leading lines and diagonals | Connect subject to route, barrier or destination | Strong lines directing attention outside the desired area |
| Frame within frame | Suggest enclosure, observation or separated worlds | Tangencies, poles or door edges cutting through faces |
| Repetition with a break | Make an anomaly meaningful in an ordered environment | So many exceptions that none can be discovered |

Choose headroom, look room, horizon height and cropped limbs deliberately. Preserve meaningful gestures. Check moving overlaps and silhouettes. Set the horizon according to whether land, water, sky or architecture carries the scene; a centered horizon can work.

Choose aspect ratio for staging and distribution. Test required crops early: a wide master's relationships can fail in portrait delivery. Recompose or create another version when necessary.

## Use Fibonacci and the golden ratio carefully

The golden ratio is `φ = (1 + √5) / 2 ≈ 1.618`; golden divisions occur near 0.382 and 0.618 of a frame dimension. Successive Fibonacci-number ratios approach φ. Quarter-circles in Fibonacci squares approximate a spiral, not an exact golden logarithmic spiral.

Use these as optional scaffolds for distributing visual mass or exploring a path of attention. They do not establish a scientific guarantee of beauty or storytelling quality. Rectangle-preference experiments have found that instructions and context change preferred proportions, so do not generalize a numerical preference into a law for complex moving scenes. [S2]

Apply a small comparison:

1. Make a composition driven solely by the story relationship.
2. Try a thirds grid, golden divisions, or a centered alternative.
3. Compare the actual subject/background relationships with overlays hidden.
4. Keep the version that communicates the intended beat and survives motion.

Try a waiting person at `x = 0.382`, leaving space toward a door on the right. Shift them when the eyeline, architecture or incoming actor requires it. Avoid forcing every element onto intersections. A spiral camera path must reveal useful information and produce coherent motion; fitting a spiral to one frame is insufficient.

## Design light from the scene

Identify time, place, weather, practical sources and emotional change. Decide key motivation, required shadow detail and background separation. Enhance or recreate sources offscreen when useful, matching their apparent direction and behavior.

| Control | Use it to | Avoid / verify |
|---|---|---|
| Direction and height | Shape faces, reveal texture, imply a window or practical | Eyeless faces or implausible shadows when expression matters |
| Apparent source size | Choose soft transitions or distinct shadows | Assuming a dimmer source becomes softer |
| Key and fill balance | Set how much shadow information remains | Adding fill until all modeling disappears |
| Negative fill | Reduce unwanted ambient bounce and deepen a side | Crushing necessary detail or restricting actor movement |
| Background illumination | Separate planes and establish the room | Bright patches stealing attention without narrative purpose |
| Edge / backlight | Separate a silhouette when needed | Automatic halos on every person |
| Practical fixtures | Establish source motivation and points of interest | Clipped bulbs dominating a face or prop |
| Flags, grids and bounce | Shape spill and redirect available light | Treating every problem as a need for another fixture |

Softness depends on the light's apparent size from the subject: enlarge the emitting/bouncing area or bring it closer to soften shadows. Brightness and softness are different controls. Diffusion works through the area actually illuminated; a tiny patch of diffusion does not become a huge source. ARRI's handbook distinguishes shadow quality, source size and intensity and presents both hard and soft light as choices. [S3]

Test light with the blocking. A close source may change brightness rapidly as someone moves; a large distant source can provide more consistent coverage over a route. Physical rigs and 3D light models have constraints. Check actual output, falloff and shadows instead of assuming every fixture or shader follows an identical ideal model.

## Control exposure, color and continuity

Set a viewing transform before judging the look. Use calibrated monitoring where available, plus waveform, false color or other exposure tools appropriate to the camera and output. Protect details that must survive the grade and delivery. Avoid universal numerical skin-exposure targets independent of complexion, scene intent, encoding and display transform.

Record exposure, white balance, source directions, practical states and changes over time. If describing a lighting ratio, define what is measured: key-to-fill source contribution differs from the total illuminated-side-to-shadow-side ratio. Never treat “4:1” as a complete lighting instruction.

Use color contrast when it reinforces the scene; warm/cool opposition and teal/orange palettes are optional. Kelvin settings, spectrum, materials and white balance interact. A temperature number alone cannot determine mood. Check faces, costume and design together, preserving meaningful scene differences.

Maintain believable world source direction across coverage. Check changes in apparent time, shadow depth and practical brightness; motivate them through action, weather or subjective transitions. Deep shadows, haze and high contrast do not independently make a shot cinematic.

## Apply firsthand workflows

**Stephen H. Burum's lighting workshop:** establish time of day and shape the set, rough in actor areas, rehearse, refine with stand-ins, then adjust after seeing actual performance, skin and costumes. Adapt this sequence to the budget: establish the environment, test blocking, refine the important faces, and reassess the recorded result. His categories of shadow, separation and fill are a useful diagnostic checklist. [S4]

**David Mullen's composition example:** when photographing a character afraid to enter a pool, he describes favoring more water in frame over attractive clouds because water carried the dramatic point. Apply that test to competing compositional attractions: increase the space occupied by what the scene is about. [S5]

## Translate into physical, 3D and AI controls

| Medium | Specify | Check |
|---|---|---|
| Physical | Source position, size, diffusion/bounce, intensity, color, flags, camera settings and blocking | Shadows, spill, exposure, reflections and route consistency |
| 3D | Light type and dimensions, units, transforms, materials, environment, exposure and color management | Rendered source motivation, shadow scale and geometry |
| AI | Observable light direction, hardness, shadow visibility, subject/background separation and attention target | Whether the generated image actually exhibits those relationships |

For AI, specify “broad window light from camera left, readable shadow-side eye, darker wall behind the face.” Exact lux or ratio promises need supported controls. Use references/masks when available; check light and shadow consistency. Treat prompted metadata as intent and verify pixels.

## Example and verification

**Beat: a worker realizes the room is empty.** Start with a doorway foreground and the worker left of center. Let the unoccupied desk occupy meaningful negative space. Use broad side light to reveal the worker while the desk remains legible. Hold their glance toward the desk, then permit a small lateral move to reveal the untouched cup. Avoid a glowing background sign that competes with that discovery.

Check thumbnail hierarchy, grayscale value separation and full-size overlaps as diagnostics. Watch at delivery speed and inspect required crops. Ask a fresh viewer what they noticed and when. Change one competing feature at a time; keep the version communicating the beat most clearly.

## Sources

- **S1:** Tim J. Smith, [The Attentional Theory of Cinematic Continuity](https://doi.org/10.3167/proj.2012.060102); [accessible author manuscript](https://files.core.ac.uk/download/pdf/141218146.pdf).
- **S2:** P. A. Russell, [The aesthetics of rectangle proportion: effects of judgment scale and context](https://pubmed.ncbi.nlm.nih.gov/10742842/), original experiments, 2000. Limited to the tested tasks, not a direct test of cinematic composition.
- **S3:** ARRI, [Lighting Handbook](https://www.arri.com/resource/blob/83996/409091c612f371b0c68b41d9dcb636db/arri-lighting-handbook-english-data.pdf).
- **S4:** American Cinematographer, [Lighting a Set with Stephen H. Burum, ASC](https://theasc.com/article/lighting-a-set/), firsthand workshop and commentary.
- **S5:** David Mullen, ASC, [Reply on compositional guidelines](https://www.rogerdeakins.com/forums/reply/221435/), firsthand practitioner example.
