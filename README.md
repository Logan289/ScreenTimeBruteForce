# iOS Restriction Passcode Brute Force [![Python2.7](https://img.shields.io/badge/Python-2.7-orange.svg?style=flat-square)](https://www.python.org/downloads/release/python-2714/) 
![OS](https://img.shields.io/badge/Works%20On-Linux%20|%20macOS%20|%20Windows%20-green.svg?style=flat-square) ![iOS](https://img.shields.io/badge/Tested%20On%20iOS-9.3.5%20|%2010.0.1%20|%2011.2.1-green.svg?style=flat-square)

## Overview

This version of the application is written in Python, which is used to crack the restriction passcode of an iPhone/iPad takes advantage of a flaw in unencrypted backups allowing the hash and salt to be discovered.

![Restriction Passcode](https://cdn.igeeksblog.com/wp-content/uploads/2016/10/Tap-on-Restrictions-in-iOS-10-on-iPhone.jpg)

## DEPENDENCIES

This has been tested with Python 2

Requires Passlib 1.7+ Install with `pip install passlib`

## How to Use

1. Clone repository

    `git clone https://github.com/thehappydinoa/iOSRestrictionBruteForce && cd iOSRestrictionBruteForce`

2. Make sure to use [iTunes](https://www.apple.com/itunes/download/) or [libimobiledevice](https://github.com/libimobiledevice/libimobiledevice) to backup the iOS device to computer

3. Run `ioscrack.py` with automatic hash discovery option

    `python ioscrack.py -a`
  
4. If ioscrack couldn't find your back up please try to [find it manually](https://github.com/thehappydinoa/iOSRestrictionBruteForce/wiki/Manually-find-restrictions-hash-and-salt) then run `ioscrack.py` with interactive hash input option

    `python ioscrack.py -i`

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

## How It Works

1. Decode the Base64 key and salt.

2. Brute force pins from 1 to 9999 to with the pbkdf2-hmac-sha1 hash with Passlib

## LICENSE

MIT License
