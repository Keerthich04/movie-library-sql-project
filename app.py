import streamlit as st
import sqlite3
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="Movie Library Explorer",
    page_icon="🎬",
    layout="wide"
)

# --- Database Connection ---
DB_FILE = "MovieLibrary.db"

@st.cache_data
def run_query(query):
    """Establishes a connection and runs a given SQL query."""
    with sqlite3.connect(DB_FILE) as conn:
        return pd.read_sql_query(query, conn)

# --- Main App ---
st.title("🎬 My Movie Library Explorer")
st.write("An interactive app to search and explore the top 1000 IMDb movies.")

# --- Search Functionality ---
st.header("🔎 Search for a Movie")
search_term = st.text_input("Enter a movie title to search:")

if search_term:
    search_query = f"""
        SELECT
            m.title AS "Title",
            m.release_year AS "Year",
            m.imdb_rating AS "IMDb Rating", -- <-- ADD THIS
            d.director_name AS "Director",
            g.genre_name AS "Genre"
        FROM Movies m
        JOIN Directors d ON m.director_id = d.director_id
        JOIN Genres g ON m.genre_id = g.genre_id
        WHERE m.title LIKE '%{search_term}%'
    """
    results_df = run_query(search_query)
    st.write(f"Found {len(results_df)} results:")
    st.dataframe(results_df, use_container_width=True)

# --- Display All Movies ---
st.header("📚 Full Movie Library")
st.write("Browse all movies in the database, sorted by release year.")

all_movies_query = """
    SELECT
        m.title AS "Title",
        m.release_year AS "Year",
        m.imdb_rating AS "IMDb Rating", -- <-- ADD THIS
        d.director_name AS "Director",
        g.genre_name AS "Genre"
    FROM Movies m
    JOIN Directors d ON m.director_id = d.director_id
    JOIN Genres g ON m.genre_id = g.genre_id
    ORDER BY m.imdb_rating DESC; -- <-- Let's sort by rating!
"""
all_movies_df = run_query(all_movies_query)
st.dataframe(all_movies_df, use_container_width=True)