# WhoIs agent · Identity & Memory Suite

> **Know who your agent is, remember everything, prove it, register every output.**
> **知道你的智能体是谁、记住一切、可被验证、登记每一次产出。**

[![LGD 有籍](https://img.shields.io/badge/有籍-8%2F8-brightgreen)](#)
[![LGD 有证](https://img.shields.io/badge/有证-8%2F8-brightgreen)](#)
[![LGD 有门禁](https://img.shields.io/badge/有门禁-8%2F8-brightgreen)](#)
[![三律全绿](https://img.shields.io/badge/三律全绿-8%2F8-success)](#)
[![downloads](https://img.shields.io/badge/modelscope%20dl-1%2C013-blue)](#)
[![license](https://img.shields.io/badge/license-MIT-blue)](#)

One collection, eight LGD-governed sub-skills, one identity lifecycle — **Register → Remember → Verify → Output → Evolve**.

## English

```
[1 REGISTER] agent-boarding-pass
      │
      ▼
[2 REMEMBER] agent-memory-keeper · session-continuity-protocol · context-engineering
      │
      ▼
[3 VERIFY]   verified-agent-identity ★ (330 dl) · agent-loop-guard
      │
      ▼
[4 OUTPUT]   agent-output-registry
      │
      └──► [5 EVOLVE] agent-evolution ── writes back to memory
```

### Sub-skill index (referenced by slug — no implementation copied)

| slug | stage | dl | LGD | package |
|------|------|---:|-----|---------|
| agent-boarding-pass | register | 92 | 有籍 | [modelscope](https://modelscope.cn/skills/StevenZhao26/agent-boarding-pass) |
| agent-memory-keeper | remember | 96 | 有证 | [modelscope](https://modelscope.cn/skills/StevenZhao26/agent-memory-keeper) |
| session-continuity-protocol | remember | 59 | 三律 | [modelscope](https://modelscope.cn/skills/StevenZhao26/session-continuity-protocol) |
| context-engineering | remember | 92 | 三律 | [modelscope](https://modelscope.cn/skills/StevenZhao26/context-engineering) |
| verified-agent-identity ★ | verify | 330 | 有籍 | [modelscope](https://modelscope.cn/skills/StevenZhao26/verified-agent-identity) |
| agent-loop-guard | verify | 94 | 有门禁 | [modelscope](https://modelscope.cn/skills/StevenZhao26/agent-loop-guard) |
| agent-output-registry | output | 141 | 有籍 | [modelscope](https://modelscope.cn/skills/StevenZhao26/agent-output-registry) |
| agent-evolution | evolve | 109 | 三律 | [modelscope](https://modelscope.cn/skills/StevenZhao26/agent-evolution) |

### Install matrix

```bash
# Claude Code
claude plugin install whois-agent@claude-plugins  # or: cp -r . ~/.claude/skills/whois-agent
# Codex
cp -r . ~/.codex/whois-agent
# Cursor
cp -r . ~/.cursor/whois-agent
# any agent (manual)
git clone https://github.com/zhaoxinghua09-cell/whois-agent
# one-shot
bash install.sh   # or: powershell -File install.ps1
```

### Evidence bars

- **有籍 8/8** · **有证 8/8** · **有门禁 8/8** · **三律全绿 8/8** (dashboard 2026-10-17, live read)
- **1,013 cumulative modelscope downloads** across the 8 sub-skills (downloads-baseline_20261017.json)
- Lineage SSOT: 113-package `skills_registry.toml` — every slug traceable.

## 中文

### 子技能索引（按 slug 引用，不复制实现）

见上表。8 包覆盖身份生命周期：登记（登机牌）→ 记忆（长期记忆/跨会话连续性/上下文预算）→ 验证（身份核验旗舰 330 下载 + 失控护栏）→ 输出（产出有籍登记）→ 进化（进化飞轮回写记忆）。

### 安装

Claude Code / Codex / Cursor / 任意 agent 见上方命令；一键脚本 `install.sh` 或 `install.ps1`。

### 证据条

8 包 **有籍/有证/有门禁 全绿 8/8**（2026-10-17 看板实读）；累计模型仓下载 **1,013**；血缘 SSOT 为 113 包 `skills_registry.toml`，每个 slug 可溯。

---

*Governance-as-a-Service · LGD-Core v0.2 · XLGD · SynomosAI · 本合集零改动子包实现。*
