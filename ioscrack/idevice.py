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
            self.crackable = True
            self.info = readPlist(INFOPATH)
            self.name = self.info['Display Name']
            self.lastBackupDate = self.info['Last Backup Date']
            self.model = self.info['Product Type']
            self.UDID = self.info['Unique Identifier'].lower()
            self.iOS = self.info['Product Version']
            self.targetType = self.info['Target Type']
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
        if isfile(path):
            self.getSecretFromFile(path)
        elif not newPath:
            self.findSecretKeySalt(newPath=(not newPath))

    def getSecretFromFile(self, path):
        try:
            line_list = readPlist(path)
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
