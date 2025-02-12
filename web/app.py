import streamlit as st
import mysql.connector
import pandas as pd

# Funktion för att hämta data från databasen
def fetch_data():
    try:
        cnxn = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="javaintegration", 
            database="news"
        )
        cursor = cnxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM news")
        rows = cursor.fetchall()
        cursor.close()
        cnxn.close()
        return rows
    except Exception as e:
        st.error(f"Connection-error: {e}")
        return []

# Huvudfunktion för att visa datan i Streamlit
def main():
    st.title("News Dashboard")

    # Hämta data från databasen
    data = fetch_data()

    if not data:
        st.write("No data found.")
        return

    # Skapa ett filter för att välja kategori
    categories = ["All"] + sorted(set(row["topics"] for row in data if row["topics"] is not None))
    selected_category = st.selectbox("Select category", categories)

    # Sökfunktion
    search_query = st.text_input("Search by title or summary:")

    # Filtrering av data baserat på val
    filtered_data = [row for row in data if 
                     (selected_category == "All" or row["topics"] == selected_category) and
                     (search_query.lower() in row["title"].lower() or search_query.lower() in row["summary"].lower())]

    # Sortering
    sort_option = st.selectbox("Sort by:", ["Publication date", "Title"])
    reverse_order = st.checkbox("Reverse order")

    # Filtrera bort rader där published är None
    filtered_data = [row for row in filtered_data if row["published"] is not None]

    if sort_option == "Publication date":
        filtered_data.sort(key=lambda x: x["published"], reverse=reverse_order)
    else:
        filtered_data.sort(key=lambda x: x["title"], reverse=reverse_order)

    # Visa resultaten
    for row in filtered_data:
        st.subheader(row["title"])
        st.write(row["summary"])
        st.write(f"🗓️ Published: {row['published']} | 🏷️ Category: {row['topics']}")
        st.write("---")

# Kör applikationen
if __name__ == "__main__":
    main()
