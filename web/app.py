import streamlit as st
from db import fetch_data
from ui import display_news, display_filter_search
import os

from PIL import Image

# Testa att visa bilden direkt i appen
def show_image():
    image = Image.open("news.jpg")
    st.image(image, use_container_width=True)  # Använd den nya parameteren

def set_background_and_text_color():
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: white;
            color: black;  /* Set text color to black */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    set_background_and_text_color()
    show_image()

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


