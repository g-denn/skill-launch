# Skill Create

Launch a useful Agent Skill as a public, installable GitHub repository—with evidence for every release layer.

`skill-create` helps an agent research an underserved job, compare candidate ideas, build the smallest credible skill, publish it, and verify that strangers can actually install it. It keeps brainstorming, local building, and public launch as separate authorization modes.

## Install

```bash
npx skills add g-denn/skill-create --skill skill-create
```

Then ask:

```text
Use $skill-create to research, build, publish, and verify a public skill for a narrow problem in my domain.
```

## What it verifies

- Local validation and tests
- Git commit and pushed default branch
- Anonymous public access
- Tagged GitHub release and CI
- Clean installation from `OWNER/REPO`
- skills.sh discovery when supported

## What it will not do silently

It will not publish without explicit launch authorization. Repository publication does not authorize social posts, third-party messages, paid promotion, account changes, or uploading private data.

## Repository layout

- [`skills/skill-create/SKILL.md`](skills/skill-create/SKILL.md) — agent instructions
- [`skills/skill-create/references`](skills/skill-create/references) — selection, release, and distribution contracts
- [`scripts/validate.py`](scripts/validate.py) — dependency-free repository checks
- [`tests/test_contract.py`](tests/test_contract.py) — contract tests

## Development

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

## License

MIT. See [LICENSE](LICENSE).
