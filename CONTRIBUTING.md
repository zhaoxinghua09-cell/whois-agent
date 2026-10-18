# Contributing / 贡献指南

Thanks for improving WhoIs agent, the identity & memory skill collection.

## Ground rules

- This repo is an **orchestration layer**: reference sub-skills by slug, do **not**
  vendor or modify their implementations here.
- When adding, removing, or reordering a sub-skill, update **both** the table in
  `README.md` and `references/subpackage-index.md`.
- Keep `SKILL.md` frontmatter compatible (`name`, `version`, `author`, `license`,
  `read_when`).
- Keep the LGD evidence bars consistent with a dated dashboard; do not invent numbers.

## Quick start

```bash
git clone https://github.com/zhaoxinghua09-cell/whois-agent
cd whois-agent
bash install.sh
```

## Don't

- Do not change `author` / `copyright` / `license` fields in `SKILL.md`,
  `package.json`, or `LICENSE` — rights fields are changed only by the maintainer.
- Do not commit tokens, credentials, or real conversation memory.

## Report a security issue

Please follow [SECURITY.md](SECURITY.md) and report privately to
zhaoxinghua09@gmail.com.
