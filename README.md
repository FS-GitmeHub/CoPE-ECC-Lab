# CoPE-ECC-Lab

Isolated, independent laboratory to evaluate **free, MIT-licensed ECC open source with OpenAI Codex**. No CoPE-Core or other owner project is copied or tested here.

## Current verified state

- 8 dependency-free synthetic Python tests: GitHub Actions **Smoke checks**.
- Pinned public ECC upstream (`90606c8315ee09cafc303515c5f33024db6b9882`): GitHub Actions **ECC open-source source audit**.
- Both checks succeeded on the experimental branch. See **Actions** for evidence.
- The paid **ECC Tools GitHub App is not required**.
- The native ECC Codex plugin has **not** been installed into a Codex CLI environment by these GitHub changes.
- **No AI agents have been launched** by this setup.

## Start here

1. [Free ECC + Codex setup](docs/START_FREE_ECC_CODEX.md) — official marketplace installation and isolation instructions, including Windows PowerShell.
2. [Synthetic first agent pilot](docs/ECC_PILOT.md) — a proposed role-based task and evidence checklist.
3. [Lab evaluation metrics](docs/EVALUATION.md) — what counts as verified.
4. [Agent safety rules](AGENTS.md) — strict scope and manual authorization.

## Checks

Run the existing synthetic test suite locally:

```sh
python3 -m unittest discover -s tests -v
```

The source audit checks out a **pinned authentic ECC GitHub commit** and inspects its manifest/asset paths, license, and Git SHA without running upstream scripts. The source audit is **not** proof of ECC security or successful agent operation.

## Cost and scope

ECC is open-source, but Codex usage remains subject to the owner's ChatGPT/Codex plan limits or independently selected API billing. GitHub Actions usage is subject to GitHub plan limits. Do not purchase ECC Tools or introduce billing without owner approval.

**CoPE-Core, cope-ci-audit and any other user projects remain out of scope**. Do not give ECC access to them. PR merges are manual.

This lab tests AI development workflow effectiveness; it does **not** validate CoPE's 100x compactness target.
