import sqlite3 as lite


def sql_query():

    con = lite.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Cars")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
    con.close()


if __name__ == '__main__':
    sql_query()



# ### OUTPUT
# (1, 'Audi', 52642)
# (2, 'Mercedes', 57127)
# (3, 'Skoda', 9000)
# (4, 'Volvo', 29000)
# (5, 'Bentley', 350000)
# (6, 'Hummer', 41400)
# (7, 'Volkswagen', 21600)
