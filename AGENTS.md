# AGENTS.md — Working guide for AI agents

This file is for automated agents (coding assistants, skill loaders). Humans should
read [README.md](README.md).

## What this repo is

`whois-agent` is an **Agent Skill collection / orchestration layer**, not a library
you import. It bundles 8 LGD-governed sub-skills under one install and one
identity-lifecycle narrative (Register → Remember → Verify → Output → Evolve). It
references sub-skills by slug and **vendors none of their implementations**.

## Useful commands

```bash
# install into your agent runtime
bash install.sh            # or: powershell -File install.ps1

# inspect the skill contract (triggers, version, license)
cat SKILL.md

# inspect package metadata
cat package.json

# route a request to the correct sub-skill slug
python scripts/whois_route.py
```

## Do

- Keep `SKILL.md` frontmatter fields compatible when editing (`name`, `version`,
  `author`, `license`, `read_when`).
- When adding or reordering a sub-skill, update both the table in `README.md` and
  `references/subpackage-index.md`.
- Keep the LGD evidence bars (有籍/有证/有门禁) consistent with the dated dashboard.

## Don't

- Do **not** copy or modify sub-skill implementations into this repo — they live in
  their own published packages.
- Do not change `author` / `copyright` / `license` fields in `SKILL.md` or
  `package.json`, and do not edit the `LICENSE` copyright line — rights fields are
  changed only by the maintainer.
- Do not commit tokens, credentials, or real user memory.
- Do not claim a sub-skill has a download count or gate result it does not have.

## Boundary

This collection covers the identity & memory column. It is not a runtime, a
framework, or a chat product; it wires already-published sub-skills into one lifecycle.
