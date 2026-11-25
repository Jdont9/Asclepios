Asclépios AV (`fr.jd.asclepios`): personal fork of MaintainTeam/Hypatia, see the README for the full list of changes.

## New Features
- Device configuration check (optional, on by default): screen lock, USB and wireless debugging, developer options, encryption, security patch age, private DNS. Runs at the end of a full scan, no battery use.
- Active sensitive services: list of the apps that really have accessibility, notification access, device admin, a keyboard, overlay or install rights switched on; also used by the app risk analysis.
- Update watch: alert when an update gives an app new sensitive access (accessibility, admin, SMS, notifications, overlay, install).
- New app risk criteria: debuggable build, built for Android before 8.0, explicit cleartext traffic.
- Anti-rollback for the signed databases (signed manifest with a sequence number and the SHA-256 of each file).

## Hardening
- No backup or device transfer of the app data, https only (http:// only for .onion servers), screenshots blocked (switchable), anti-tapjacking on the threat list and its dialogs.

## Notes
- Needs the databases server to publish `hypatia-manifest.txt` for the anti-rollback check; servers without it keep working as before.
