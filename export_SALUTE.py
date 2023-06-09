import os

import streamlit as st
import pandas as pd
import sqlite3
from datetime import date

# Connect to SQLite database
conn = sqlite3.connect('activities.db')

st.title("Activity Query")

# User input for date range
start_date = st.date_input("Start date", date.today())
end_date = st.date_input("End date", date.today())

# Build SQL query based on date range
query = f'SELECT * FROM activities WHERE date BETWEEN "{start_date}" AND "{end_date}"'

# Caching the function that gets the data from SQL database
@st.cache_data
def get_data(query):
    return pd.read_sql_query(query, conn)

# Execute query and display results when button is clicked
if st.button("Execute"):
    try:
        st.session_state.df = get_data(query)
        st.dataframe(st.session_state.df)
        #st.session_state.mission = st.session_state.df['mission'].drop_duplicates().iloc[0]
    except Exception as e:
        st.error(f"An error occurred: {e}")
current_folder = os.getcwd()
# Export to CSV file when button is clicked
if st.button("Export to CSV"):
    if 'df' in st.session_state and not st.session_state.df.empty:
        try:
            st.session_state.df.to_csv(f'{start_date}_{end_date}.csv', index=False)
            st.success(f"Data exported successfully.\n{current_folder}\\{start_date}_{end_date}.csv")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("No data to export. Please execute the query first.")
