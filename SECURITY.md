# Security Policy / 安全策略

## Report a security issue

If you find a security problem in this repository (e.g. `install.sh` /
`install.ps1` performs a dangerous action, a sub-skill index points to a hostile
target, or a plugin manifest leaks sensitive information), please contact the
maintainer **privately**:

- Email: zhaoxinghua09@gmail.com
- Include: a description, reproduction steps, impact, and your suggested fix.

**Do not disclose unpatched security issues in a public issue / PR.**

## Scope

This repository is an Agent Skill **collection / orchestration layer**:

- **What it runs** — `install.sh` / `install.ps1` copy the skill files into your
  agent runtime directory; `scripts/whois_route.py` routes by slug. No telemetry,
  no phone-home, no account required.
- **Out of scope** — the 8 sub-skills referenced by slug run in their own packages;
  vulnerabilities in those belong to their own upstreams. This repo only stores the
  index and orchestration.
- **Third-party targets** — install commands point to the public model registry and
  your local agent runtime directories. Verify the slug before installing.

## Our commitment

- We will acknowledge valid reports within a reasonable time and assess impact.
- Fixes are recorded in the commit message (desensitized as needed).

## Users, please note

- Get this skill only from the official repository; watch for third-party repacks.
- Review `install.sh` / `install.ps1` before running them on your machine.
- Never commit keys / tokens / real conversation memory into the repo.

---

License: MIT ｜ Copyright (c) 2026 XLGD · SynomosAI
