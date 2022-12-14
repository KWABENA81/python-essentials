import sqlite3
import sqlite3 as lite


def fetch_desc():
    try:
        conn = lite.connect("store.db")
        cursr = conn.cursor()

        print(cursr.description)

        cursr.close()
    except sqlite3.Error:
        print("\nFailed to perform operation")
    finally:
        if conn:
            conn.close()
            print("\nConnection close")


if __name__ == '__main__':
    fetch_desc()
