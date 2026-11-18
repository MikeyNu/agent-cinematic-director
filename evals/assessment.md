# Cinematic Director assessment

Assessed 18 November 2026. The skill passed the reviewed decision criteria for twelve fictional planning scenarios across three fresh agent contexts. This is evidence of usable instructions in those scenarios, not a measured improvement in generated-film quality or a guarantee across all agents and tools.

## Method

Each agent received the skill and four production briefs with task-local inputs. No expected answers or earlier conclusions were supplied. Agents could read relevant local references. No paid generation, live configuration change, or media upload was allowed. Brief I permitted creation of a temporary JSON plan and running the bundled checker.

The skill's authors did not serve as the fresh agents. The root reviewer read the responses and checked concrete compliance with each brief. Raw responses are retained, with local reference links normalized for the repository. No quality scores were fabricated and no inaccessible footage was claimed to have been watched.

## Scenario outcomes

| Case | Decision criteria | Observed behavior | Outcome |
| --- | --- | --- | --- |
| A | Separate viewpoint, field of view, framing and focus under a tight-room constraint | Corrected the fixed-position compression claim; offered viable lens/distance choices, sensor assumptions and a performance-aware focus plan | Pass |
| B | Preserve centered exact product design and both delivery ratios while treating visual devices as conditional | Kept the watch centered, used ratio guides for surrounding design, separated optical intent from actual controls, used approved artwork and checked both crops | Pass |
| C | Apply twelve principles beyond characters without deforming protected glyphs or sacrificing reading time | Gave all twelve distinct applications, deterministic timing, a 6.5-second settled hold and a real website reduced-motion branch | Pass |
| D | Make an overloaded chase executable, preserve the single-shot ambition and exact address | Planned an apparent continuous sequence with four simple plates and motivated joins; distinguished a true uninterrupted take and a deterministic alternative; composited exact text | Pass |
| E | Interpret mixed sources correctly, protect brand color and avoid universal effect order | Used separate Sony, unknown generated-video and sRGB handling; withheld unsupported camera-log assignment; made teal and grain contextual choices with export checks | Pass |
| F | Distinguish reported from observed defects; require temporal evidence; repair geometry directly | Marked the incident unverified, requested original/consecutive frames, prepared detector/executor handoffs, preserved invariants and rejected concealment as proof of repair | Pass |
| G | Preserve intentional stylization and separate quality from generated origin | Stopped score-chasing; accepted stop-motion traits as intentional; required final quality checks and retained known generation history | Pass |
| H | Recover ambiguous submissions while preserving existing spending authority | Reserved the unresolved 40-credit request, identified 30 uncommitted and 110 potential exposure, and chose recovery without another paid job | Pass |
| I | Correct exact duration, overlap arithmetic and source handles; run the helper | Extended C to frame 288, retained the 12-frame dissolve, checked 148 required source frames against 160, ran the checker successfully and disclosed missing A/B source checks | Pass |
| J | Respect the connected schema and move exact requirements to a capable route | Excluded unsupported optical/easing fields, labeled the request wrapper as a planning envelope, and selected Blender for binding camera values | Pass |
| K | Resolve information overload before locking speech, captions and motion | Calculated 296 or about 404 words per minute, proposed a measured shorter script or longer animatic, protected chart/caption readability and avoided an irrelevant scroll implementation | Pass |
| L | Avoid temporal/audio/compression claims from sparse stills and text | Returned not-assessed outcomes, distinguished them from observed failures, and requested full playback, actual audio, timestamps and a delivery encode | Pass |

Raw responses:

- [Shots and motion, A through D](outputs/shots-and-motion.md).
- [Postproduction and repair, E through H](outputs/post-and-repair.md).
- [Timing and execution, I through L](outputs/timing-and-execution.md).
- [Brief I validated JSON](outputs/brief-i-shot-plan.json).
- [Exact scenario inputs](scenarios.md).
- [Actual local verification output](local-verification.md).

## Deterministic checks

The standard-library suite contains **41 tests**, run against the actual checker. It covers rational frame rates, exact duration, gaps, ordering, duplicate IDs, malformed transitions, correct and incorrect overlaps, triple overlap, source handles, invalid types, missing fields, malformed JSON, duplicate JSON keys, non-finite values, input preservation and invocation from another working directory.

The bundled example validates as 288 frames at 24 fps, exactly 12 seconds. Brief I independently used the helper to correct an 11.5-second timeline that had been declared as 12 seconds. Its remaining source warnings were reported rather than hidden.

The skill-creator validator passed against the canonical personal skill directory. The repository structure check passed for frontmatter, interface metadata, entrypoint size, local links and long-reference navigation. The entrypoint is approximately 1,600 words and routes to ten references. Authored material was checked for the user's punctuation constraint.

During repository assembly, one test invocation occurred before the checker had been mirrored into the repository and failed to import it. Mirroring the validated canonical files resolved that assembly error. The structure checker initially treated valid directory links as missing files; it was corrected to allow existing directory targets and then passed. These were packaging/checker issues, not concealed successful runs.

## Final editorial review

The fresh-agent scenarios used the drafted main workflow and reference set. After those responses, a final editorial pass made the still-image route explicit and expanded the lens reference with prime/zoom, spherical/anamorphic and close-focus choices, supported by Cooke and ARRI primary documentation. Those additions did not change the timeline checker or companion contracts. Final structural checks were rerun. The new lens table was source-reviewed, not separately evaluated through a rendered test.

## Limits and next production evidence

- Three fresh contexts handled four tasks each; this was not twelve isolated model runs or a multi-model benchmark.
- Review was qualitative, performed against explicit task constraints. There was no blinded audience study or measured token-savings experiment.
- No film, tutorial video or comparison footage was watched during the source research; the creator reference identifies written or description-only evidence.
- No paid images, video, speech, physical camera takes or final color-managed renders were produced for this assessment.
- Live Higgsfield catalog discovery was read-only and showed the inspected connection's support at that time. It does not establish future or platform-wide capability.
- A real production should still verify its representative shot, actual audio, native/consecutive frames, full-speed edit, color handling and delivered encode. The skill makes those checks part of execution.

Hosted CI status is reported separately from these local results. An unstarted or blocked runner must not be described as a passing workflow.
