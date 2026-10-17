# whois-agent one-shot install (Windows / manual-copy mode).
$ErrorActionPreference = "Stop"
$src = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "WhoIs agent installer — copying skill into agent skill dirs."
$targets = @("$env:USERPROFILE\.claude\skills", "$env:USERPROFILE\.codex", "$env:USERPROFILE\.cursor")
foreach ($t in $targets) {
  New-Item -ItemType Directory -Force -Path $t | Out-Null
  Copy-Item -Recurse -Force $src (Join-Path $t "whois-agent")
}
Write-Host "Done. Verify: python `"$env:USERPROFILE\.claude\skills\whois-agent\scripts\whois_route.py`" --list"
