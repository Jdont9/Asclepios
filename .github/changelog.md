Asclépios AV (`fr.jd.asclepios`): personal fork of MaintainTeam/Hypatia, see the README for the full list of changes.

## Features
- New "Active threats" line on the home screen. Tapping it opens the list of threats that are still active.
- Threat details: for each threat, the reasons it was flagged (signature database match with the hash type, file, SHA-256, date), with VirusTotal lookup, delete / uninstall and ignore actions.
- Ransomware decoy files (opt-in, Settings → Protection): bait files in Download, Documents, Pictures and DCIM. If an app modifies, renames or deletes one, you get an alert and the bait is put back.
- Mass rename detection (opt-in, Settings → Protection): alerts when many files get a suffix added to their name within seconds.
- Malicious URL scan in files (opt-in, Settings → Scans): checks the web addresses inside APKs and text files against the malicious-domain database. Needs the link scanner.
- Trusted files: "Always ignore" on a threat adds the file's SHA-256 to a list of files that are never reported again. The list can be imported from a text file (any 64-character hex hashes found are used), viewed and cleared in Settings → Advanced.
- NSRL import (opt-in, manual): Settings → Advanced → NSRL list imports the SHA-256 of known Android APKs prepared from the NIST NSRL (tutorial in the README). Kept apart from the trusted files list, limited to 3 million fingerprints, replaced by a new import and removable.
- Online whitelist of known-good files (Settings → Updates, on by default): downloaded and loaded with the signature databases to reduce false positives.

## Changes
- Threats are now remembered until the file is deleted, the app is uninstalled or the threat is ignored.
- "Ignore" on a threat asks whether to ignore it this time or always.

## Development Updates
- New `ThreatStore`, `RansomwareGuard`, `ThreatsActivity`, `UrlScanner` and `Whitelist`; no new dependency.
- The online whitelist is a new signed bloom file, `hypatia-whitelist-sha256-bloom.bin`, in the same format as the other databases. A server that does not publish it just logs a 404.
