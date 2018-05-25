from os import name, path, environ
from os.path import isdir


def fixPath(path):
    if path.endswith('/'):
        return path
    else:
        return path + '/'


def isFolder(path, parser=False):
    if not isdir(path):
        if parser:
            return parser.error("The folder %s does not exist!" % path)
        return False
    else:
        return fixPath(path)


def backupPaths():
    if "nt" in name:
        BACKUP_PATHS = path.join(environ['USERPROFILE'], 'AppData', 'Roaming',
                                 'Apple Computer', 'MobileSync', 'Backup\\')
    else:
        BACKUP_PATHS = path.join(environ['HOME'], 'Library',
                                 'Application Support', 'MobileSync',
                                 'Backup/')
    return BACKUP_PATHS
