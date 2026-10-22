# Free ECC + OpenAI Codex: isolated lab setup

**Status:** GitHub Actions can audit an authentic pinned ECC checkout, but those checks do **not** install the ECC Codex plugin, launch AI agents, or authenticate Codex. The ECC Tools paid GitHub App is neither installed nor needed for this approach.

## What is free and what is not

- ECC itself is MIT-licensed open-source code: https://github.com/affaan-m/ECC/blob/main/LICENSE
- The Codex native plugin can be installed without paying ECC Tools.
- Codex model use is governed by **your existing ChatGPT/Codex plan limits** or optional API billing, depending on login method. There is no promise of unlimited use or a separate free model quota.
- GitHub Actions checks in this laboratory do not consume model tokens; they are subject to GitHub Actions usage limits.
- Do **not** place ChatGPT credentials or API tokens in repo files, GitHub Actions logs, or public Issues.

## 1. Recommended: locally isolated Codex CLI

Official ECC Codex instructions: https://github.com/affaan-m/ECC/blob/main/.codex-plugin/README.md

Codex **0.146.0 or newer** is required for the native plugin commands. For **Windows PowerShell**, in a shell where Codex CLI works:

```powershell
codex --version
$env:CODEX_HOME = Join-Path $HOME ".codex-cope-ecc-lab"
New-Item -ItemType Directory -Force -Path $env:CODEX_HOME | Out-Null
git clone https://github.com/FS-GitmeHub/CoPE-ECC-Lab.git
Set-Location CoPE-ECC-Lab
codex login
codex plugin marketplace add affaan-m/ECC
codex plugin add ecc@ecc
codex plugin list --json
codex
```

Choose the **Sign in with ChatGPT** option when supported. Using a dedicated `CODEX_HOME` keeps the plugin registration and login state separate from the usual Codex home; it is *not* a security sandbox. Do not commit anything from that directory.

After opening Codex, review `/plugins` to confirm ECC appears. Review `/hooks` **before trusting or enabling ECC hooks**; hooks may execute programs in the environment. The optional `$configure-ecc` guided setup should be run only after reviewing its proposed changes.

**Important:** Codex native plugins register under the active `CODEX_HOME`, not inside this GitHub repository. Uploading files or running GitHub Actions alone never installs the native plugin.

## 2. Browser-only / no local machine

This GitHub repository and its source verification checks run without your computer. For **interactive Codex + ECC**, use an authorized Codex CLI environment that you control. GitHub Codespaces could provide a browser-hosted terminal, but availability, computing quota, and charges depend on your GitHub plan; do not create one without reviewing the displayed limits. Codex Cloud and an ordinary ChatGPT conversation are not equivalent to a configured Codex CLI native plugin installation.

Do not automate login or run `codex` with a secret in GitHub Actions.

## 3. First safe experiment

Read [ECC_PILOT.md](ECC_PILOT.md) for a synthetic task and manual acceptance tests. Work on a new feature branch, ask Codex to use ECC's testing/review skills, and keep any merges manual. Record versions, usage, elapsed time, test results and PR evidence.

## Source provenance and scope

| Component | Origin | Trust/operation |
|---|---|---|
| ECC upstream | https://github.com/affaan-m/ECC | MIT; independent upstream |
| Pinned audit SHA | `90606c8315ee09cafc303515c5f33024db6b9882` (20 October 2026 upstream commit) | Read-only source checkout and static checks |
| Native ECC Codex plugin | Official upstream CLI instructions | **Not** installed by GitHub checkout |
| Lab code | This lab only | Synthetic, never imports CoPE-Core |
| ECC Tools GitHub App | Optional paid service | Not needed and not requested |

Audit SHA pin guarantees **which source was inspected**, not that running the upstream hooks, MCP servers, or arbitrary agent instructions is safe. Explicit user review remains necessary.
