#!/usr/bin/env python3
# iOSRestrictionBruteForce Version 2.1.0
from builtins import input

from ioscrack.parse import argparse, findHashes
from ioscrack.cli import prompt
from ioscrack.crack import crackHashes
from ioscrack.test import testAll


def handleArgs():
    parser = argparse()
    args = parser.parse_args()
    if args.backup:
        crackHashes(findHashes(path=args.backup))
    if args.automatically:
        crackHashes(findHashes())
    elif args.cli:
        prompt()
    elif args.test:
        print("Running unittests")
        testAll()
    elif not any(vars(args)[key] for key in vars(args).keys()):
        parser.print_help()


def main():
    try:
        print("\n iOSRestrictionBruteForce")
        print(" Written by thehappydinoa \n")
        handleArgs()
        # input("Press [enter] to exit")
    except KeyboardInterrupt:
        print("Exiting...\r"),
        exit(0)


if __name__ == "__main__":
    main()
