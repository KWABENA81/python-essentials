import sqlite3
import sqlite3 as lite


def select_table():
    sql_Select = """SELECT * FROM store;"""
    try:
        conn = lite.connect("store.db")
        cursr = conn.cursor()

        cursr.execute(sql_Select)
        data = cursr.fetchall()
        for row in data:
            print(row)

        cursr.close()
    except sqlite3.Error:
        print("\nFailed to perform operation")
    finally:
        if conn:
            conn.close()
            print("\nConnection close")


if __name__ == '__main__':
    select_table()
