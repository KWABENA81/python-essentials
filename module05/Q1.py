import sqlite3


def sql_query():
    con = sqlite3.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute('SELECT sqlite_version()')
        data = cur.fetchone()
        print("SQLite version: %s" % data)
        cur.close()

    con.close()

if __name__ == '__main__':
    sql_query()




###
#   ===> SQLite version: 3.37.2