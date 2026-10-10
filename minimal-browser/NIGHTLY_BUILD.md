# Linux nightly build

Workflow: `.github/workflows/minimal-browser-nightly.yml`

- Scheduled daily at **03:15 JST** (18:15 UTC). GitHub schedule is best-effort; it can be delayed.
- `workflow_dispatch` allows manual runs.
- Only runs automatically after the workflow is merged into the repository **default branch** (`master`).
- Uses the minimal-browser GN preset and uploads build logs / manifest, **not** a browser release. No binary publishing until telemetry removal and runtime audit pass.
- A failed run must be inspected before treating a newer upstream revision as supported.

## Required dedicated runner

Register an **isolated, trusted** GitHub Actions self-hosted Linux x86-64 runner
with labels `self-hosted`, `linux`, `x64`, `brave-nightly`.

Provision and verify before dispatch:
- Linux Chromium/Brave build prerequisites, `git`, `node` (compatible with `package.json`), `pnpm`, `python3`, `gn`, `autoninja`, and Chromium `depot_tools` on PATH
- Substantial available storage (plan for **hundreds of GB** including build output), RAM and swap appropriate for Chromium compilation
- Outbound network access to fetch Chromium and dependencies
- Runner account without production credentials; dedicated to this trusted repo, never used for untrusted pull request builds

The workflow initializes Chromium sources on every run and can download many GB.
It does not yet set up an optimized shared Chromium checkout or incremental cache.
Follow upstream environment prerequisites and actual resource usage for sizing.

## Upstream synchronization

Nightly currently builds the Brave Core revision from the default branch.
It does **not** automatically merge updates from `brave/brave-core`.
Upstream updates should be separately fetched, reviewed and integrated,
then built and audited by this workflow. Automatic unreviewed upstream merges
must not be mistaken for verified privacy-safe releases.

## Manual verification

Actions → Minimal browser nightly (Linux) → Run workflow.
Confirm `gn gen`, `autoninja`, and upload-artifact success.
The Python preset check alone is not a binary/runtime privacy test.
