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


from MLModelReturns_4 import validDict
import mysql.connector
from mysql.connector import Error

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
        INSERT INTO news (title, summary, link, published, topic)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Transform the data into a list of tuples
        data_tuples = [(d['title'], d['summary'], d['link'], d['published'], ', '.join(d['topics'])) for d in data]

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
