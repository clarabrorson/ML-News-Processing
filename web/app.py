import streamlit as st
from db import fetch_data
from ui import display_news, display_filter_search

def main():
    st.title("News Dashboard")

    # Hämta data från databasen en gång och lagra i session_state om det inte redan finns
    if "data" not in st.session_state:
        data = fetch_data()
        if not data:
            st.write("No data found.")
            return
        st.session_state.data = data

    # Visa filter och sökfunktion
    display_filter_search(st.session_state.data)

    # Visa nyheter
    display_news(st.session_state.data)

if __name__ == "__main__":
    main()


