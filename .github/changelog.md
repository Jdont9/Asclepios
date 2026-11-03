Asclépios AV (`fr.jd.asclepios`): personal fork of MaintainTeam/Hypatia, see the README for the full list of changes.

## New Features
- Scan a folder or a file: two new entries in the home screen menu ("Scan a folder…", "Scan a file…") scan only what you pick, ignoring the Settings scan options.
- Auto-update: choose the time of day of the check (daily or less frequent updates). The update now also stays within the chosen network policy when a job is started by its deadline.
- Share several files at once to Asclépios AV (previously a single file).

## Bug Fixes
- Sharing a file to the app now actually scans it: the scan runs from the main screen (progress and result are shown there) and waits for the signature database if it is still loading after a cold start, instead of silently scanning nothing.
- Temporary copies made for shared-file scans are all deleted after the scan (only the first one was).
