from __future__ import print_function
from time import time
from base64 import b64decode
from passlib.utils.pbkdf2 import pbkdf2

from ioscrack.database import addKey, keyExists

COMMON_KEYS = [
    1234, 1111, 0000, 1212, 7777, 1004, 2000, 4444, 2222, 6969, 9999, 3333,
    5555, 6666, 1122, 1313, 8888, 4321, 2001, 1010, 2580
]


def check(secret64, salt64, key):
    try:
        secret = b64decode(secret64)
        salt = b64decode(salt64)
    except TypeError as e:
        print(str(e))
        exit(1)
    out = pbkdf2(key, salt, 1000)
    status = (out == secret)
    if status:
        addKey(secret64, salt64, key)
    return status


def print_try(key):
    print("Trying: %d \r" % key, end=""),


def crack(secret64, salt64):
    secret64 = secret64.strip()
    salt64 = salt64.strip()
    start_t = time()
    inDB = keyExists(secret64, salt64)
    if inDB:
        key = inDB[0]
        duration = round(time() - start_t, 2)
        print("Passcode is %s (in database)\n" % (key))
        return key
    # Top 20 common pins
    for i in COMMON_KEYS:
        print_try(i)
        key = "%04d" % (i)
        if check(secret64, salt64, key):
            duration = round(time() - start_t, 2)
            print("Passcode is %s (top %d most common passcode)\n" %
                  (key, len(COMMON_KEYS)))
            return key
    # Common birth dates
    for i in range(1900, 2017):
        print_try(i)
        key = "%04d" % (i)
        if check(secret64, salt64, key):
            duration = round(time() - start_t, 2)
            print("Passcode is %s (common year) it took %s secconds\n" %
                  (key, duration))
            return key
    # Brute force all pins
    for i in range(10000):
        print_try(i)
        key = "%04d" % (i)
        if check(secret64, salt64, key):
            duration = round(time() - start_t, 2)
            print("Passcode is %s it took %s secconds\n" % (key, duration))
            return key
    print("Invalid Key and/or Salt")


def crackHashes(devices):
    for device in devices:
        print("\nUDID: %s \n%s: %s running iOS %s" %
              (device.UDID, device.targetType, device.model, device.iOS))
        print("Cracking restrictions passcode for %s..." % device.name)
        #if not session[device.UDID]:
        device.crack()
