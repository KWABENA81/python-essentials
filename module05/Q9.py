import sqlite3 as lite


def sqlite3_create_function(db, table_info, param1, SQLITE_UTF8, id, name, price):
    pass

def sql_query():
    con = lite.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute('sqlite3_create_function table_info(Cars)')
        data = cur.fetchall()

        for d in data:
            print(d[0], d[1], d[2])


if __name__ == '__main__':
    sql_query()
