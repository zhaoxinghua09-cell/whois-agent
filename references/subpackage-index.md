# Sub-package index — referenced by slug, implementations live in each package's own repo.
# Lineage source of truth: skills_registry.toml (internal SSOT).
# Evidence (downloads): downloads-baseline_20261017.json (2026-10-17).
# LGD status: LGD三律达标率看板_20261017.json (2026-10-17; all 8 overall=true).

| slug | stage | version | downloads | lineage | evidence files |
|------|-------|---------|----------:|---------|----------------|
| agent-boarding-pass | REGISTER | 1.0.0 | 92 | LGD-有籍 | SKILL.md, README.md, scripts/agent_boarding_pass.py |
| agent-memory-keeper | REMEMBER | 1.1.0 | 96 | LGD-有证 | SKILL.md, README.md, scripts/memory_audit.py |
| session-continuity-protocol | REMEMBER | 1.0.0 | 59 | LGD-三律 | SKILL.md, README.md |
| context-engineering | REMEMBER (context-token-budget) | 1.0.0 | 92 | LGD-三律 | SKILL.md, README.md, scripts/context_budget.py |
| verified-agent-identity | VERIFY (flagship) | TBD | 330 | LGD-有籍 | SKILL.md, README.md |
| agent-loop-guard | VERIFY | 1.0.0 | 94 | LGD-有门禁 | SKILL.md, README.md, scripts/loop_guard.py |
| agent-output-registry | OUTPUT | 1.0.0 | 141 | LGD-有籍 | SKILL.md, README.md, scripts/output_registry.py |
| agent-evolution | EVOLVE | 1.1.0 | 109 | LGD-三律 | SKILL.md, README.md |

Adjacent memory-core (referenced, not in the 8-stage lifecycle):
- ai-brain-learning-memory-pro 168 downloads (derived_from ai-brain-learning-memory 134 downloads)
