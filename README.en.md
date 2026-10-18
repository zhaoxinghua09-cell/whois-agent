# WhoIs agent · Identity & Memory Suite (English)

[![LGD 有籍](https://img.shields.io/badge/有籍-8%2F8-brightgreen)](#)
[![LGD 有证](https://img.shields.io/badge/有证-8%2F8-brightgreen)](#)
[![license](https://img.shields.io/badge/license-MIT-blue)](#)
[![AI-friendly](https://img.shields.io/badge/AI--friendly-llms.txt-101E2C.svg)](llms.txt)

> **Know who your agent is, remember everything, prove it, register every output.**

The canonical, bilingual README lives in [README.md](README.md).

One collection, eight LGD-governed sub-skills, one identity lifecycle —
**Register → Remember → Verify → Output → Evolve**.

## Quick Start

```bash
git clone https://github.com/zhaoxinghua09-cell/whois-agent
cd whois-agent
bash install.sh        # or: powershell -File install.ps1
```

Per-agent:

```bash
claude plugin install whois-agent@claude-plugins   # Claude Code
cp -r . ~/.codex/whois-agent                       # Codex
cp -r . ~/.cursor/whois-agent                      # Cursor
```

## The pipeline

```text
[1 REGISTER] agent-boarding-pass
      ▼
[2 REMEMBER] agent-memory-keeper · session-continuity-protocol · context-engineering
      ▼
[3 VERIFY]   verified-agent-identity ★ · agent-loop-guard
      ▼
[4 OUTPUT]   agent-output-registry
      ▼
[5 EVOLVE]   agent-evolution ── writes back to memory
```

## Repository layout

| Path | Purpose |
|---|---|
| `SKILL.md` | skill main file (YAML frontmatter + read_when triggers) |
| `package.json` | package metadata |
| `install.sh` / `install.ps1` | one-shot installers |
| `scripts/whois_route.py` | route a request to the right sub-skill slug |
| `references/subpackage-index.md` | slug index and install locations |

Each sub-skill is published independently on the public model registry; this repo
copies none of their implementations.

## License

MIT — Copyright (c) 2026 XLGD · SynomosAI. Full terms in [LICENSE](LICENSE).
Cite as: `https://github.com/zhaoxinghua09-cell/whois-agent`.
