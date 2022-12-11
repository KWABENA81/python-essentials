import sqlite3 as lite


def sql_query():
    con = lite.connect('test.db')
    with con:
        cur = con.cursor()

        cur.execute("DROP TABLE if exists Cars")
        cur.execute("CREATE TABLE if not exists Cars(id INTEGER PRIMARY KEY, Model TEXT);")

        cur.execute("SELECT * FROM Cars")

        for colinfo in cur.fetchall():
            print(colinfo)

    con.close()


if __name__ == '__main__':
    sql_query()
