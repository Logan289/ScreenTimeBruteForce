from builtins import input

from ioscrack.crack import crack


def prompt():
    secret64 = input("\nEnter Secret Key: ")
    if len(secret64) < 10 or secret64 == "":
        print("Invalid Key")
        exit()
    salt64 = input("Enter Salt: ")
    if len(salt64) < 3 or salt64 == "":
        print("Invalid Salt")
        exit()
    crack(secret64, salt64)
