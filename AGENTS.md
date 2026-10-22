# ECC lab agent rules

## Scope
Only `FS-GitmeHub/CoPE-ECC-Lab` is within this experiment's scope. Never clone, modify, push, inspect secrets from, or run code from CoPE-Core or any other user project as part of these tests.

## Roles (requested; not claims of active agents)
- **Coordinator:** decomposes work; establishes acceptance criteria and permissions.
- **Implementer:** changes isolated lab code in a feature branch.
- **Reviewer:** independently inspects diff, licenses, provenance and security.
- **Verifier:** executes synthetic, reproducible tests and reports evidence.

## Mandatory controls
- Keep PR review and merge manual by default.
- Do not expose tokens, keys, credentials, or private content.
- Do not change GitHub repository settings or app permissions without the owner's approval.
- Do not enable internet deployment, billing, or external writes as a side effect of tests.
- Do not assert that ECC agents are running unless runtime evidence exists.
- Keep dependency licenses and source/provenance in the PR.
- No production CoPE claims may be based on the synthetic lab example.
