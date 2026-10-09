# Compatibility and efficiency test matrix

All entries are **unverified** until run on actual build and platform. Test on Windows and Linux, recording GPU, drivers, codec/CDM availability and exact Brave/Chromium revision.

| Area | Acceptance scenario |
|---|---|
| GitHub | Two profiles signed in simultaneously; issue editing, PR diff, review and OAuth where applicable |
| Redmine | Session survives browser restart (server permitting); edit forms and attachment uploads |
| ChatGPT | Sign-in, streaming responses, long sessions, uploads and background-tab return |
| YouTube | Playback, seek, captions, live, hardware decode; ad-block behavior and filter updates |
| Prime Video | Sign-in, protected video, audio/video synchronization, CDM availability, error logging without telemetry |
| Password | No save prompts, manager UI, password autofill or persistence in product-owned password store |
| Privacy | First-launch/idle/restart network capture; no telemetry payloads or endpoints; justified service traffic documented |
| Isolation | Sandboxing and site isolation enabled; multiple accounts do not cross-leak cookies/site state |
| Footprint | Cold/warm start, idle 1/3/10 tabs, pressure handling, 2-profile overhead; record RSS/PSS, CPU and load time |

Use matched workload, clean and warmed profiles, repeated runs, and compare with same-revision upstream Brave. Preserve raw traces locally for reproducibility; do not upload user browsing data.
