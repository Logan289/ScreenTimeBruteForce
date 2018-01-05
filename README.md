# iOS Restriction Passcode Brute Force [![Python2.7](https://img.shields.io/badge/Python-2.7-orange.svg?style=flat-square)](https://www.python.org/downloads/release/python-2714/) ![OS](https://img.shields.io/badge/Tested%20On-Linux%20|%20macOS%20|%20Windows%20-green.svg?style=flat-square) ![iOS](https://img.shields.io/badge/Tested%20On%20iOS-9.3.5%20|%2010.0.1-green.svg?style=flat-square)

## Overview

This version of the application is written in Python, which is used to crack the restriction passcode of an iPhone/iPad takes advantage of a flaw in unencrypted backups allowing the hash and salt to be discovered.

![Restriction Passcode](https://cdn.igeeksblog.com/wp-content/uploads/2016/10/Tap-on-Restrictions-in-iOS-10-on-iPhone.jpg)

## Brute Force

1. Get the Base64 key and salt from the backup file in Computer.

2. Decode the Base64 key and salt.

3. Try from 1 to 9999 to with the pbkdf2-hmac-sha1 hash with Passlib

## How to Use

1. Make sure to use iTunes to backup the iOS device to computer

2. Run ioscrack.py

  `python ioscrack.py -a`

## Usage

```bash
usage: ioscrack.py [-h] [-v] [-a] [-i] [-b folder]

a script which is used to crack the restriction passcode of an iPhone/iPad
through a flaw in unencrypted backups allowing the hash and salt to be
discovered

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -a, --automatically   automatically finds and cracks hashes
  -i, --interactive     prompts user for input
  -b folder, --backup folder
                        where backups are located
```


3. If ioscrack couldn't find your back up please try to [find it manually](https://github.com/thehappydinoa/iOSRestrictionBruteForce/wiki/Manually-find-restrictions-hash-and-salt)

## DEPENDENCIES

This has been tested with Python 2.6 and 2.7.

Requires Passlib 1.7 Install with `pip install passlib`

## LICENSE

MIT License
