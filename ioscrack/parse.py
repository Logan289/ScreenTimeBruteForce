from argparse import ArgumentParser
from os import listdir
from ioscrack.paths import isFolder, fixPath
from ioscrack.idevice import iDevice


def findHashes(path):
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
        print(str(e))
        print("Directory Not Found")
        return devices


def argparse():
    parser = ArgumentParser(
        prog="iOSCrack.py",
        description=
        "a script which is used to crack the restriction passcode of an iPhone/iPad through a flaw in unencrypted backups allowing the hash and salt to be discovered"
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
    return parser
