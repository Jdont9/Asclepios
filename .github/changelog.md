Asclépios AV (`fr.jd.asclepios`): personal fork of MaintainTeam/Hypatia, see the README for the full list of changes.

## New Features
- Phishing domains: the malicious-domain database now also includes the active phishing domains of Phishing.Database, filtered by the same allowlist (Tranco top sites + MISP warninglists) as the other extra sources. The link scanner and the malicious URL scan in files use them once the databases are updated. No new setting.

## Notes
- This release contains no change to the app code: it only aligns the version with the databases. The phishing domains reach every installed version through the normal database update.
- 4.7.0 features (stalkerware detection, app risk analysis, downloaded APK watcher, look-alike domain detection) are unchanged.
