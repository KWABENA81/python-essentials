import sqlite3


def sql_query():
    con = sqlite3.connect('new_db')
    with con:
        cur = con.cursor()

        cur.execute("DROP TABLE if exists Friends")

        cur.execute("CREATE TABLE if not exists Friends(id INTEGER PRIMARY KEY, Name TEXT);")
        cur.execute("INSERT INTO Friends( Name) VALUES('Tom');")
        cur.execute("INSERT INTO Friends( Name) VALUES('Rebecca');")
        cur.execute("INSERT INTO Friends( Name) VALUES('Jim');")
        cur.execute("INSERT INTO Friends( Name) VALUES('Robert');")
        cur.execute("SELECT max(id) FROM Friends")

        print("The last id of the inserted row is %d " % cur.lastrowid)


if __name__ == '__main__':
    sql_query()
