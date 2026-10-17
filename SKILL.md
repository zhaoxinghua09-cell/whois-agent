---
name: whois-agent
description: "WhoIs agent — one install that answers who your agent is, remembers everything across sessions, verifies its identity, and registers every output. Use when you need agent identity governance, cross-session memory, anti-drift identity verification, or an auditable output registry."
version: 1.0.0
author: "SynomosAI (LGD initiative)"
license: MIT
copyright: "XLGD · SynomosAI"
display_name: "WhoIs agent · 身份与记忆套件"
ai_protocol: true
read_when:
  - "my agent forgets context between sessions / 跨会话失忆、开局不知上轮做了什么"
  - "agent identity drifts or needs a verified identity card / 身份漂移、需要可核验身份"
  - "I need every AI output registered & traceable / 产出要留痕可溯"
  - "I am wiring memory, context budget, and loop safety as one suite / 把记忆/上下文/护栏当一套装治理"
---

# WhoIs agent — Identity & Memory Suite · 身份与记忆套件

> **One-line pain:** your agent is amnesiac and its identity drifts. WhoIs agent makes it **know who it is, remember everything, prove it, and register every output** — as one lifecycle, not eight loose skills.
> **一句话痛点：** 你的智能体既失忆、身份又漂移。WhoIs agent 让它**知道自己是谁、记住一切、可被验证、并登记每一次产出**——一条生命周期，而不是八个散装技能。

---

## English

### What this collection is

WhoIs agent is a **lifecycle-anchored** orchestration suite over 8 LGD-governed sub-skills (referenced by slug, implementations live in their own packages — this repo copies nothing). It narrates one identity lifecycle: **Register → Remember → Verify → Output**, with an **Evolution** loop feeding improvement back into memory.

It is the "Identity & Memory" column of the LGD collection strategy (alongside GovernanceOS and the AI Safety Suite). It bundles the highest-download identity/memory packages in the 113-package lineage under one install, one ASCII pipeline, and one LGD three-laws status band.

### The one-page pipeline

```
                 ┌──────────────────────────────────────────────────────────┐
                 │            WhoIs agent · identity lifecycle              │
                 │                                                          │
   onboard ──►  [1 REGISTER]   agent-boarding-pass        (登机牌 / 有籍✓)   │
                 │     issue boarding pass = who am I, what scope            │
                 │                          │                               │
                 ▼                          ▼                               │
   remember ─►  [2 REMEMBER]  agent-memory-keeper      (长期记忆 / 有证✓)    │
                 │            session-continuity-protocol (开局四步 / 三律✓) │
                 │            context-engineering       (context-token-budget)│
                 │                          │                               │
                 ▼                          ▼                               │
   verify   ──► [3 VERIFY]    verified-agent-identity  (身份核验 / 有籍✓) ★  │
                 │            agent-loop-guard         (失控护栏 / 有门禁✓)   │
                 │                          │                               │
                 ▼                          ▼                               │
   output   ──► [4 OUTPUT]    agent-output-registry     (产出有籍 / 有籍✓)    │
                 │                          │                               │
                 └──────────► [5 EVOLVE] agent-evolution (进化飞轮 / 三律✓) ◄┘
                              learns from registered outputs, writes back to memory
```

### Stage playbook — when to use / which slug / expected output

| # | Stage | Sub-skill slug | When to invoke | Expected output |
|---|-------|----------------|----------------|-----------------|
| 1 | Register | `agent-boarding-pass` | A new agent/session starts; need to pin identity & scope | A boarding-pass record (who, scope, lineage) |
| 2 | Remember | `agent-memory-keeper` | Long-term memory must persist across sessions | A governed memory entry + memory-audit result |
| 2 | Remember | `session-continuity-protocol` | Resuming after a break; "the four opening steps" | A continuity handoff (what was done, next step) |
| 2 | Remember | `context-engineering` | Context/token budget must fit the task | A context-budget plan (what to keep vs. compress) |
| 3 | Verify | `verified-agent-identity` ★ | Identity must be proven, not asserted | A verified identity claim (core package, 330 dl) |
| 3 | Verify | `agent-loop-guard` | Agent is repeating / looping / drift risk | A loop-guard verdict (halt or continue) |
| 4 | Output | `agent-output-registry` | Any deliverable leaves the session | An immutable output-registry record (有籍) |
| 5 | Evolve | `agent-evolution` | Registered outputs feed improvement | An evolution-flyer entry written back to memory |

