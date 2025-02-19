import streamlit as st

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
    set_label_text_color()  # Apply the custom CSS

    # Skapa en lista med alla unika kategorier i datan (exkluderar None)
    categories = ["All"] + sorted(set(row["topics"] for row in data if row["topics"] is not None))

    # Skapa en drop-down meny för att välja kategori
    selected_category = st.selectbox("Select category", categories, index=categories.index(st.session_state.get("selected_category", "All")))

    # Skapa ett textfält för att söka efter nyheter
    search_query = st.text_input("Search by title or summary:", value=st.session_state.get("search_query", ""))

    # Spara de valda värdena i session_state så att de kan användas senare
    st.session_state.selected_category = selected_category
    st.session_state.search_query = search_query

def display_news(data):
    # Hämta de filtrerade värdena från session_state
    selected_category = st.session_state.get("selected_category", "All")
    search_query = st.session_state.get("search_query", "").lower()

    # Filtrera data baserat på kategori och sökfråga
    filtered_data = [row for row in data if 
                     (selected_category == "All" or row["topics"] == selected_category) and
                     (search_query in row["title"].lower() or search_query in row["summary"].lower())]

    # Filtrera bort rader där 'published' är None
    filtered_data = [row for row in filtered_data if row["published"] is not None]

    # Visa de filtrerade nyheterna i kolumner och kort
    cols = st.columns(3)  # Skapa tre kolumner

    for idx, row in enumerate(filtered_data):
        with cols[idx % 3]:  # Fördela artiklarna över kolumnerna
            st.markdown(
                f"""
                <div class="news-card" style="border: 3px solid #ddd; border-radius: 10px; padding: 10px; margin-bottom: 10px;">
                    <h3>{row["title"]}</h3>
                    <p>{row["summary"]}</p>
                    <p><strong>🗓️ Published:</strong> {row['published']}</p>
                    <p><strong>🏷️ Category:</strong> {row['topics']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
