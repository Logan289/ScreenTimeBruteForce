import sqlite3


def connect(db_name="pins.db"):
    conn = sqlite3.connect(db_name)
    if not doesTableExist(conn):
        createTable(conn)
    return conn


def doesTableExist(conn):
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='KEYS';")
    results = cursor.fetchone()
    return results


def createTable(conn):
    conn.execute('''CREATE TABLE KEYS
         (secret64      CHAR(50) NOT NULL,
         salt64         CHAR(50) NOT NULL,
         key            INT      NOT NULL);''')


def keyExists(secret64, salt64, conn=connect()):
    cursor = conn.execute(
        "SELECT key FROM KEYS WHERE secret64 = ? AND salt64 = ?", (
            secret64,
            salt64,
        ))
    results = cursor.fetchone()
    return results


def addKey(secret64, salt64, key, conn=connect()):
    if not keyExists(secret64, salt64):
        conn.execute("INSERT INTO KEYS (secret64, salt64, key) \
          VALUES (?, ?, ?)", (
            secret64,
            salt64,
            key,
        ))
        conn.commit()
