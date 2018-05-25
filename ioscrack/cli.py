from builtins import input

from ioscrack.crack import crack


def verify(string, length):
    return (not len(string) < length and not string == "")


def prompt():
    secret64 = input("\nEnter Secret Key: ")
    if verify(secret64, 10):
        print("Invalid Key")
        prompt()
    salt64 = input("Enter Salt: ")
    if verify(salt64, 3):
        print("Invalid Salt")
        prompt()
    crack(secret64, salt64)
