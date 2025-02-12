import streamlit as st

def display_filter_search(data):
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

    # Visa de filtrerade nyheterna
    for row in filtered_data:
        st.subheader(row["title"])
        st.write(row["summary"])
        st.write(f"🗓️ Published: {row['published']} | 🏷️ Category: {row['topics']}")
        st.write("---")
