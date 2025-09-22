-- Create the Directors table
CREATE TABLE Directors (
    director_id INTEGER PRIMARY KEY AUTOINCREMENT,
    director_name TEXT NOT NULL UNIQUE
);

-- Create the Genres table
CREATE TABLE Genres (
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre_name TEXT NOT NULL UNIQUE
);

-- Create the Movies table (with the new imdb_rating column)
CREATE TABLE Movies (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    release_year INTEGER,
    imdb_rating REAL, -- <-- ADD THIS LINE
    director_id INTEGER,
    genre_id INTEGER,
    FOREIGN KEY (director_id) REFERENCES Directors(director_id),
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
);