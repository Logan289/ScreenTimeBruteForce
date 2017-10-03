#!/usr/bin/python
#Filename: ioscrack.py

from passlib.utils.pbkdf2 import pbkdf2
from time import time
import os, sys, base64

HOMEDIR = '~/Library/Application Support/MobileSync/Backup/'

def crack(secret64, salt64):
    print "secret: ", secret64
    print "salt: ", salt64
    secret = base64.b64decode(secret64)
    salt = base64.b64decode(salt64)
    start_t = time()
    for i in range(10000):
        key = "%04d" % ( i )
        out = pbkdf2(key, salt, 1000)
        if out == secret:
            print "key: ", key
            duration = time() - start_t
            print "%f seconds" % ( duration )
            sys.exit(0)
    print "no exact key"

try:
    backup_dir = os.listdir(HOMEDIR)
    for bkup_dir in backup_dir:
        passfile = open(HOMEDIR + bkup_dir + "/398bc9c2aeeab4cb0c12ada0f52eea12cf14f40b", "r")
        line_list = passfile.readlines()
        secret64 = line_list[6][1:29]
        salt64 = line_list[10][1:9]
        crack(secret64, salt64)
except Exception as e:
    while not secret64:
        secret64 = raw_input("Enter Secret Key: ")
        if secret64 < 3:
            secret64 = NONE
    while not salt64:
        salt64 = raw_input("Enter Salt: ")
        if salt64 < 10:
            salt64 = NONE
    crack(secret64, salt64)
