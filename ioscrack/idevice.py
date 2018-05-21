from os.path import isdir, isfile
from plistlib import readPlist

from ioscrack.crack import crack


class iDevice():
    def __init__(self, path):
        if isdir(path):
            self.path = path
        else:
            raise ValueError("%s is not a valid directory" % path)
        INFOPATH = path + "/Info.plist"
        if isfile(INFOPATH):
            self.info = readPlist(INFOPATH)
            self.name = self.info['Display Name']
            self.lastBackupDate = self.info['Last Backup Date']
            self.model = self.info['Product Type']
            self.UDID = self.info['Unique Identifier'].lower()
            self.iOS = self.info['Product Version']
            self.targetType = self.info['Target Type']
            self.findSecretKeySalt()
        else:
            raise ValueError("%s does not appear to contain a backup" % path)

    def findSecretKeySalt(self, newPath=False):
        restrictionsFile = "/398bc9c2aeeab4cb0c12ada0f52eea12cf14f40b"
        try:
            if newPath:
                passfile = open(self.path + "/39" + restrictionsFile, "r")
            else:
                passfile = open(self.path + restrictionsFile, "r")
        except IOError:
            if not newPath:
                return self.findSecretKeySalt(newPath=(not newPath))
        try:
            line_list = passfile.readlines()
            self.secret64 = line_list[6][1:29]
            self.salt64 = line_list[10][1:9]
        except IndexError:
            raise ValueError("%s appears to be encrypted" % self.path)

    def crack(self):
        self.pin = crack(self.secret64, self.salt64)
        return self.pin
