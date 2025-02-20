import streamlit as st

"""
This file contains the code for the Streamlit web app.

Functions:
    set_label_text_color: Set the label text color to black.
    display_filter_search: Display the filter and search options.
    display_news: Display the filtered news articles.

The display_filter_search function displays the filter and search options for the news articles.
It gives the user the option to filter the news articles by category and search by title or summary.
This function also stores the selected category and search query in the session_state, so that the values are retained across sessions.

The display_news function displays the filtered news articles based on the selected category and search query.
It displays the news articles in columns and cards with the title, summary, published date, and category.

"""

def set_label_text_color():
    st.markdown(
        """
        <style>
        .stSelectbox label, .stTextInput label {
            color: black;  /* Set label text color to black */
        }
        .news-card h3 {
            font-size: 1.2em;  /* Set title font size */
        }
        .news-card p {
            font-size: 0.9em;  /* Set summary font size */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def display_filter_search(data):

    set_label_text_color() 

    categories = ["All"] + sorted(set(row["topics"] for row in data if row["topics"] is not None))

    selected_category = st.selectbox("Select category", categories, index=categories.index(st.session_state.get("selected_category", "All")))

    search_query = st.text_input("Search by title or summary:", value=st.session_state.get("search_query", ""))

    st.session_state.selected_category = selected_category
    st.session_state.search_query = search_query

def display_news(data):
    
    selected_category = st.session_state.get("selected_category", "All")
    search_query = st.session_state.get("search_query", "").lower()

    filtered_data = [row for row in data if 
                     (selected_category == "All" or row["topics"] == selected_category) and
                     (search_query in row["title"].lower() or search_query in row["summary"].lower())]

    filtered_data = [row for row in filtered_data if row["published"] is not None]

   
    cols = st.columns(3) 

    for idx, row in enumerate(filtered_data):
        with cols[idx % 3]:  
            st.markdown(
                f"""
                <div class="news-card" style="border: 3px solid #ddd; border-radius: 10px; padding: 10px; margin-bottom: 10px;);
">
                    <h3>{row["title"]}</h3>
                    <p>{row["summary"]}</p>
                    <p><strong>🗓️ Published:</strong> {row['published']}</p>
                    <p><strong>🏷️ Category:</strong> {row['topics']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
