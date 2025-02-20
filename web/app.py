import streamlit as st
from db import fetch_data
from ui import display_news, display_filter_search
import os
from PIL import Image

# This is the main file for the Streamlit web application, it includes the main function that is run when the application is started.
# To start the application run the following command in the terminal:
# streamlit run app.py
#
# The file also includes the following functions:
# - show_image: Displays an image in the center of the page.
# - set_background_and_text_color: Sets the background color to white and the text color to black.
#
# HTML and CSS code is used to style the page and the elements on the page.
# To center the image on the page, the image is placed in the middle column of a three column layout.
#
# An if statement is used to check if the data has already been fetched from the database and stored in the session_state.
# If the data has not been fetched, the data is fetched and stored in the session_state.
#
# The main function also calls the display_filter_search and display_news functions from the ui.py file to display the filter and search bar and the news articles on the page.


def show_image():
    image = Image.open("news.jpg")

    col1, col2, col3 = st.columns([1, 2, 1])    
    with col2:  
        st.image(image, width=500)
        st.markdown("<h1 style='text-align: center; font-weight: normal; font-size: 36px;'>News Hub</h1>", unsafe_allow_html=True)

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

    if "data" not in st.session_state:
        data = fetch_data()
        if not data:
            st.write("No data found.")
            return
        st.session_state.data = data

   
    display_filter_search(st.session_state.data)
    display_news(st.session_state.data)

if __name__ == "__main__":
    main()


