# ECC + Codex pilot — synthetic multi-role exercise

## Goal
Measure whether ECC skills improve a small coding task without touching any of the owner's other projects. The public `CoPE-ECC-Lab` repository is the only authorized working scope.

## Exercise

Create a fresh branch. Ask Codex (with the ECC plugin visibly installed in `/plugins`):

> Work ONLY in FS-GitmeHub/CoPE-ECC-Lab. Read AGENTS.md. Implement `plan_waves(tasks)` in `lab_demo/pipeline.py`: given the same dependency graph accepted by `plan_tasks`, return deterministic layers of tasks that can run in parallel, sorted lexicographically within each layer. Reject the same invalid inputs and cycles. Write tests FIRST, implement with no third-party runtime dependencies, run the full suite, and request an independent review. Use ECC skills for test-driven development and verification if they are installed. Do not modify other projects, access secrets, or merge automatically. Report actual executed agent roles and evidence; do not claim a multi-agent swarm unless it ran.

## Evidence to record in the PR

| Field | Must contain |
|---|---|
| Codex version | Actual CLI `codex --version` output |
| ECC version | `codex plugin list --json`, without secrets |
| Execution model | Which tools/roles actually ran, not agent counts in catalog |
| Correctness | Full unit-test log, expected and observed behavior |
| Quality | Reviewer findings, fixes and outstanding concerns |
| Time | Start/end wall-clock and number of iterations |
| Cost | Reported usage if available; mark unavailable honestly |
| Source provenance | Links to changed files and any third-party material |
| Merge | Manual only after approval |

## Controls

Avoid contacting endpoints other than the GitHub repository and the configured model provider during the interactive task. No access to CoPE-Core, no attempts to run other owner's projects, no automatic release or deployment. The benchmark is about agent workflow, not CoPE's 100x compression objective.

Until a real Codex+ECC execution log exists, the result is **NOT VERIFIED**.
