"""
This script connects to a MySQL database and inserts the data from the MLModelReturns_4.py script into the database.
The script first establishes a connection to the database, then defines a function to convert the date format to a MySQL-compatible format.
The script then defines a function to insert the data into the database, and finally calls the main function to execute the script.
The main function calls the db_connection function to establish a connection to the database, and if successful, inserts the data into the database.
The script can be run independently to transfer the data from the ML model to the database.

"""



import mysql.connector
from mysql.connector import Error
from MLModelReturns_4 import main

validDict = main()

if validDict:
    print("First classified article:", validDict[0]) 
else:
    print("No classified articles found.")

def db_connection():

    try:
        
        cnxn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="javaintegration",
            database="news"
        )
        if cnxn.is_connected():
            print("Successfully connected to the database")
            return cnxn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

from datetime import datetime

def convert_to_mysql_date(date_str):

    date_formats = [
        "%a, %d %b %Y %H:%M:%S %z",  # e.g., Tue, 11 Feb 2025 05:51:26 +0100
        "%Y-%m-%dT%H:%M:%S%z",       # e.g., 2025-02-11T09:39:00+01:00
        "%Y-%m-%d %H:%M:%S",         # e.g., 2025-02-11 09:39:00
        "%a, %d %b %Y %H:%M:%S GMT"  # e.g., Tue, 11 Feb 2025 01:36:09 GMT
    ]
    
    for fmt in date_formats:
        try:
            date_obj = datetime.strptime(date_str, fmt)
            return date_obj.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
    
    print(f"Invalid date format for '{date_str}'. Setting it to NULL.")
    return None  

def insert_data(data, cnxn):

    try:
        cursor = cnxn.cursor()

        sql = """
        INSERT INTO news (title, summary, link, published, topics)
        VALUES (%s, %s, %s, %s, %s)
        """
        data_tuples = [(d['title'], d['summary'], d['link'], convert_to_mysql_date(d['published']), ', '.join(d['topics'])) for d in data]

        cursor.executemany(sql, data_tuples)

        cnxn.commit()
        print(f"{cursor.rowcount} records inserted successfully.")

        cursor.close()
    except Error as e:
        print(f"Error inserting data: {e}")
        cnxn.rollback()  

def main():
    
    cnxn = db_connection()
    
    if cnxn:
        
        data = validDict  
        insert_data(data, cnxn)
        
        
        cnxn.close()
    else:
        print("No database connection established.")

if __name__ == "__main__":
    main()
