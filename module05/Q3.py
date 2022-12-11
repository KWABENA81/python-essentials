import os
import sqlite3


def xxxxxxx(db_filename):
    return os.path.exists(db_filename)


def sql_query():
    db_filename = 'todo.db'
    db_is_new = not xxxxxxx(db_filename)

    conn = sqlite3.connect(db_filename)

    if db_is_new:
        print('Need to create schema')
        print('Creating database')
    else:
        print('Database exists, assume schema does, too')

    conn.close()


if __name__ == '__main__':
    sql_query()
