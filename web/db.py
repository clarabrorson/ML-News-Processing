import mysql.connector
from config import DB_CONFIG

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
