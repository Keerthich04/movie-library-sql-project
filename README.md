# Movie-Library-sql-project 🎬

- This is a comprehensive, end-to-end data project that builds, analyzes, and displays a database of the top 1000 IMDb movies.
  The project starts with a raw CSV file and ends with a fully interactive web application, demonstrating a wide range of skills in database management, data engineering, and web development.

## 🚀 Live Application Screenshot
![WhatsApp Image 2025-09-23 at 00 50 31_d99be2b0](https://github.com/user-attachments/assets/69fd177f-d25c-43a9-b179-32dd79174fbf)

## ✨ Key Features
- Automated ETL Pipeline: A Python script automates the entire ETL (Extract, Transform, Load) process: extracting data from a source CSV, cleaning and validating it with Pandas, and loading it into a SQLite database.
- Relational Database: A well-designed SQLite database with a normalized schema, ensuring data integrity with primary and foreign keys.
- Interactive Web App: A user-friendly front-end built with Streamlit that allows users to perform live searches and browse the entire movie library, sorted by IMDb rating.
- Data Analysis: A Jupyter Notebook is included to showcase exploratory data analysis, featuring SQL queries and visualizations that uncover insights from the data (e.g., top directors by movie count).

## 🛠️ Technologies Used
- Back-End: Python
- Database: SQLite, SQL
- Data Manipulation & Analysis: Pandas, Jupyter Notebook
- Data Visualization: Matplotlib, Seaborn
- Web Framework: Streamlit
- Version Control: Git & GitHub

## 📂 Project Structure
├── create_tables.sql             # SQL schema for the database
├── app.py                        # Main script for the Streamlit web app
├── analysis.ipynb                # Jupyter Notebook for data analysis
├── imdb_top_1000.csv             # The raw source data
├── MovieLibrary.db               # The final SQLite database file
├── README.md                     # Project description
└── setup_database.py             # Script to build and populate the database
