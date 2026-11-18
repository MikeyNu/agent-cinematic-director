# Color and finishing

Checked 18 November 2026. Use for look development, mixed-source grading, shot matching, and delivery. Procedures are practical synthesis; linked definitions come from primary documentation. Creator methods are contextual examples.

## Contents

- [Define the color contract](#define-the-color-contract)
- [Identify inputs, including generated media](#identify-inputs-including-generated-media)
- [Choose where operations live](#choose-where-operations-live)
- [Correct, develop the look, and match](#correct-develop-the-look-and-match)
- [Motivate the palette](#motivate-the-palette)
- [Protect people, products, and gamut](#protect-people-products-and-gamut)
- [Design texture deliberately](#design-texture-deliberately)
- [Check operation interactions](#check-operation-interactions)
- [Finish for the actual delivery](#finish-for-the-actual-delivery)
- [Sources and further reading](#sources-and-further-reading)

## Define the color contract

Before adjusting a frame, record source encoding, working space, viewing transform, output target, and approval reference. Include gamut and transfer function rather than writing only "log" or "709." Record transform versions, legal/full range interpretation, frame size, and any baked look. A LUT needs a documented input and intended output. Its filename is insufficient evidence.

Select a coherent managed workflow, such as Resolve Color Management, ACES, or explicitly configured transforms. Blackmagic supports input, timeline, and output transformations; these are technical decisions separate from creative preferences. Avoid applying the same conversion twice. [BMD]

Choose delivery first: an agreed SDR video specification, web stills, a cinema master, or a specified HDR target. A Rec. 709 SDR project with a matching calibrated viewing condition is one common case, not a default for every screen. ACES output transforms account for the intended display and viewing conditions. [ACES-OUT]

## Identify inputs, including generated media

For camera material, check recording settings and metadata against camera documentation. For scans, graphics, stock, and renders, request the actual supplied encoding. Confirm that a technical transform gives a plausible result before adding a look. A flat appearance does not establish a particular log curve.

Treat AI imagery as an input with provenance to establish:

1. Record generator, model/version, download format, embedded color tags, and any upstream processing.
2. Determine whether the download already includes a display rendering. A prompt naming a camera or film stock is an aesthetic instruction, not evidence of that camera's encoding.
3. If provenance is incomplete, preserve an untouched reference. Choose and document a provisional interpretation supported by the file and platform information, then compare the managed image with that reference.
4. Do not assign a camera-specific input transform merely to make the image look dramatic. Resolve missing metadata through inspection, documentation, or a small controlled comparison.

Moving an already rendered image into a larger working space does not recover clipped highlights, missing chroma, or scene radiometry. Expect limited latitude in baked, compressed sources. Keep the original and record uncertainty rather than claiming that an unknown generation is RAW, log, or HDR. Color-space conversion requires knowledge of both ends of the conversion. [KELLY-SPACE]

## Choose where operations live

Scene-referred processing describes scene light before the final display rendering. Display-referred processing describes an image already prepared for viewing. These are different interpretations, not quality rankings. ACES separates source-to-working transforms, creative adjustments, and the transformation for display; ACEScct is a grading encoding, while ACEScg serves rendering and compositing. [ACES]

Check each effect's expected domain. A scene-linear exposure adjustment, log grading control, display-space overlay, and film-emulation plugin may need different inputs. An existing display render may require a dedicated inverse or display-source handling route to preserve appearance inside a scene-based project. Consult the implementation instead of assuming any generic transform is reversible.

Keep viewing transforms active while judging the result. Use scopes at the point relevant to the question: source diagnosis before the output transform, delivery limits after it. Ensure graphics and titles enter through their intended route and do not receive unintended double contrast or saturation.

## Correct, develop the look, and match

Separate three jobs conceptually, even when a tool combines them:

- **Correction:** resolve unintended exposure, balance, tint, and source inconsistencies.
- **Look development:** establish the project's contrast behavior, palette relationships, saturation, highlight treatment, and texture.
- **Shot matching:** make adjacent shots belong to the same scene while retaining motivated lighting differences.

Choose representative anchors: a face, a wide, a highlight-heavy shot, and a difficult low-light shot. Establish a shared look across these, then balance clips while viewing through it.

Match in context using a split screen or reference still and playback across the cut. Compare subject exposure, black density, highlight behavior, dominant neutrals, skin, and saturated objects. Match the audience's focal point before irrelevant background averages. Different angles may legitimately reveal different light sources.

A correctly photographed chart helps establish a technical reference. It must share the scene's illumination, and its patches must be unobstructed. Cullen Kelly treats chart matching as useful evidence that can be blended or rejected when it conflicts with the intended lighting. [KELLY-CHART]

For AI clips, check the whole duration for exposure pumping, hue changes, evolving materials, and drifting faces. A static grade cannot repair changing identity or geometry. If tracking and restrained keyframes cannot solve the problem cleanly, regenerate or replace the affected shot.

## Motivate the palette

Start with light sources, production design, subject priority, and the scene's dramatic progression. The following are proposed directions to test, not universal color-emotion rules. Cultural context, surrounding scenes, performance, and sound can change their meaning.

| Scenario | Possible motivated direction | What must remain legible |
|---|---|---|
| Intimate kitchen conversation | Warm practical pool against quieter window ambience; restrained separation | Faces, food, and the believable source of warmth |
| Clinical product reveal | Controlled neutrals and selective brand accents; precise material contrast | Product color, label, finish, and highlight shape |
| Night exterior under mixed fixtures | Distinct local light families with controlled saturation | Spatial geography, facial identity, and useful shadow detail |
| Sunlit travel sequence | Warm illuminated surfaces, natural sky separation, consistent exposure | Location character and differences between shots |
| Suspense in an ordinary room | Reduced competing colors and selective density around the subject | The clue or threat the viewer must notice |
| Archival or remembered event | A defined period reference for contrast, palette, and texture | Narrative connection and separation from present-day scenes |

Translate references into observable attributes: soft or steep toe, highlight hue, chroma distribution, density, edge softness, and grain scale. Agree on which attributes matter. Teal shadows, orange faces, faded blacks, letterboxing, and grain are optional choices. None guarantees cinematic storytelling. Kelly's analytical viewing approach separates the combined effect of a scene from the particular production and post choices that create it. [KELLY-STYLE]

## Protect people, products, and gamut

Judge skin in its actual illumination. The vectorscope skin indicator is a diagnostic reference, not a command to push every person to one hue, saturation, or brightness. Colored lighting can appropriately move skin away from neutral. Prefer broad corrections when they solve the problem; use careful secondaries when global adjustments damage other colors. [KELLY-SKIN]

For products, agree on approved color references and the viewing condition. Preserve material differences, packaging, and typography. Check masks through motion, reflections, hair, and occlusion. Generated text or geometry needs repair at source or in compositing; a color key cannot correct its shape.

Use waveform for tonal placement, RGB parade for channel imbalance and clipping, vectorscope for hue/chroma, and a gamut-aware view for output boundaries. Scopes supplement a trustworthy display. Inspect saturated lights and brand reds for clipped channels. [BMD]

## Design texture deliberately

Noise is an acquisition or processing characteristic; added grain is a chosen texture model. They can coexist. Diagnose fixed patterns, compression blocks, temporal shimmer, and chroma noise before choosing cleanup. Use enough denoising to control the defect while preserving faces, fabrics, and motion.

Specify grain by apparent size at final resolution, strength, tonal distribution, color behavior, and temporal behavior. Judge playback and normal viewing distance, then inspect fine detail. Cullen Kelly demonstrates grain as part of a coherent look and proposes slight softening before it; treat his sequence as one workflow to test rather than a mandatory node order. [KELLY-GRAIN]

Distinguish grain from halation and bloom. Halation emulation concerns highlight-edge light spread associated with film; bloom softens or spreads bright image regions. Both can reduce local contrast and obscure details when excessive. Evaluate bright windows, jewelry, lettering, and faces rather than judging only a flattering sample. [KELLY-FX]

A conventional 3D LUT maps individual RGB values. Spatial effects such as halation require neighborhood information and cannot be faithfully stored inside that LUT alone. Yedlin separates color rendition, grain, halation, and gate movement in his own display-preparation work. [YEDLIN]

## Check operation interactions

Organize the graph so changes remain explainable. There is no single correct node order across every plugin and source.

- Denoising after added grain may erase the intended texture.
- Sharpening after grain can exaggerate it; resizing changes its apparent scale.
- Contrast and output rendering can change grain visibility and highlight spread.
- Halation before versus after strong tone mapping can select different highlights.
- A shared look is useful for consistency, but mixed-resolution sources may need different texture treatment.

Verify the effect's color-space requirements, test placement on representative shots, and save the selected configuration. Compare at matched playback size and output conditions. Change one interacting choice at a time when diagnosing a defect.

## Finish for the actual delivery

Export a short representative sequence through the real delivery settings. Review the encoded file, not only the grading viewer. Grain is difficult to compress because its randomness defeats prediction, as AOMedia's film-grain work explains. A clean master can become smeared, blocky, or unstable after distribution. [AOM]

Check tags and range, highlight clipping, gradients, dark detail, grain survival, edge halos, and scene-to-scene consistency. Include motion and the hardest cut. If authorized and needed, inspect a platform transcode too. Reduce or redesign texture when it competes with detail at the available bitrate. Increasing output dimensions alone does not restore missing source detail.

Keep a high-quality master and the delivery version. Record settings, transform/plugin versions, references, and limitations. Approve individual frames and continuous playback. Finish when the sequence serves the story and survives delivery; additional texture is not inherently an improvement.

## Sources and further reading

- **[ACES]** [Academy: ACES system overview](https://docs.acescentral.com/background/overview/), updated 10 September 2025.
- **[ACES-OUT]** [Academy: Output transforms](https://docs.acescentral.com/system-components/output-transforms/), updated 10 September 2025.
- **[BMD]** [Blackmagic Design: Color tools and scopes](https://www.blackmagicdesign.com/products/davinciresolve/color). For version-specific procedures, use the [official training/manual portal](https://www.blackmagicdesign.com/products/davinciresolve/training).
- **[KELLY-SPACE]** [Cullen Kelly: Color spaces](https://blog.frame.io/2020/02/03/color-spaces-101/), 3 February 2020, updated 18 August 2024.
- **[KELLY-CHART]** [Cullen Kelly: Using color charts](https://blog.frame.io/2023/11/06/how-to-use-a-color-chart-in-davinci-resolve/), 6 November 2023.
- **[KELLY-STYLE]** [Cullen Kelly: Developing a style](https://blog.frame.io/2021/01/11/how-to-develop-your-own-style-as-a-colorist/), 11 January 2021.
- **[KELLY-SKIN]** [Cullen Kelly: Skin tones](https://blog.frame.io/2020/10/05/skin-tones-in-davinci-resolve/), 5 October 2020.
- **[KELLY-GRAIN]** [Cullen Kelly: Film grain](https://blog.frame.io/2023/08/14/how-a-pro-colorist-uses-film-grain/), 14 August 2023.
- **[KELLY-FX]** [Cullen Kelly: Film Look Creator](https://blog.frame.io/2024/08/15/what-is-resolves-new-film-look-creator-plugin/), 15 August 2024. Resolve 19 examples, not a current control inventory.
- **[YEDLIN]** [Steve Yedlin: Display Prep FAQ](https://www.yedlin.net/NerdyFilmTechStuff/DispPrepDemoFAQ/), 14 July 2019.
- **[AOM]** [Alliance for Open Media: Film grain synthesis technology](https://aomedia.org/docs/CWG-C051o_TR_AOMedia_film_grain_synthesis_technology_v2.pdf). Technical rationale for grain and compression, not a promise of platform behavior.
