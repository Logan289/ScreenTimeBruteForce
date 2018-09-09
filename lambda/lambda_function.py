from __future__ import print_function

from base64 import b64decode
from datetime import date
from time import time

from passlib.utils.pbkdf2 import pbkdf2

COMMON_KEYS = [
    1234, 1111, 0000, 1212, 7777, 1004, 2000, 4444, 2222, 6969,
    9999, 3333, 5555, 6666, 1122, 1313, 8888, 4321, 2001, 1010
]


def format_key(pin):
    return "%04d" % int(pin)


def check(secret64, salt64, key):
    try:
        secret = b64decode(secret64)
        salt = b64decode(salt64)
    except TypeError as e:
        raise ValueError("Unable to base64 decode")
    return pbkdf2(key, salt, 1000) == secret


def try_pins(secret64, salt64, pins):
    for pin in pins:
        pin = format_key(pin)
        if check(secret64, salt64, pin):
            return pin
    return None


def crack(secret64, salt64):
    pin = try_pins(secret64, salt64, COMMON_KEYS)
    if not pin:
        pin = try_pins(secret64, salt64, range(1000, date.today().year + 50))
    if not pin:
        pin = try_pins(secret64, salt64, range(10000))
    return {"pin": pin}


def lambda_handler(event, context):
    print("Parsing args")
    operation = event.get("operation")

    if operation == "crack":
        print("Cracking...")
        payload = event.get("payload")
        secret64 = payload.get("secret64")
        salt64 = payload.get("salt64")
        return crack(secret64, salt64)
    return ValueError("Unrecognized operation '{}'".format(operation))


if __name__ == "__main__":
    sample_event = {
        "operation": "crack",
        "payload": {
            "secret64": "r3JS9BgcHea1hxFIeAAR7z0Il2w=",
            "salt64": "osz+8g=="
        }
    }
    print(lambda_handler(sample_event, None))
