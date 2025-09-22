import sqlite3
import pandas as pd
import os

# --- CONFIGURATION ---
DB_FILE = "MovieLibrary.db"
CSV_FILE = "imdb_top_1000.csv"
SCHEMA_FILE = "sql_scripts/create_tables.sql"

def setup_database():
    """Builds and populates the database from scratch."""

    # 1. Clean up old database file
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"✅ Old database '{DB_FILE}' removed.")

    # 2. Connect to DB and create tables
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        with open(SCHEMA_FILE, 'r') as f:
            cursor.executescript(f.read())
        print("✅ Database and tables created successfully.")
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        return

    # 3. Read the movie data from CSV
    try:
        df = pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        print(f"❌ Error: The file '{CSV_FILE}' was not found. Make sure it's in the correct folder.")
        return

    # --- DATA CLEANING SECTION ---
    # Force 'IMDB_Rating' to be a number. If a value can't be converted, the row will be dropped.
    df['IMDB_Rating'] = pd.to_numeric(df['IMDB_Rating'], errors='coerce')

    # Force 'Released_Year' to be a number. This handles non-year text like 'PG-13'.
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')

    # Drop any rows that had conversion errors in critical columns.
    df.dropna(subset=['IMDB_Rating', 'Released_Year', 'Director', 'Genre'], inplace=True)
    df['Released_Year'] = df['Released_Year'].astype(int) # Convert year to a whole number
    print("✅ Data types cleaned and validated.")
    # --- END OF DATA CLEANING SECTION ---
    
    # 4. Insert unique Directors and Genres
    directors = df['Director'].unique()
    pd.DataFrame(directors, columns=['director_name']).to_sql('Directors', conn, if_exists='append', index=False)
    
    all_genres = set()
    df['Genre'].str.split(', ').apply(all_genres.update)
    pd.DataFrame(list(all_genres), columns=['genre_name']).to_sql('Genres', conn, if_exists='append', index=False)
    print(f"✅ Inserted unique directors and genres.")

    # 5. Prepare and insert movies with correct foreign keys
    director_map = pd.read_sql('SELECT director_id, director_name FROM Directors', conn).set_index('director_name')['director_id'].to_dict()
    genre_map = pd.read_sql('SELECT genre_id, genre_name FROM Genres', conn).set_index('genre_name')['genre_id'].to_dict()

    movies_to_insert = []
    for _, row in df.iterrows():
        main_genre = row['Genre'].split(', ')[0]
        director_id = director_map.get(row['Director'])
        genre_id = genre_map.get(main_genre)
        
        if director_id and genre_id:
            movies_to_insert.append((
                row['Series_Title'],
                row['Released_Year'],
                row['IMDB_Rating'],
                director_id,
                genre_id
            ))
            
    cursor.executemany(
        'INSERT INTO Movies (title, release_year, imdb_rating, director_id, genre_id) VALUES (?, ?, ?, ?, ?)',
        movies_to_insert
    )
    print(f"✅ Inserted {len(movies_to_insert)} movies.")

    # 6. Commit and close
    conn.commit()
    conn.close()
    print("\n🎉 Database setup is complete!")

if __name__ == "__main__":
    setup_database()