# CoPE-ECC-Lab

An isolated, independent **ECC + OpenAI Codex evaluation laboratory**. No CoPE-Core code or any other user project is copied or tested here.

## Verified setup

- The laboratory is in `FS-GitmeHub/CoPE-ECC-Lab`, independent from `CoPE-Core`.
- The repository contains a small, dependency-free synthetic Python task scheduler with eight unit tests.
- GitHub Actions workflow: `.github/workflows/smoke.yml` (**Smoke checks**).
- The ECC GitHub App is **not installed** by these repository files.
- The ECC Codex plugin is **not installed** by these repository files.
- No AI agents are running as a result of uploading this starter.

## Quick checks

From the repository root:

```sh
python3 -m unittest discover -s tests -v
```

See **Actions → Smoke checks** in this repository to inspect the independent hosted run and its logs.

## ECC reference and integration

- Source: https://github.com/affaan-m/ECC
- ECC GitHub App: https://github.com/apps/ecc-tools

### Integration phases

1. **Smoke-check phase** — confirm that GitHub Actions runs and all eight tests pass.
2. **Permission phase (owner approval required)** — if using the ECC GitHub App, install it only for `CoPE-ECC-Lab`; review its authorization and avoid granting access to `CoPE-Core`.
3. **Codex phase** — separately review and install the ECC plugin using its current official instructions in an isolated, authorized development environment. Installing a GitHub App alone does not launch a 64- or 71-agent swarm.
4. **Evidence phase** — run a synthetic multi-role coding task in an isolated branch; record agent/harness versions, timestamps, logs, costs, PR review and test evidence.
5. **Go/no-go review** — decide whether ECC contributes to speed, quality and auditability before considering integration elsewhere.

## Guardrails

- Do not copy, analyze or modify `CoPE-Core`, `cope-ci-audit` or any other user project.
- No automated merges, unreviewed external scripts, secrets, deployments, billing or unrestricted agent permissions.
- Keep testing and PR approval under human control.
- Read `AGENTS.md` for coordination rules and `docs/EVALUATION.md` for the benchmark plan.

This is an **orchestration laboratory**, not evidence that CoPE has achieved its fixed 100× compactness objective.
