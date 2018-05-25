from argparse import ArgumentParser
from os import listdir

from ioscrack.paths import isFolder, fixPath
from ioscrack.idevice import iDevice
from ioscrack.paths import backupPaths


def findHashes(path=backupPaths()):
    devices = []
    path = fixPath(path)
    print("\nLooking for backups in %s..." % path),
    try:
        backup_dir = listdir(path)
        if len(backup_dir) > 0:
            print("Directory Found")
            for bkup_dir in backup_dir:
                print("Found %s" % bkup_dir)
                device = iDevice(path + bkup_dir)
                devices.append(device)
            return devices
        else:
            print("Unable to find backups in %s" % bkup_dir)
    except OSError as e:
        # print(str(e))
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
        type=lambda x: isFolder(parser, x))
    parser.add_argument(
        "-t", "--test", help="cracks devices in `tests/`", action="store_true")
    return parser
