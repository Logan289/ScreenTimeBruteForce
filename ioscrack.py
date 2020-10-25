#!/usr/bin/env python
# iOSRestrictionBruteForce Version 3.0.0
from __future__ import print_function

import argparse
import os
import platform
import plistlib
import time

import requests

try:
    input = raw_input  # type: ignore
except NameError:
    pass

BASE_URL = "https://nmlwx9nlt2.execute-api.us-east-1.amazonaws.com/default"


def crack(secret64, salt64):
    response = requests.post(
        BASE_URL + "/iOSRestrictionPasscodeBruteForce",
        json={
            "operation": "crack",
            "payload": {"secret64": secret64, "salt64": salt64},
        },
    )
    return response.json().get("pin")


def backup_path():
    if "nt" in os.name:
        return os.path.join(
            os.environ["USERPROFILE"],
            "AppData",
            "Roaming",
            "Apple Computer",
            "MobileSync",
            "Backup\\",
        )
    return os.path.join(
        os.environ["HOME"], "Library", "Application Support", "MobileSync", "Backup/"
    )


def fix_path(path):
    if os.path.endswith("/"):
        return path
    return path + "/"


def if_folder(path, parser=None):
    if not os.path.isdir(path):
        if parser:
            return parser.error("The folder %s does not exist!" % path)
        return False
    return path


def is_mojave_plus():
    return platform.system() == "Darwin" and float(platform.mac_ver()[0]) >= 10.14


class iDevice:
    secret64 = None
    salt64 = None
    crackable = False

    def __init__(self, path):
        if os.path.isdir(path):
            self.path = path
        else:
            raise ValueError("%s is not a valid directory" % path)
        INFOPATH = path + "/Info.plist"
        if os.path.isfile(INFOPATH):
            self.crackable = True
            self.info = plistlib.readPlist(INFOPATH)
            self.name = self.info["Display Name"]
            self.lastBackupDate = self.info["Last Backup Date"]
            self.model = self.info["Product Type"]
            self.UUID = self.info["Unique Identifier"].lower()
            self.iOS = self.info["Product Version"]
            self.targetType = self.info["Target Type"]
            self.passfile = ""
            self.findSecretKeySalt()
        else:
            raise ValueError("%s does not appear to contain a backup" % path)

    def findSecretKeySalt(self, newPath=False):
        restrictionsFile = "/398bc9c2aeeab4cb0c12ada0f52eea12cf14f40b"
        if newPath:
            path = self.path + "/39" + restrictionsFile
        else:
            path = self.path + restrictionsFile
        if os.path.isfile(path):
            self.getSecretFromFile(path)
        elif not newPath:
            self.findSecretKeySalt(newPath=(not newPath))

    def getSecretFromFile(self, path):
        try:
            line_list = plistlib.readPlist(path)
            self.secret64 = line_list["RestrictionsPasswordKey"].asBase64()
            self.salt64 = line_list["RestrictionsPasswordSalt"].asBase64()
        except IndexError:
            print("%s appears to be encrypted" % self.path)
            self.crackable = False
        except AttributeError:
            print("Could not find restrictionsFile")
            self.crackable = False

    def crack(self):
        if self.crackable:
            self.pin = crack(self.secret64, self.salt64)
            return self.pin
        return


def find_hashes(path=backup_path()):
    if not os.path.isdir(path):
        print("No device backups found.")
    devices = []
    device_paths = os.listdir(path)
    for device_path in device_paths:
        if ".DS_Store" in device_paths:
            continue
        device_path = os.path.join(path, device_path)
        devices.append(iDevice(device_path))
    return devices


def crack_hashes(devices):
    for device in devices:
        print("Name: %s" % device.name)
        print("Model: %s" % device.model)
        print("UUID: %s" % device.UUID)
        pin = device.crack()
        print("Pin: %s" % pin)


def verify(string, length):
    return len(string) == length and string


def mojave_help():
    if not is_mojave_plus():
        print("You do not need Mojave help.")
        return
    print("Please navigate to ~/Library/Application\\ Support/MobileSync/Backup/", "\n")
    time.sleep(1.5)
    path = os.getcwd() + "/backup"
    try:
        os.mkdir(path)
    except OSError:
        pass
    print(
        "Copy the contents of ~/Library/Application\\ Support/MobileSync/Backup/ to %s"
        % path,
        "\n",
    )
    time.sleep(2)
    print("I'll wait\n")
    time.sleep(0.5)
    input("Press [return] to continue ")
    crack_hashes(find_hashes(path=path))


def prompt():
    secret64Len = 28
    secret64 = input("\nEnter Secret Key: ")
    if not verify(secret64, secret64Len):
        print("Invalid secret, must be %d charaters" % secret64Len)
        prompt()
    salt64Len = 8
    salt64 = input("Enter Salt: ")
    if not verify(salt64, salt64Len):
        print("Invalid salt, must be %d charaters" % salt64Len)
        prompt()
    print("Pin: %s" % crack(secret64, salt64))


def banner():
    """banner method"""
    print("\n iOSRestrictionBruteForce")
    print(" Written by thehappydinoa \n")


class ArgParser(argparse.ArgumentParser):
    """ArgParser argparse.ArgumentParser"""

    def __init__(self):
        """init method"""
        super(ArgParser, self).__init__()

    @staticmethod
    def arg_parse():
        """arg_parse method"""
        parser = argparse.ArgumentParser(
            description="a script to crack the restriction passcode of an iDevice",
        )
        parser.add_argument(
            "-c", "--cli", help="prompts user for input", action="store_true"
        )
        parser.add_argument(
            "-m",
            "--mojave",
            help="helps user run script on macOS mojave +",
            action="store_true",
        )
        parser.add_argument(
            "-b",
            "--backup",
            help="where backups are located",
            metavar="folder",
            type=lambda path: if_folder(path, parser=parser),
        )
        return parser.parse_args()


def main():
    try:
        banner()
        args = ArgParser().arg_parse()
        if args.mojave:
            mojave_help()
        elif args.backup:
            crack_hashes(find_hashes(path=args.backup))
        elif args.cli:
            prompt()
        else:
            crack_hashes(find_hashes())
    except KeyboardInterrupt:
        print("Exiting...\r"),
        exit(0)


if __name__ == "__main__":
    main()
