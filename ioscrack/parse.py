from argparse import ArgumentParser
from os import listdir

from ioscrack.paths import isFolder, fixPath
from ioscrack.idevice import iDevice
from ioscrack.paths import backupPaths


def findHashes(path=backupPaths(), test=False):
    devices = []
    path = fixPath(path)
    if not test:
        print("\nLooking for backups in %s..." % path),
    try:
        backup_dir = listdir(path)
        if len(backup_dir) > 0:
            if not test:
                print("Directory Found")
            for bkup_dir in backup_dir:
                if not test:
                    print("Found %s" % bkup_dir)
                device = iDevice(path + bkup_dir)
                devices.append(device)
            return devices
        else:
            if not test:
                print("Unable to find backups in %s" % bkup_dir)
    except OSError as e:
        if not test:
            print("Directory Not Found")
        return devices


def argparse():
    parser = ArgumentParser(
        prog="iOSCrack.py",
        description="a script to crack the restriction passcode of an iDevice"
    )
    parser.add_argument(
        "-a",
        "--automatically",
        help="automatically finds and cracks hashes",
        action="store_true")
    parser.add_argument(
        "-c", "--cli", help="prompts user for input", action="store_true")
    parser.add_argument(
        "-b",
        "--backup",
        help="where backups are located",
        metavar="folder",
        type=lambda path: isFolder(path, parser=parser))
    parser.add_argument(
        "-t", "--test", help="runs unittests", action="store_true")
    return parser
