import sqlite3
from sqlite3 import Error

def insert_to_database(dbfile, data):
    """
    A function for inserting check outed item data to sqlite3 database.
    Args:
        -dbfile (str) : name of database file
        -data (list of tuples) : check outed item data
    Return: - 
    """
    #error handling for inserting record to database
    try:
        connection = sqlite3.connect(dbfile)
        cursor = connection.cursor()

        cursor.execute(''' CREATE TABLE IF NOT EXISTS checkout_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    unit_price INTEGER NOT NULL,
                    amount INTEGER NOT NULL
                )
        ''')

        cursor.executemany("INSERT INTO checkout_items(item_name, quantity, unit_price, amount) VALUES (?,?,?,?)", data)
        print("Check outed item is succesfully added to database!")
        
        connection.commit()
        connection.close()
    except Error as e:
        print(e)
