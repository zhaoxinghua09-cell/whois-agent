#!/usr/bin/env bash
# whois-agent one-shot install (manual-copy mode, no auto-update).
set -e
SRC="$(cd "$(dirname "$0")" && pwd)"
echo "WhoIs agent installer — copying skill into agent skill dirs."
mkdir -p "$HOME/.claude/skills" "$HOME/.codex" "$HOME/.cursor"
cp -r "$SRC" "$HOME/.claude/skills/whois-agent"
cp -r "$SRC" "$HOME/.codex/whois-agent"
cp -r "$SRC" "$HOME/.cursor/whois-agent"
echo "Done. Verify: python3 $HOME/.claude/skills/whois-agent/scripts/whois_route.py --list"
