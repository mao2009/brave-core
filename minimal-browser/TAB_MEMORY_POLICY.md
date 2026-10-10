# Tab memory management design (planned, not implemented)

## Goals
- Reduce per-tab resident memory and browser idle overhead without compromising Chromium Site Isolation or upstream mergeability.
- Performance target: usable 10–20 tabs on an 8 GiB Linux desktop, to be measured with representative workloads; **not a guarantee or fixed memory budget**.
- Preserve ad blocking, session cookies/logins, security updates and normal foreground page behavior.
- Favor Chromium's existing tab lifecycle, performance manager and memory-pressure mechanisms before introducing fork-specific code.

## Policy presets (initial candidates; tune after measurements)

| Mode | Consider freeze after background | Consider discard after background |
| --- | --- | --- |
| Gentle | 10 min | 60 min |
| Balanced (default candidate) | 3 min | 20 min |
| Aggressive | 1 min | 5 min |

These are eligibility thresholds, not unconditional timers. Freeze need not free memory; discard releases the page's in-memory state and reloads it on activation. Respect Chromium's eligibility logic and OS memory pressure.

## Hard safety and UX requirements
- Never automatically discard the active tab.
- Protect tabs with audio/video capture, active media playback, downloads, calls or similar ongoing activity, and allow explicit user protection.
- Protect potentially unsaved form edits and other valuable unsaved state where detectable. If uncertain, prefer retention; explain that JavaScript application state is not always detectable or recoverable.
- Keep website isolation and account-container storage boundaries: do **not** bypass Site Isolation or force unrelated sites into shared renderers to save memory.
- Explicit multi-login/container identities must have separated cookies/storage; process reuse cannot merge their identities.
- Do not disable important security controls or adblock lists.
- Provide per-site opt-out and visible freeze/discard diagnostics; avoid invasive telemetry. All measurements stay local.

## Implementation stages
1. Baseline: measure private memory/RSS/PSS, process counts, tab reload behavior, idle CPU, cold/warm startup and responsiveness for 1, 5, 10 and 20 tabs under 8 GiB and 16 GiB Linux test environments.
2. Integrate policy with existing Chromium lifecycle APIs using a minimal upstream-friendly integration seam.
3. Add protected-tab rules and UI controls, with regression tests for login retention, edits, media, WebRTC, downloads and container isolation.
4. Adjust background scheduling and page cache/image budgeting only with verified benefits, not blanket limits.
5. Enforce performance regressions in CI using robust baselines. Recheck all policies after upstream Brave/Chromium updates.

## Verification
- Confirm GN build and functional tests on Linux; record Chromium/Brave commit IDs.
- Use local-only benchmarks. Check memory delta and restoration cost, not RSS alone.
- Test crash isolation and site security. Confirm no telemetry send-paths are reintroduced.
- Keep this entirely separate from upstream source tree deletions. Presets and compact patches are preferred.

## Scope
This file records agreed architecture only. None of the tab lifecycle policy, exclusions, UI or benchmarks has been implemented yet.
