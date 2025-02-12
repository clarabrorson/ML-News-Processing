import streamlit as st

def display_filter_search(data):
    categories = ["All"] + sorted(set(row["topics"] for row in data if row["topics"] is not None))
    selected_category = st.selectbox("Select category", categories)

    search_query = st.text_input("Search by title or summary:")
    
    st.session_state.selected_category = selected_category
    st.session_state.search_query = search_query

def display_news(data):
    selected_category = st.session_state.get("selected_category", "All")
    search_query = st.session_state.get("search_query", "").lower()

    filtered_data = [row for row in data if 
                     (selected_category == "All" or row["topics"] == selected_category) and
                     (search_query in row["title"].lower() or search_query in row["summary"].lower())]

    sort_option = st.selectbox("Sort by:", ["Publication date", "Title"])
    reverse_order = st.checkbox("Reverse order")

    if sort_option == "Publication date":
        filtered_data.sort(key=lambda x: x["published"], reverse=reverse_order)
    else:
        filtered_data.sort(key=lambda x: x["title"], reverse=reverse_order)

    for row in filtered_data:
        st.markdown(f"""
        <div style="background-color:#f4f4f4; padding: 15px; margin: 10px 0; border-radius: 8px;">
            <h4>{row["title"]}</h4>
            <p>{row["summary"]}</p>
            <p><strong>Published:</strong> {row["published"]} | <strong>Category:</strong> {row["topics"]}</p>
        </div>
        """, unsafe_allow_html=True)
