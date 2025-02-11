"""
DbTransfer_5.py

This script will:
  - Import the final structured/validated data (e.g., `validDict`) from MLModelReturns_4.py
  - Connect to a MySQL database
  - Insert each record into a table (e.g., `news`) with columns: (title, summary, link, published, topic).

Students:
 - Fill out the pseudo code to connect to the DB, handle potential errors,
   and insert data in a loop or with executemany.
"""



import mysql.connector
from mysql.connector import Error

#from MLModelReturns_4 import validDict

from MLModelReturns_4 import main

validDict = main()

# Lägg till utskrift för att kontrollera den första artikeln
if validDict:
    print("First classified article:", validDict[0])  # Skriv ut den första klassificerade artikeln
else:
    print("No classified articles found.")

def db_connection():
    """
    Create and return a database connection.
    Pseudo code:
       - try to connect with mysql.connector.connect
       - return the connection object if successful
       - otherwise handle exceptions and return None
    """
    try:
        # Establish a connection to the MySQL database
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
    """
    Convert a date string to a MySQL-compatible date format (YYYY-MM-DD).
    If the string is already a valid date, return it as is.
    """
    try:
        # Attempt to parse the date string into a datetime object
        # Adjust the format string to match your date string's format
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        print(f"Invalid date format for '{date_str}'. Setting it to NULL.")
        return None  # Return None if the date format is invalid

def insert_data(data, cnxn):
    """
    Insert the provided data (list of dict) into the 'news' table.
    Each dict in 'data' is expected to have:
      - 'title'
      - 'summary'
      - 'link'
      - 'published'
      - 'topic'
    """
    try:
        # Create a cursor from the connection object
        cursor = cnxn.cursor()

        # Define the INSERT statement
        sql = """
        INSERT INTO news (title, summary, link, published, topics)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Transform the data into a list of tuples
        data_tuples = [(d['title'], d['summary'], d['link'], convert_to_mysql_date(d['published']), ', '.join(d['topics'])) for d in data]

        # Use cursor.executemany to insert the data
        cursor.executemany(sql, data_tuples)

        # Commit the transaction
        cnxn.commit()
        print(f"{cursor.rowcount} records inserted successfully.")

        # Close the cursor
        cursor.close()
    except Error as e:
        print(f"Error inserting data: {e}")
        cnxn.rollback()  # Rollback in case of error


def main():
    # 1. Connect to the DB
    cnxn = db_connection()
    
    if cnxn:
        # 2. Insert data
        data = validDict  # from MLModelReturns_4
        insert_data(data, cnxn)
        
        # 3. Close the connection
        cnxn.close()
    else:
        print("No database connection established.")

if __name__ == "__main__":
    main()
