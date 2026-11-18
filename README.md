# Cinematic Director

A practical directing skill for agents producing cinematic images, films, AI video and motion graphics. It turns a brief into motivated shots, executable production choices and observable acceptance criteria.

Start with [SKILL.md](SKILL.md). Load only the reference needed for the current decision. The main workflow remains compact so routine tasks do not require another broad research pass.

## What it covers

| Area | Decisions the agent can make |
| --- | --- |
| Camera and lenses | Shot size, viewpoint, camera movement, sensor assumptions, focal length, depth of field, focus pulls and coverage |
| Composition and light | Blocking, layers, visual attention, golden-ratio/Fibonacci guides, source motivation, contrast and delivery crops |
| Animation | All twelve principles applied to cameras, props, environments, transitions and typography as well as characters |
| Pacing and editing | Information-driven timing, eyelines, screen direction, action matches, J/L cuts, handles, sound and readable holds |
| Color and finishing | Source interpretation, correction, shot matching, creative looks, skin/product accuracy, grain, halation and export review |
| AI production | References, supported controls, continuity, exact artwork, bounded repair and honest inspection claims |

## Work with your other skills

- **Higgsfield Director:** execute supported generation/editing routes, discover current model controls, manage the authorized allocation and recover jobs. See [the companion repository](https://github.com/MikeyNu/agent-higgsfield).
- **AI Detector:** inspect production quality independently, provide reproducible findings, and keep quality separate from origin. See [the companion repository](https://github.com/MikeyNu/agent-ai-detector).
- **ElevenLabs Speech:** direct and assess voiceover/dialogue before final edit timing. See [the companion repository](https://github.com/MikeyNu/agent-elevenlabs).
- **Cinematic Scroll Director:** implement a directed camera/media journey in a readable, responsive scroll experience when that is the delivery format.

Cinematic Director supplies artistic intent and acceptance criteria. The executing skill supplies current tool syntax and operational controls. No companion is claimed to have run unless it actually did.

## Example requests

```text
Use Cinematic Director with Higgsfield Director to plan a 12-second product film.
Keep the exact product geometry and wordmark. Explain the purpose of each shot,
the motion, light, color, edit and acceptance checks. Plan before generating.
```

```text
Use Cinematic Director and AI Detector to inspect this sequence. Preserve the
accepted shots. Identify reproducible defects, repair the smallest failing unit,
and review the actual export at normal speed before calling it finished.
```

```text
Use Cinematic Director to animate this title. Apply the relevant animation
principles, protect the brand letterforms, allow real reading time, and prepare
a reduced-motion version for the website.
```

## Repository map

- [SKILL.md](SKILL.md): agent entrypoint and reference routing.
- [references](references): ten focused guides with sources and operational examples.
- [assets/shot-plan.example.json](assets/shot-plan.example.json): a fictional 12-second production plan.
- [scripts/check_plan.py](scripts/check_plan.py): offline timeline structure and frame-arithmetic checker.
- [tests](tests): deterministic checker tests.
- [evals](evals): realistic agent-use scenarios, outputs and assessment limits.

The installable skill consists of `SKILL.md`, `agents/`, `references/`, `assets/`, and `scripts/check_plan.py`. Repository maintenance and assessment material is kept outside that installed set.

## Run the offline checks

Requires Python 3.10 or newer. The checker and tests use the standard library and make no network requests.

```bash
python3 scripts/check_skill.py .
python3 -m unittest discover -s tests -v
python3 scripts/check_plan.py assets/shot-plan.example.json
```

The plan checker validates exact frame timing, coverage, declared overlaps, handles and basic required fields. It does not validate footage, aesthetics, audience comprehension, current model support, cost or permission. Read the [contract](references/shot-contract.md) before authoring a JSON plan.

## Research and limits

Research snapshot: **18 November 2026**. Sources include primary cinematography, optics, animation and color documentation; firsthand filmmaker/colorist/motion-designer accounts; and labeled creator/community reports. [Creator practice](references/creator-practice.md) records dates, models, commercial context and evidence limitations. [Evidence and maintenance](references/evidence-and-maintenance.md) explains when targeted research is still needed.

Higgsfield website controls and connected-tool schemas can differ. The skill requires current capability discovery rather than assuming a website feature is an API parameter. Visual quality is assessed against the intended style. A clean synthetic shot remains synthetic, and a detector score is not an objective quality gate.

Offline checks and fresh-agent planning exercises assess structure and decision behavior. They do not establish the quality of a generated film or the reliability of a live model. No paid media generation is needed to run the repository checks.
