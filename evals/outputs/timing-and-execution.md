These are fresh-agent responses to fictional planning fixtures. No media was rendered or inspected, and only Brief I's offline checker was executed.

## Brief I: Correct the edit by extending C to frame 288

Keep A at `[0,72)` and B at `[72,168)`. Change C from `[156,276)` to **`[156,288)`**, retaining the existing 12-frame dissolve over `[156,168)`.

| Shot | Corrected interval | Timeline duration |
|---|---:|---:|
| A | `[0,72)` | 72 frames |
| B | `[72,168)` | 96 frames |
| C | `[156,288)` | 132 frames |
| B-to-C overlap | `[156,168)` | 12 shared frames |

The original picture ends at frame 276, so it supplies **11.5 seconds**, despite declaring `total_frames=288`. The correction supplies:

\[
72+96+132-12=288\text{ frames}, \qquad 288/24=12\text{ seconds}.
\]

C’s source requirement is **132 + 8 + 8 = 148 frames**, leaving **12 spare frames** from the 160 usable, already conformed frames. The dissolve is already included in C’s interval and must not be added again when calculating its source requirement.

A feasible allocation within C’s source is `[8,140)` for the 132-frame edit, `[0,8)` for the head handle, `[140,148)` for the tail handle, and `[148,160)` spare. That is a frame allocation, not a claim that the added content has been inspected. The actual extension and landing still require playback. This follows the local [shot contract](../../references/shot-contract.md).

### Created and validated JSON

Temporary file: [brief-i-shot-plan.json](brief-i-shot-plan.json).

```json
{
  "schema_version": 1,
  "title": "Brief I corrected 12-second edit",
  "fps": "24",
  "resolution": [1920, 1080],
  "total_frames": 288,
  "shots": [
    {
      "id": "A",
      "purpose": "Retain the approved opening.",
      "primary_focus": "Existing approved subject in A.",
      "start_frame": 0,
      "end_frame": 72,
      "route": "edit",
      "invariants": ["Preserve A picture and timing."],
      "checks": ["Compare with the approved A edit."]
    },
    {
      "id": "B",
      "purpose": "Retain the approved middle beat.",
      "primary_focus": "Existing approved subject in B.",
      "start_frame": 72,
      "end_frame": 168,
      "route": "edit",
      "invariants": ["Preserve B picture and timing."],
      "checks": ["Compare with the approved B edit."]
    },
    {
      "id": "C",
      "purpose": "Complete the final beat at exactly twelve seconds.",
      "primary_focus": "Existing approved subject in C.",
      "start_frame": 156,
      "end_frame": 288,
      "route": "edit",
      "invariants": [
        "Preserve C start and the twelve-frame B-to-C dissolve."
      ],
      "checks": [
        "Inspect the added twelve source frames and final landing."
      ],
      "source": {
        "available_frames": 160,
        "head_handle_frames": 8,
        "tail_handle_frames": 8
      }
    }
  ],
  "transitions": [
    {
      "from": "B",
      "to": "C",
      "kind": "dissolve",
      "overlap_frames": 12
    }
  ]
}
```

I ran:

```bash
python3 /home/agent/.codex/skills/remote-skills/cinematic-director/scripts/check_plan.py /tmp/brief-i-shot-plan.json
```

**Actual result: exit code 0, `valid_structure: true`, `errors: []`.**

```json
{
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
  }
}
```

A and B’s source counts were deliberately omitted because none were supplied. The checker validates declared timeline structure and arithmetic. It does not establish media quality, readable holds, continuity, sound, or source content.

## Brief J: Use Blender for exact camera requirements; keep the fixture request within its schema

The connected fixture is **`fixture_video_v1`**. The article’s Cinema Studio 4.0 feature descriptions do not establish controls on this fixture. Its supplied capability facts are the authority for the planned connected request.

### Six-second shot treatment

The lamp remains rigid and illuminated throughout. Begin with a clear three-quarter product composition, then approach the hinge and lamp head so their material and construction become easier to inspect.

| Time | Intended event |
|---|---|
| 0.0–0.5 s | Establish the lamp and stable lighting. |
| 0.5–5.0 s | One restrained forward dolly, with a level horizon and continuous focus on the chosen product detail. |
| 5.0–6.0 s | Hold the tighter landing without drift. |

Those timestamps are editorial targets. They become exact only through deterministic animation or verified editing.

### Control assignment

