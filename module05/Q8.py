import sqlite3 as lite


def sql_query():
    uId = 1
    uPrice = 62300
    con = lite.connect('test.db')
    with con:
        cur = con.cursor()

        cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))

        con.commit()

        print("Number of rows updated: %d" % cur.rowcount)


if __name__ == '__main__':
    sql_query()

