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

| slug | stage | dl | LGD |
|------|------|---:|-----|
| agent-boarding-pass | register | 92 | 有籍 |
| agent-memory-keeper | remember | 96 | 有证 |
| session-continuity-protocol | remember | 59 | 三律 |
| context-engineering | remember | 92 | 三律 |
| verified-agent-identity ★ | verify | 330 | 有籍 |
| agent-loop-guard | verify | 94 | 有门禁 |
| agent-output-registry | output | 141 | 有籍 |
| agent-evolution | evolve | 109 | 三律 |

> Each sub-skill is published independently on the public model registry; install it there by slug. Lineage SSOT: `skills_registry.toml`.

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

## 仓库结构 / Repository layout

```text
whois-agent/
├── SKILL.md              # 技能主文件（Agent Skills 规范 · YAML frontmatter）
├── package.json          # 包元数据（name / version / author / license / keywords）
├── install.sh            # 一键安装（macOS / Linux）
├── install.ps1           # 一键安装（Windows PowerShell）
├── scripts/whois_route.py # 按 slug 把请求路由到对应子技能
├── references/subpackage-index.md  # 8 个子技能的 slug 索引与安装位置
├── .claude-plugin/ .codex-plugin/ .cursor-plugin/  # 各 Agent 运行时插件清单
├── openclaw.plugin.json  # OpenClaw 插件清单
├── README.md             # 本文件（双语）
└── llms.txt / llms-full.txt / AGENTS.md / SECURITY.md
```

每个子技能以 slug 引用、实现独立发布在公开模型仓；本合集**不复制任何子包实现**，只做编排、管线图与证据条。

## 触发词 / When to use

- 跨会话失忆、开局不知上轮做了什么（session continuity）
- 智能体身份漂移、需要一张可核验的身份卡（verified identity）
- 要求每一次 AI 产出都留痕可溯（output registry）
- 把记忆、上下文预算、循环护栏当作一整套来治理（one suite）

```text
触发词示例：who is my agent / 跨会话记忆 / 身份核验 / 产出留痕 / anti-drift identity / memory lifecycle
```

## 安全 / Security

如发现脚本存在危险行为、子技能索引指向错误目标或插件清单泄漏敏感信息，请按 [`SECURITY.md`](SECURITY.md) 的方式私下报告，不要在公开 issue 中披露。

## License / 许可

本合集以 **MIT 许可证**发布，版权声明原文如下（未修改）：

> MIT License — Copyright (c) 2026 XLGD · SynomosAI

完整条款见仓库根目录 [LICENSE](LICENSE)。引用时请标注仓库名与链接
`https://github.com/zhaoxinghua09-cell/whois-agent`。各子技能以其各自独立许可证为准。

---

*Governance-as-a-Service · LGD-Core v0.2 · XLGD · SynomosAI · 本合集零改动子包实现。*
