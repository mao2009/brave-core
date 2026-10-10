# Minimal private browser: experimental build preset

This directory is the first incremental implementation for a lean desktop
browser based on Brave Core. The **privacy contract is not yet fulfilled**.
In particular, disabling UI/product features does not remove all telemetry
implementations or their network paths.

## Current scope

- Uses Brave Origin's existing unbranded feature defaults and explicitly
  disables Rewards, Wallet, AI Chat and VPN using verified GN arguments.
- Preserves Brave Shields / ad blocking (no corresponding disable flag).
- Does **not** add an account, password manager, or custom telemetry service.
- Does **not** yet remove upstream Chromium metrics, Brave P3A, crash reporting,
  sync, account/sign-in plumbing, password-storage plumbing, or update-related
  requests. It also does not yet implement independent site identities.

## Building (Linux desktop, Chromium checkout required)

The Brave Core repository belongs at `src/brave` in a Chromium checkout.
Initialize that checkout with the upstream instructions (`pnpm run init`).
From `src/brave`:

```sh
mkdir -p ../out/Minimal
cp minimal-browser/args.gn ../out/Minimal/args.gn
# Generate from the Chromium src directory with depot_tools on PATH:
(cd .. && gn gen out/Minimal)
# Compile from the Chromium src directory:
(cd .. && autoninja -C out/Minimal brave)
```

The exact GN target may differ by upstream revision. Inspect generated targets
if `brave` is unavailable. Do not distribute the output as privacy-hardened
until the remaining audit is completed.

## Acceptance criteria for future increments

1. Remove telemetry *implementations and send paths*, not only preferences or
   command-line suppression. Include Chromium metrics, Brave P3A, crash uploads,
   referral/usage stats, and other usage reporting.
2. Keep security updates and ad-block rule updates functional. Document and
   test every necessary update endpoint separately from telemetry.
3. Remove Google/Brave account integration and password-storage features while
   retaining cookies, sessions and explicit site login/logout.
4. Implement independent website identities (isolated cookies/storage) without
   permanently duplicating the entire browser process per identity.
5. Validate build and runtime behavior with a real Linux build plus network
   capture and repeatable tests. Never infer privacy solely from GN flags.

## Preset sanity check

Run `python3 minimal-browser/test_preset.py` from the repository root.
This checks configuration invariants, **not** build or network behavior.

## Upstream maintenance architecture

**Rule: keep upstream mergeable, but keep unnecessary features out of the
resulting binary.** Source presence is not the same as compiled inclusion.

- Keep `master` a close upstream-tracking branch. Maintain product changes on
  separate branches and periodically rebase or merge them after upstream sync.
  Avoid destructive source-tree deletions and large mechanical rewrites.
- Prefer upstream supported GN build switches and conditional target dependencies.
  Where upstream lacks switches, add minimal isolated guards/stubs, rather than
  commenting out source at dozens of call sites.
- Prove feature removal with the generated GN dependency graph, linkage /
  symbols, runtime UI checks, and network tracing. An argument set to `false`
  alone is **not** proof of absence.
- Limit behavioral changes to product-specific integration seams; keep security
  patches, Chromium updates, certificates, DRM compatibility where permitted,
  and adblock filter updates distinct from analytics.
- Any upstream integration must rerun build, tests, and outbound-network audit
  before the fork can be released. Treat reintroduced optional features or
  telemetry paths as a regression.
- Keep site session/cookie persistence, while removing built-in credential
  storage and account synchronization in later audited steps.
