# Minimal Brave-based browser — initial requirements

Status: design baseline, not implemented. Parent project: brave/brave-core.

## Product scope
Desktop-first (Windows and Linux), Chromium-compatible browser optimized for minimal runtime memory and maintainability. Simplify UI even when it trades customization for resources. Target: GitHub, Redmine, ChatGPT, YouTube and Amazon Prime Video. Do not introduce proprietary account infrastructure.

## Mandatory
- Native Brave Shields and tracker blocking, with filter refresh.
- YouTube video/live playback, captions, compatible codecs and hardware acceleration where supported; ad-blocking behavior must be tested, not guaranteed for every ad format.
- Prime Video playback requiring legally available Widevine CDM, codecs and protected media path; treat Linux/platform restrictions as a release risk.
- Full website authentication: cookies, persistent storage, OAuth/SSO, WebAuthn and safe session restoration; session expiration remains controlled by the website.
- Multiple simultaneous logins to the same website, initially via distinct Chromium profiles; evaluate lighter container isolation later.
- No telemetry feature whatsoever (not even opt-in), browser-account sign-in, browser sync, saved-password store, password autofill, payment/address autofill.
- Preserve sandbox, site isolation, certificates, security updates, browser privacy controls and core APIs needed by target websites.

## Candidate removals after dependency audit
Brave Rewards, Wallet, Leo, News, VPN, unnecessary onboarding UI, cosmetic UI, suggestions/prefetch, background app persistence. Removal must target shipped code/services, not just visible controls. Do not remove necessary privacy/security features to meet footprint targets.

## Memory model
- Lazy restore non-active tabs; freeze/discard eligible tabs under pressure.
- Protect active audio/video, user forms, downloads, media DRM sessions and potentially active ChatGPT output from accidental discard.
- Treat any numeric reduction goal as hypothesis until benchmarked. Distinguish browser overhead from the cost of web apps.
- Benchmark per-profile cost of dual accounts versus experimental StoragePartition approach. Container architecture is not yet selected.

## Privacy and network
Application-level telemetry and its collection/upload machinery are forbidden. Document functional network traffic and keep it minimal. External website, DNS, certificate, filter update, security service and DRM traffic must be reviewed separately; prohibition on telemetry must not disable necessary protective functions. Locally generated, explicitly requested development diagnostics are not product telemetry.

## Delivery milestones
M0: reproducible upstream build and benchmark methodology.
M1: privacy and feature removal with proofs.
M2: compatibility and session persistence.
M3: memory controls and benchmarks.
M4: optional lightweight container experiment.
