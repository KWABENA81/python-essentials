import csv
import sqlite3
import sqlite3 as lite


def re_row(row):
    lst = []
    for r in row:
        lst.append(r)
    return lst


def from_csv_load_db(csv_file):
    sql_drop_table = """DROP TABLE if exists store;"""
    sql_create_table = """CREATE TABLE if not exists store (float1, float2, telNr, address);"""
    sql_data_insert = """INSERT INTO store (float1, float2, telNr, address) VALUES (?, ?, ?, ?);"""

    try:
        conn = lite.connect("store.db")
        cursr = conn.cursor()

        cursr.execute(sql_drop_table)
        cursr.execute(sql_create_table)

        with open(csv_file, 'r') as csvfile:
            read_obj = csv.reader(csvfile)

            for row in read_obj:
                cursr.execute(sql_data_insert, re_row(row))
            conn.commit()
            print("DB loaded ... ")

            cursr.close()
    except sqlite3.Error:
        print("Failed to perform operation")
    finally:
        if conn:
            conn.close()
            print("Connection close")


if __name__ == '__main__':
    from_csv_load_db('sample-storedata.csv')
