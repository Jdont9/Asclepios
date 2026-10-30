#!/usr/bin/env python3
"""Lists the SHA-256 of every APK published by F-Droid (and optionally IzzyOnDroid / the F-Droid archive).

Output: one lowercase SHA-256 per line, sorted, without duplicates. Feed it to the generator of the
signature-database repository to build hypatia-whitelist-sha256-bloom.bin.

Usage:
  python3 tools/fdroid_hashes.py > fdroid.sha256                 # main repo
  python3 tools/fdroid_hashes.py --archive --izzy > all.sha256   # + archive + IzzyOnDroid
  python3 tools/fdroid_hashes.py --index some-index-v2.json      # use a local index instead (no download)

The index files are signed (index-v2.json.asc for F-Droid): verify them if the list feeds a whitelist.
"""
import argparse
import json
import re
import sys
import urllib.request

REPOS = {
    "fdroid": "https://f-droid.org/repo/index-v2.json",
    "archive": "https://f-droid.org/archive/index-v2.json",
    "izzy": "https://apt.izzysoft.de/fdroid/repo/index-v2.json",
}
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def hashes_from_index(index):
    """index-v2 layout: packages -> <appId> -> versions -> <sha256 of the APK> -> file.sha256"""
    found = set()
    for package in index.get("packages", {}).values():
        for key, version in package.get("versions", {}).items():
            candidate = (version.get("file", {}).get("sha256") or key).lower()
            if HEX64.match(candidate):
                found.add(candidate)
    return found


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", action="store_true", help="also read the F-Droid archive")
    parser.add_argument("--izzy", action="store_true", help="also read IzzyOnDroid")
    parser.add_argument("--index", action="append", default=[], help="local index-v2.json (repeatable)")
    args = parser.parse_args()

    indexes = []
    if args.index:
        for path in args.index:
            with open(path, encoding="utf-8") as f:
                indexes.append(json.load(f))
    else:
        urls = [REPOS["fdroid"]]
        if args.archive:
            urls.append(REPOS["archive"])
        if args.izzy:
            urls.append(REPOS["izzy"])
        for url in urls:
            print("downloading " + url, file=sys.stderr)
            with urllib.request.urlopen(url, timeout=120) as response:
                indexes.append(json.load(response))

    all_hashes = set()
    for index in indexes:
        all_hashes |= hashes_from_index(index)
    for h in sorted(all_hashes):
        print(h)
    print(f"{len(all_hashes)} hashes", file=sys.stderr)


if __name__ == "__main__":
    main()