> ★ = flagship. All eight are referenced by slug; open each package's own SKILL.md for its scripts and details. **No implementation is duplicated here.**

### LGD three-laws status band (实读 / read live from dashboard 2026-10-17)

| slug | 有籍 registered | 有证 evidenced | 有门禁 gated | overall |
|------|:---:|:---:|:---:|:---:|
| agent-boarding-pass | ✓ | ✓ | ✓ | ✓ |
| agent-memory-keeper | ✓ | ✓ | ✓ | ✓ |
| session-continuity-protocol | ✓ | ✓ | ✓ | ✓ |
| context-engineering | ✓ | ✓ | ✓ | ✓ |
| verified-agent-identity | ✓ | ✓ | ✓ | ✓ |
| agent-loop-guard | ✓ | ✓ | ✓ | ✓ |
| agent-output-registry | ✓ | ✓ | ✓ | ✓ |
| agent-evolution | ✓ | ✓ | ✓ | ✓ |

**Badge row:** `有籍 8/8 ✓` · `有证 8/8 ✓` · `有门禁 8/8 ✓` · `三律全绿 8/8 ✓`
System baseline (113-package lineage): 有籍 113/113 = 100% · 有证 112/113 = 99.1% · 有门禁 112/113 = 99.1%.

### Quantified evidence bars (实读 / downloads-baseline_20261017.json, modelscope cumulative)

| sub-skill | downloads |
|-----------|----------:|
| verified-agent-identity ★ | **330** |
| agent-output-registry | 141 |
| agent-evolution | 109 |
| agent-memory-keeper | 96 |
| agent-loop-guard | 94 |
| agent-boarding-pass | 92 |
| context-engineering | 92 |
| session-continuity-protocol | 59 |
| **suite total (8)** | **1,013** |

Adjacent memory-core packages (referenced, not in the 8-stage lifecycle): `ai-brain-learning-memory-pro` 168 dl, `ai-brain-learning-memory` 134 dl.

### Routing (USK v3 cli)

```
python scripts/whois_route.py --list                 # list the 8 sub-skills
python scripts/whois_route.py --route "my agent forgot the last session"   # -> stage 2
```

---

## 中文

### 本合集是什么

WhoIs agent 是一条**生命周期锚定**的编排套件，编排 8 个受 LGD 治理的子技能（按 slug 引用，实现留在各包内——本仓不复制实现）。它叙述一条身份生命周期：**登记 → 记忆 → 验证 → 输出**，并由一条**进化**回环把改进写回记忆。

它是 LGD 合集战略中的「身份与记忆」一列（与 GovernanceOS、AI 安全套件并列）。它把 113 包血缘里下载量最高的身份/记忆包，收拢到一次安装、一页 ASCII 流水线、一条 LGD 三律状态带之下。

### 一页流水线图

（见上方 English 区 ASCII 图，同一图中英共用。）

### 环节手册——何时用 / 调哪个 slug / 预期输出

（见上方表格，中英共用。）要点：开局先 `agent-boarding-pass` 登记身份 → 跨会话用 `agent-memory-keeper` + `session-continuity-protocol` 记住上下文，用 `context-engineering` 控 token 预算 → 用 `verified-agent-identity`（旗舰，330 下载）核验身份、`agent-loop-guard` 拦失控循环 → 每次产出经 `agent-output-registry` 登记留痕 → `agent-evolution` 从登记产出中学习并回写记忆。

### LGD 三律状态带（实读 2026-10-17）

上表 8 包 **有籍 8/8 ✓、有证 8/8 ✓、有门禁 8/8 ✓、三律全绿 8/8 ✓**。系统基线（113 包血缘）：有籍 100%、有证 99.1%、有门禁 99.1%。

### 量化证据条（实读下载基线）

8 包累计下载合计 **1,013**；旗舰 `verified-agent-identity` 330、`agent-output-registry` 141、`agent-evolution` 109。相邻记忆核心包（引用不入 8 环）：`ai-brain-learning-memory-pro` 168、`ai-brain-learning-memory` 134。

### 路由（USK v3 cli）

`python scripts/whois_route.py --list` 列 8 子技能；`python scripts/whois_route.py --route "<你的场景>"` 给出对应环节。

---

*LGD-Core v0.2 · 有籍/有证/有门禁 · 血缘 SSOT: skills_registry.toml · 本合集只编排引用，零改动子包实现。*
