Asclépios AV (`fr.jd.asclepios`): personal fork of MaintainTeam/Hypatia, see the README for the full list of changes.

## New Features
- Stalkerware detection: installed apps and APK files are compared (package name and signing certificate) with a GPG-signed list built from the Stalkerware Indicators of the Echap association. On by default. **Update the databases once** to download the list. Uninstalling warns that the person who installed the stalkerware may notice.
- App risk analysis (heuristic): a score from the manifest (accessibility service, device admin, notification access, SMS, overlay, app installation, microphone, call log...), a missing launcher icon, an unknown install source and a changed signer. Only risky combinations raise an alert and every reason is listed. On by default.
- Downloaded APK watcher: an `.apk` landing in storage is analysed before you install it, with a notification saying whether it is dangerous or just installable. Needs the realtime scanner. On by default; `.apks`/`.xapk`/`.apkm` bundles are reported but not analysed.
- Links: the link scanner and the file URL scan share the same rules (domain and parent domains, Unicode and punycode spellings), and flag domains that mix look-alike letters from several alphabets (for example a Cyrillic "а" in a Latin name).
- Three new switches in Settings → Protection to turn each feature off.

## Bug Fixes
- Link scanner: screen text is lowercased with a fixed locale, so ASCII domains are no longer missed on devices set to Turkish ("I" became "ı").

## Notes
- The stalkerware list needs the matching HypatiaDatabases release (`hypatia-stalkerware-bloom.bin`); without it the feature stays idle and nothing else changes.
- The app risk analysis is a heuristic: legitimate apps (password managers, screen readers) can resemble risky profiles. Use "Always ignore" on a threat you trust.
