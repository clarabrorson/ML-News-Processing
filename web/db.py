import mysql.connector
from config import DB_CONFIG

"""
This file contains the code to fetch data from the MySQL database.
To protect the database credentials, the configuration is stored in a separate config.py file.
The fetch_data function fetches all the news articles from the database and returns them as a list of dictionaries.

This file is imported in the web/ui.py file to fetch the data for the Streamlit web app.
The data is then used to display the news articles based on the selected category and search query.
"""
def fetch_data():
    try:
        cnxn = mysql.connector.connect(
            host=DB_CONFIG["host"], 
            user=DB_CONFIG["user"], 
            password=DB_CONFIG["password"], 
            database=DB_CONFIG["database"]
        )
        cursor = cnxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM news")
        rows = cursor.fetchall()
        cursor.close()
        cnxn.close()
        return rows
    except Exception as e:
        raise Exception(f"Error fetching data: {e}")
