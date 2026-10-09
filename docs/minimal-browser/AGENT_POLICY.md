# Minimal browser fork: agent policy

This document defines fork-specific requirements; upstream `.claude/CLAUDE.md` remains authoritative for established development procedures.

## Non-negotiable requirements
- No telemetry product, including opt-in telemetry: remove collection, buffering, identifiers, uploading, and UI/config controls for UMA, UKM, Brave P3A and related reporting wherever feasible. Do not confuse necessary local performance metrics for a test run with production telemetry. Never assert full removal without source/binary audits and runtime network tests.
- Preserve Chromium sandbox, site isolation, secure updates, TLS validation, WebAuthn, core web APIs, and current security patch uptake. Never reduce security merely to reduce memory.
- Keep Brave Shields/native blocking; verify filter update behavior and YouTube content playback. Do not claim guaranteed ad blocking across server-side/DRM content.
- No browser-account sign-in, Google/Brave sync, or browser-hosted cloud profile. Website sign-in/OAuth must remain functional.
- Preserve persistent site cookies/storage and sign-in across restart when permitted by the site; do not include a password manager, saved passwords, password autofill or payment/address autofill.
- Keep compatibility with GitHub, Redmine, ChatGPT, YouTube and Prime Video (including Widevine support conditional on legal distribution and availability); never ship proprietary DRM binaries without rights.
- Prefer smallest durable patch set against upstream Brave/Chromium. Keep upstream attribution, licenses and notices.
- Containerized sessions are a design experiment, not a pre-committed architecture; measure memory cost against Chromium profiles before adoption.

## Working rules
- Work in a dedicated feature branch; never make speculative changes directly to master.
- For each change: reference an Issue, explain impact on memory, performance, privacy, compatibility, licensing and upstream merge burden.
- Record baseline, test commands, environment, reproducible pass/fail evidence, and limitations on PRs/issues. Never invent benchmark results.
- Require build, relevant tests, and runtime smoke tests where feasible before merging. Explicitly label unavailable Windows/Linux/Widevine/DRM evidence.
- Prefer feature deletion at build time over merely hiding UI; guard every deletion against breaking dependent services.
- Preserve platform parity wherever viable; document exceptions.

## Proposed release gates
1. Network capture from first launch, idle, page navigation and restart: no application telemetry endpoints. Enumerate justified traffic (filter updates, website requests, security services, DRM, etc.).
2. Fresh profile: no password-save prompts, saved credential store, browser account or sync entry point.
3. Persistent profile: login survives restart subject to site policies; separate-profile dual sign-ins work.
4. GitHub PR/issue editing, Redmine forms, ChatGPT stream/upload, YouTube playback/blocking and Prime Video playback are verified.
5. Repeatable memory/startup baseline versus matched Brave version and workloads; report peak/steady RSS/PSS and process counts.
6. Sandbox/site isolation remain enabled, security updates remain maintainable.
