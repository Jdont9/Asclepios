Asclépios AV (`fr.jd.asclepios`): personal fork of MaintainTeam/Hypatia, see the README for the full list of changes.

## Features
- Redesigned main screen: red theme (light and dark), rounded cards and a large Start / Stop scan button.
- New categorised Settings page (Network, Updates, Protection, Scans, Advanced) replacing the overflow menu.
- New "Last scan" card on the main screen: date, result (threats detected or none) and number of files checked.
- Automatic database updates: choose the frequency (every 6 h, 12 h, once a day, every 2 days, once a week) and the allowed network (Wi-Fi only, Wi-Fi + mobile data without roaming, or any network).
- Scan animation: the rod of Asclépios inside a rotating ring while a scan is running.

## Changes
- Scan options (apps, external storage, removable storage, deep scan, /system) are now remembered between launches.
- Enabling automatic updates now schedules a first check right away (it waits for an allowed network if needed).
- Defaults are unchanged: once a day, Wi-Fi only.

## Development Updates
- New `SettingsActivity` and `LastScan` helper; no new dependency.
- Added translations (en, fr) for the new strings; other languages fall back to English.
