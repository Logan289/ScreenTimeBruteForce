#!/usr/bin/python2

from datetime import datetime
from passlib.utils.pbkdf2 import pbkdf2
from plistlib import readPlist
from base64 import b64decode
from time import time
import os
import os.path
import sys

BACKUP_PATHS = ['~/Library/Application Support/MobileSync/Backup/',
                os.path.dirname(__file__) + "/Backups/"]
COMMON_KEYS = [1234, 1111, 0000, 1212, 7777, 1004, 2000, 4444, 2222,
               6969, 9999, 3333, 5555, 6666, 1122, 1313, 8888, 4321, 2001, 1010, 2580]


class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'


def logo():
    print("%s\n iOSRestrictionBruteForce" % color.HEADER)
    print(" Written by thehappydinoa %s" % color.END)


def check(secret64, salt64, key):
    secret = b64decode(secret64)
    salt = b64decode(salt64)
    out = pbkdf2(key, salt, 1000)
    return (out == secret)


def crack(secret64, salt64):
    start_t = time()
    for i in COMMON_KEYS:
        key = "%04d" % (i)
        if check(secret64, salt64, key):
            duration = time() - start_t
            return (key, duration)
    for i in range(1900, ):
        key = "%04d" % (i)
        if check(secret64, salt64, key):
            duration = time() - start_t
            return (key, duration)
    for i in range(10000):
        key = "%04d" % (i)
        if check(secret64, salt64, key):
            duration = time() - start_t
            return (key, duration)


def prompt():
    response = raw_input(
        "Do you want to manually enter a hash and salt? (Y/n): ")
    if (response == 'y' or response == 'Y'):
        print("Please manually find the file 398bc9c2aeeab4cb0c12ada0f52eea12cf14f40b within a iOS backup folder")
        secret64 = raw_input("Enter Secret Key: ")
        if secret64 < 3:
            secret64 = NONE
        salt64 = raw_input("Enter Salt: ")
        if salt64 < 10:
            salt64 = NONE
        crack(secret64, salt64)


def findHash(path):
    print("\n%sLooking for backups in %s..." % (color.OKBLUE, path)),
    try:
        backup_dir = os.listdir(path)
        print("%sFound %s" % (color.OKGREEN, color.END))
        for bkup_dir in backup_dir:
            try:
                INFOPATH = path + bkup_dir + "/Info.plist"
                if os.path.isfile(INFOPATH):
                    pl = readPlist(INFOPATH)
                    try:
                        deviceName = pl['Device Name']
                        lastBackupDate = pl['Last Backup Date']
                        print('\n%sFound Backup for %s as of %s %s' %
                              (color.OKGREEN, deviceName, str(lastBackupDate), color.END))
                    except:
                        break
                    try:
                        passfile = open(path + bkup_dir +
                                        "/398bc9c2aeeab4cb0c12ada0f52eea12cf14f40b", "r")
                        line_list = passfile.readlines()
                        secret64 = line_list[6][1:29]
                        salt64 = line_list[10][1:9]
                        print("%sCracking restrictions passcode for %s... %s" %
                              (color.OKBLUE, deviceName, color.END))
                        results = crack(secret64, salt64)
                        print("%sPasscode is %s %s" %
                              (color.NOTICE, results[0], color.END))
                    except IOError:
                        print("%sNo restriction hash found\n%s" %
                              (color.FAIL, color.END))
            except OSError as e:
                print(
                    "Unable to find backups with restrictions with passcode in %s" % bkup_dir)
    except OSError as e:
        print("%sNot Found%s" % (color.FAIL, color.END))


def findHashes(paths):
    for path in paths:
        findHash(path)
    prompt()


if __name__ == "__main__":
    logo()
    findHashes(BACKUP_PATHS)
