# Verification

## Read when

- changing build, test, lint, or CI behavior
- preparing final task verification

## Stable context

- Fast commands are configured in `.harness.toml` under `verification.fast`.
- Full delivery commands are configured in `.harness.toml` under `verification.full`.
- Record the exact commands and results in the active Journal before archival.

## Update when

- package scripts, task runners, CI workflows, or required delivery checks change
