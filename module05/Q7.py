import sqlite3 as lite


def sql_query():
    con = lite.connect('test.db')
    with con:
        con.row_factory = lite.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM Cars")
        rows = cur.fetchall()
        for row in rows:
            print("%s %s %s" % (row["Id"], row["Name"], row["Price"]))
        cur.close()

    con.close()


if __name__ == '__main__':
    sql_query()