| Requested choice | Connected fixture | Deterministic production route |
|---|---|---|
| Six-second duration | Supported integer duration `6` | Verify actual output and conform to the final timeline. |
| Aspect ratio | Supported `16:9` or `9:16`; use `16:9` for this proposed shot | Inspect framing in the selected ratio. |
| `lens_mm=85` | Descriptive intent only; unsupported parameter | Set a real 85 mm camera lens in Blender, with a declared sensor assumption. |
| `aperture=1.4` | Descriptive intent only; unsupported parameter | Set f/1.4 in the Blender camera and inspect whether the required detail remains in focus. |
| `shutter=180` | Unsupported parameter | Set an exposure interval equivalent to half a frame, using the installed renderer’s actual controls. |
| `easing="cubic"` | Unsupported parameter | Implement a defined curve in Blender; “cubic” alone does not specify a unique trajectory. |
| Exact camera travel and landing | Prompted intent | Keyframe the real camera transform. |
| Exact final duration | Request plus output verification | Set and inspect the editor’s final frame count. |

For a deterministic proof, assume **24 fps and a 36 mm active sensor width**, unless the production specifies otherwise. That gives 144 delivered frames over six seconds, and 180 degrees corresponds to an exposure of `1/48` second. Position the camera from the desired perspective, then verify framing with the 85 mm lens.

Define the requested cubic easing explicitly as:

\[
s(u)=3u^2-2u^3,\qquad
u=\operatorname{clamp}\left(\frac{t-0.5}{4.5},0,1\right).
\]

Interpolate between the blocked opening and landing camera positions with `s(u)`. This gives zero velocity at the move’s endpoints and a settled final second. Keep the focal length fixed; the camera translates through the scene. A 2D editor scale animation would not produce the same parallax.

Because the producer asks for exact optical and motion values, **Blender is the preferred production route if those values are binding**. The editor handles conforming and finishing. The local [camera reference](../../references/camera-and-lenses.md) and [tool handoff reference](../../references/higgsfield-and-companions.md) make this distinction explicit.

### Next supported connected-request shape

This is a planning envelope. The fixture facts do not specify the actual API wrapper names, so the executor must map the wrapper to its real schema. The values, parameter names, and reference role below stay within the supplied capabilities.

```json
{
  "model_id": "fixture_video_v1",
  "duration": 6,
  "aspect_ratio": "16:9",
  "references": [
    {
      "role": "start_image",
      "asset": "<approved lamp start-image reference>"
    }
  ],
  "params": {
    "mode": "std",
    "sound": "off",
    "cfg_scale": 0.5
  },
  "prompt": "Keep the reference lamp rigid and its illumination constant. Begin in a stable three-quarter product composition. Make one restrained forward dolly toward the hinge and lamp head, with a level horizon and the important product detail remaining sharp. Ease gently into the movement, settle into a tighter composition, and finish with a stable hold. Use a narrow field of view and a softly separated background."
}
```

The approved start image must exist and be inspected before submission. An `end_image` could be considered when an approved landing image and a supported combined-input shape are available. It would still require continuity inspection.

Do not add `lens_mm`, `aperture`, `shutter`, or `easing` to `params`. No generation was made.

## Brief K: Resolve the information load before producing the fifteen-second video

**The current package is not ready for picture lock.** Seventy-four words in 15 seconds implies 296 words per minute, before accounting for pauses. Reserving a silent four-second final hold leaves 11 seconds and requires approximately **404 words per minute**. Even if speech continues through the final hold, the chart, captions, and titles still compete for attention.

These calculations identify the constraint. They do not establish a universal acceptable speaking rate.

### Recommended fifteen-second edit

Preserve the requested length by making this a **single-takeaway educational sequence**. Propose a factual rewrite to approximately **24–28 words as an initial drafting budget**, then measure the actual performance. Preserve the complete 22-value chart and use the voice to direct attention to one selected relationship. Treat the three titles as brief labels integrated into existing beats.

| Time | Picture and graphics | Voice and reading requirement |
|---|---|---|
| 0.0–0.3 s | Title 1 enters over a simple orienting image. | No essential reading assigned during the entrance. |
| 0.3–2.5 s | Title 1 is settled. Establish the subject. | One short setup statement. |
| 2.5–2.8 s | Cut to the chart; Title 2 settles. | Keep transition simple. |
| 2.8–10.5 s | Hold the complete 22-label chart. Highlight the selected comparison without moving the chart underneath the reader. | Explain one relationship. Keep captions in a reserved region, clear of values and labels. |
| 10.5–11.0 s | Title 3, the final message, enters. | Finish the thought before the settled hold. |
| 11.0–15.0 s | Fully legible, stable final message. | Protect the complete four-second reading hold. |

This proposal does **not** establish that viewers can read all 22 labeled values during the chart beat. Before production, inspect the real chart at delivery size with the actual captions. If the requirement is for every value to be individually understood during one viewing, the duration needs to increase. Showing a dense chart is not the same as making its content comprehensible.

