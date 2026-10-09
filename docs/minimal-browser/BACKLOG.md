# Implementation backlog

GitHub Issues are currently disabled on this fork (HTTP 410). These are issue-ready work items; migrate each to an Issue when Issues are enabled. No work below is claimed implemented.

| ID | Phase | Work item | Acceptance evidence |
|---|---|---|---|
| MB-001 | M0 | Reproducible Windows/Linux Brave checkout/build and upstream baseline | Build commands, versions, cold/warm memory/process/CPU timing for fixed workloads |
| MB-002 | M1 | Remove telemetry including UMA, UKM, P3A and uploaders | Source/binary audit, clean first-launch/idle/restart traffic traces, no telemetry feature or opt-in UI |
| MB-003 | M1 | Remove browser-account sync, password manager, autofill and unnecessary Brave services | Source/build audit; website logins, WebAuthn, session persistence remain working |
| MB-004 | M2 | GitHub, Redmine, ChatGPT compatibility and session persistence | Functional cross-platform smoke matrix for editing, upload, streaming, restart |
| MB-005 | M2 | Shields, YouTube and Prime Video compatibility | Filter update, playback/codec/GPU, CDM feasibility/license, tested limitations |
| MB-006 | M3 | Lazy tab restore and memory-pressure discard | RSS/PSS and load-time benchmark; active media/forms/streams not discarded |
| MB-007 | M4 | Multi-account profiles and experimental tab containers | Isolation/cookie persistence test, incremental memory overhead, architecture decision |
| MB-008 | M3 | Minimal browser UI and build-time dead-service removal | Screenshots, accessible navigation, quantified binary and runtime impact |

Each work item requires a focused feature branch, PR, test evidence, upstream diff impact and regression risks. Do not merge solely on documentation completion.

## Immediate sequence
1. MB-001, then MB-002 and MB-003 in independently reviewable PRs.
2. MB-004 and MB-005 establish compatibility gates before aggressive runtime changes.
3. MB-006 and MB-008 follow measured hotspots.
4. MB-007 only after profiling confirms acceptable memory overhead.
