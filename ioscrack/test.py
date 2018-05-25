import unittest


class iOSCrackTest(unittest.TestCase):

    def test_verify(self):
        from ioscrack.cli import verify
        SECRET64LENGTH = 28
        INVALID_SECRET = "r3JS9BgcHea1hxFIeAAR7z0Il2w"
        VALID_SECRET = "r3JS9BgcHea1hxFIeAAR7z0Il2w="
        SALT64LENGTH = 8
        INVALID_SALT = "osz+8g"
        VALID_SALT = "osz+8g=="
        self.assertEqual(verify(INVALID_SECRET, SECRET64LENGTH), False)
        self.assertEqual(verify(VALID_SECRET, SECRET64LENGTH), True)
        self.assertEqual(verify(INVALID_SALT, SALT64LENGTH), False)
        self.assertEqual(verify(VALID_SALT, SALT64LENGTH), True)

    def test_crack(self):
        from ioscrack.crack import crack
        SECRET64 = "r3JS9BgcHea1hxFIeAAR7z0Il2w="
        SALT64 = "osz+8g=="
        RESULT = "1234"
        self.assertEqual(crack(SECRET64, SALT64, test=True), RESULT)

    def test_database(self):
        from ioscrack.database import keyExists, addKey
        SECRET64 = "r3JS9BgcHea1hxFIeAAR7z0Il2w="
        SALT64 = "osz+8g=="
        RESULT = "1234"
        addKey(SECRET64, SALT64, RESULT)
        self.assertEqual(keyExists(SECRET64, SALT64), RESULT)

    def test_finding(self):
        from ioscrack.parse import findHashes
        from ioscrack.idevice import iDevice
        VALID_DEVICES = findHashes(path="tests", test=True)
        self.assertEqual(type(VALID_DEVICES), list)
        for device in VALID_DEVICES:
            self.assertEqual(type(device), iDevice)
        INVALID_DEVICES = findHashes(path="invalid/folder", test=True)
        self.assertEqual(INVALID_DEVICES, [])

    def test_folder(self):
        from ioscrack.paths import isFolder, fixPath
        VALID_PATH = "tests"
        INVALID_PATH = "invalid/folder"
        self.assertEqual(isFolder(VALID_PATH), VALID_PATH + '/')
        self.assertEqual(isFolder(INVALID_PATH), False)
        self.assertEqual(fixPath(VALID_PATH), VALID_PATH + '/')
        self.assertEqual(fixPath(INVALID_PATH), INVALID_PATH + '/')


def testAll():
    suite = unittest.TestLoader().loadTestsFromTestCase(iOSCrackTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
