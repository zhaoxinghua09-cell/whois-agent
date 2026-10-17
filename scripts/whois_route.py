#!/usr/bin/env python3
"""whois_route.py — USK v3 cli for the WhoIs agent collection.

Routes a user scenario to the correct sub-skill stage of the identity lifecycle.
Zero credentials, read-only. Usage:
    python whois_route.py --list
    python whois_route.py --route "my agent forgot the last session"
"""
import argparse
import sys

# (stage, slug, dl, lgd, trigger-keywords)
SUBS = [
    ("REGISTER",  "agent-boarding-pass",        92,  "有籍",   ["boarding", "enroll", "登记", "登机牌", "new agent", "onboard", "开局身份"]),
    ("REMEMBER",  "agent-memory-keeper",        96,  "有证",   ["memory", "记住", "长期记忆", "remember", "long-term"]),
    ("REMEMBER",  "session-continuity-protocol",59,  "三律",   ["continuity", "resume", "跨会话", "上轮", "忘了", "forgot", "handoff"]),
    ("REMEMBER",  "context-engineering",        92,  "三律",   ["context", "token", "上下文", "预算", "budget", "compress"]),
    ("VERIFY",    "verified-agent-identity",   330,  "有籍",   ["identity", "身份", "verify", "核验", "漂移", "drift", "who am i"]),
    ("VERIFY",    "agent-loop-guard",          94,  "有门禁", ["loop", "repeating", "循环", "失控", "drift guard", "halt"]),
    ("OUTPUT",    "agent-output-registry",    141,  "有籍",   ["output", "registry", "产出", "登记", "留痕", "deliverable", "trace"]),
    ("EVOLVE",    "agent-evolution",          109,  "三律",   ["evolve", "improve", "进化", "飞轮", "learn", "feedback"]),
]

def list_all():
    print(f"{'STAGE':9} {'SLUG':32} {'DL':>5}  LGD")
    for stage, slug, dl, lgd, _kw in SUBS:
        print(f"{stage:9} {slug:32} {dl:>5}  {lgd}")
    print(f"\nTotal 8 sub-skills, {sum(s[2] for s in SUBS)} cumulative modelscope downloads.")

def route(text):
    t = text.lower()
    best, hits = None, 0
    for stage, slug, dl, lgd, kw in SUBS:
        c = sum(1 for k in kw if k.lower() in t)
        if c > hits:
            best, hits = (stage, slug, dl, lgd), c
    if not best:
        print("No strong match — default entry: REGISTER -> agent-boarding-pass")
        return
    stage, slug, dl, lgd = best
    print(f"Scenario: {text}")
    print(f"-> stage {stage}, sub-skill '{slug}' ({dl} dl, {lgd})")
    print(f"   open {slug}/SKILL.md in its own package for scripts & details.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--route", type=str, default="")
    a = ap.parse_args()
    if a.list or (not a.route):
        list_all()
    if a.route:
        route(a.route)
