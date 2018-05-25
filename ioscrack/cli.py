from builtins import input

from ioscrack.crack import crack


def verify(string, length):
    return (len(string) == length and not string == "")


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
    crack(secret64, salt64)