The brief supplies no actual narration, chart, or title copy. A factual rewrite and a verified hierarchy therefore cannot be completed yet. The next editorial handoff requires those actual materials, together with the educational takeaway.

If all 74 words and comprehensive reading of all 22 values are mandatory, prepare a longer animatic rather than silently dropping content or speeding up the voice. A **40-second animatic** is a concrete first experiment: establish the subject, guide attention through meaningful chart groups, return to the overall conclusion, and reserve seconds 36–40 for the final hold. Its eventual duration must follow the measured voice and reading test; 40 seconds is a proposal, not a validated minimum.

### ElevenLabs Speech handoff

Prepare three separate components:

1. **Canonical text:** the approved short script, exact chart values, names, units, and subtitle wording.
2. **Synthesis text:** the spoken version with any verified pronunciation substitutions and only necessary supported cues.
3. **Direction and timing:** a clear educational delivery to one listener, selective emphasis on the chosen comparison, and an approximately 10.2-second speaking window in the proposed edit.

Preserve an established voice if one exists. The installed Speech skill’s planning default is `eleven_v4`, subject to workspace verification before synthesis. Keep its saved/default settings for the initial take. Do not invent a Speed parameter or use unsupported SSML to force the performance into the edit.

The speech handoff must return the **actual auditioned take and measured timing before final picture lock**. Align captions to that audio, preserve canonical wording, and check names and values by listening. A matching transcript alone cannot establish naturalness. These decisions follow the local [Speech skill](https://github.com/MikeyNu/agent-elevenlabs/blob/main/SKILL.md) and its [performance direction reference](https://github.com/MikeyNu/agent-elevenlabs/blob/main/references/performance-direction.md).

### Cinematic Scroll Director handoff boundary

I read the requested Cinematic Scroll Director skill. Its website implementation workflow is outside this linear-video assignment.

Its useful contribution here is the principle of settling the visual stage before dense reading and composing for the actual display. The production handoff goes to the editor/compositor for titles, chart graphics, and timed captions. No scroll progress, sticky sections, semantic HTML overlay, browser playback implementation, or web storyboard validator is needed.

This is a prepared handoff plan. No speech was generated or auditioned, and no handoff was executed.

## Brief L: Delivery approval remains unassessed

**Outcome: `not_assessed` for pacing, lip sync, temporal continuity, and delivery grain.** Withhold final delivery approval pending the necessary media. This is an evidence limitation, not an observed failure of the clip.

| Requested approval | Current evidence permits | Evidence still required |
|---|---|---|
| Pacing | A sparse still sequence cannot establish felt timing. | Full normal-speed playback with the intended audio. |
| Lip sync | No audio or playable mouth performance is available. | Matching picture and speech, checked through complete utterances. If no visible speech exists, record this check as not applicable. |
| Continuity | The written “stable subject” statement is an unverified analysis claim. Still samples cannot cover the two-second gaps. | Continuous playback and consecutive frames through motion, occlusion, contacts, and suspected incidents. |
| Grain in 9:16 compression | Contact-sheet appearance cannot establish texture at delivery scale or through time. | The actual vertical crop, full-resolution frames, and the real delivery encode in motion. |

No image attachment or playable source was supplied in this assignment, so even the contact sheet’s reported beauty is not an independent visual inspection by me. A nominal sample labeled “8 seconds” may also be an approximate or clamped endpoint. Verify the actual source timestamps.

### Concrete next steps

1. **Obtain the original playable clip and matching intended audio.** Preserve the originals and generation lineage. Inspect actual dimensions, duration, timestamps, frame rate, audio tracks, and color metadata.
2. **Review all eight seconds at normal speed in the intended 9:16 composition.** Check subject identification, motion, landing, cropping, and caption clearance. Compare with neighboring shots if continuity approval covers a sequence.
3. **Inspect native frames and consecutive intervals.** Concentrate on visible speech, contacts, changing occlusions, reflections, topology, and the last usable frames. Record reproducible timestamps and regions instead of relying on a written scene description.
4. **Encode the actual delivery candidate.** Use the agreed vertical dimensions, codec, bitrate, and color handling. Compare its grain, fine detail, gradients, and motion with the master at normal viewing size and native scale.
5. **Repair only observed defects.** Correct a sync offset before replacing a performance. If grain shimmers or masks detail after compression, adjust its scale or strength and repeat the same encode comparison. Do not add texture to conceal a continuity failure.
6. **Approve by criterion after reinspection.** Record the tested versions and coverage. Preserve the known generated origin regardless of the quality verdict.

This follows the local [quality review workflow](../../references/quality-and-repair.md). No detector ran, no audio was heard, and no delivery encode was inspected during this assignment.
