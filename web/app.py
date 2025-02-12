import streamlit as st
from db import fetch_data
from ui import display_news, display_filter_search

def main():
    # Lägg till logotyp
    st.image("assets/logo.png", width=200)

    st.title("News Dashboard")

    # Hämta data från databasen
    data = fetch_data()

    if not data:
        st.write("No data found.")
        return

    # Visa filter och sökfunktion
    display_filter_search(data)

    # Visa nyheter
    display_news(data)

if __name__ == "__main__":
    main()
