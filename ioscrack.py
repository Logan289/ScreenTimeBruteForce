#!/usr/bin/env python3
from builtins import input

from ioscrack.parse import argparse, findHashes
from ioscrack.cli import prompt
from ioscrack.crack import crackHashes


def handleArgs():
    parser = argparse()
    args = parser.parse_args()
    if args.automatically and not args.cli:
        crackHashes(findHashes())
    if args.cli:
        prompt()
    if args.backup:
        crackHashes(findHashes(path=args.backup))
    if args.test:
        crackHashes(findHashes(path="tests"))
    if not any(vars(args)[key] for key in vars(args).keys()):
        parser.print_help()


def main():
    try:
        print("\n iOSRestrictionBruteForce")
        print(" Written by thehappydinoa \n")
        handleArgs()
        input("Press [enter] to exit")
    except KeyboardInterrupt:
        print("Exiting...\r"),
        exit(0)


if __name__ == "__main__":
    main()
