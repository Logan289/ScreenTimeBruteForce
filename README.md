# iOS Restriction Passcode Brute Force
[![Python2.7](https://img.shields.io/badge/Python-2.7-orange.svg?style=flat-square)](https://www.python.org/downloads/release/python-2714/) ![OS](https://img.shields.io/badge/Works%20On-Linux%20|%20macOS%20|%20Windows%20-green.svg?style=flat-square) ![iOS](https://img.shields.io/badge/Tested%20On%20iOS-9.3.5%20|%2010.0.1%20|%2011.2.1-green.svg?style=flat-square) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![Code Climate](https://img.shields.io/codeclimate/maintainability/thehappydinoa/iOSRestrictionBruteForce.svg?style=flat-square)](https://codeclimate.com/github/thehappydinoa/iOSRestrictionBruteForce)

## Overview

This version of the application is written in Python, which is used to crack the restriction passcode of an iPhone/iPad takes advantage of a flaw in unencrypted backups allowing the hash and salt to be discovered.

![Restriction Passcode](docs/ios-restrictions.jpeg)

## DEPENDENCIES

This has been tested with [Python 2.7](https://www.python.org/downloads/release/python-2714/)

Requires [Passlib](https://passlib.readthedocs.io/en/stable/) Install with `pip install passlib`

## How to Use

1. Clone repository

    ```bash
    git clone https://github.com/thehappydinoa/iOSRestrictionBruteForce && cd iOSRestrictionBruteForce
    ```

2. Make sure to use [iTunes](https://www.apple.com/itunes/download/) or [libimobiledevice](https://github.com/libimobiledevice/libimobiledevice) to backup the iOS device to computer

3. Run `ioscrack.py` with automatic hash discovery option

    ```
    python ioscrack.py -a
    ```

4. If ioscrack couldn't find your back up please try to [find it manually](https://github.com/thehappydinoa/iOSRestrictionBruteForce/wiki/Manually-find-restrictions-hash-and-salt) then run `ioscrack.py` with interactive hash input option

    ```
    python ioscrack.py -i
    ```

![GIF](docs/ioscrack.gif)

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

Done by using the [pbkdf2](http://www.ietf.org/rfc/rfc2898.txt) hash with the Passlib python module

1. Trys the [top 20 four-digit](http://www.datagenetics.com/blog/september32012/index.html) pins

2. Trys birthdays between 1900-2017

3. Brute force pins from 1 to 9999

## How to Protect Against

1. Encrpyt backups

2. Backup only on trusted computers

## Acknowledgments

- [yuejd](/yuejd)

## LICENSE

[MIT License](LICENSE)
