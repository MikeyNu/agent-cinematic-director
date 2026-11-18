# Working on Cinematic Director

Maintain this as a reusable skill that helps an agent direct, execute and inspect actual production work with available tools.

## Editing priorities

- Keep `SKILL.md` lean and route detail to one-level references. Link every reference from the entrypoint and give references over 100 lines a contents list.
- Preserve the exact skill name `cinematic-director`. Keep the interface metadata aligned with it.
- Use primary sources for technical claims. Label firsthand creator experience, promotional examples, historical model details and unverified community reports.
- Separate physical facts, creative recommendations, descriptive AI intent and real executable controls.
- Preserve user style and existing authorization. Do not add a repeated approval step for work already authorized.
- Keep quality and provenance separate. Never claim footage was watched or audio heard based on text, metadata or a contact sheet alone.
- Preserve accepted material. Prefer local repairs, verified current capabilities, bounded attempts and recovery of unknown job state.
- Do not use em dashes in authored material.

## Checks before publishing

Run `python3 scripts/check_skill.py .`, `python3 -m unittest discover -s tests -v`, and `python3 scripts/check_plan.py assets/shot-plan.example.json`.

When changing instructions that affect behavior, use fresh-agent scenarios with task-local inputs. Do not disclose expected answers or prior diagnoses. Save raw responses and a scoped assessment, including limitations and failed cases.

Never make paid generations to test the skill or preflight script. Use fictional media identifiers and offline fixtures. Do not publish credentials, account balances, private URLs, customer references or real job identifiers in research snapshots or tests.

Keep hosted CI enabled. Do not add CI-skipping commit markers or present a blocked/unexecuted workflow as passing. Report local and hosted verification separately.

Installable files are `SKILL.md`, `agents/`, `references/`, `assets/`, and `scripts/check_plan.py`. Repository documentation, CI, tests and assessment records are maintenance material, not required agent context.
