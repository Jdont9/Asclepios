Asclépios AV (`fr.jd.asclepios`): personal fork of MaintainTeam/Hypatia, see the README for the full list of changes.

## Bug Fixes
- The database loading state is always released if a load is cancelled or fails, and a partially loaded database is reloaded instead of being treated as loaded.
- README: troubleshooting entry about periodic database reloads (process killed by Android, battery optimization).
- The persistent notification opens the app when tapped and shows the signature count again (link scanner and realtime scanner).
- The log can be scrolled back up again on the home screen.
