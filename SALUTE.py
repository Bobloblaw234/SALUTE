import sqlite3
import streamlit as st



# Connect to SQLite database
conn = sqlite3.connect('SALUTE_REPORTS.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
          CREATE TABLE IF NOT EXISTS activities
          (date text, mission text,activity text, building text, startTime text, endTime text)
          ''')

st.title("SALUTE Reports")
date = st.date_input("Date")
mission = st.text_input('Mission').upper()
activity = st.text_area('Summary of Activity', '', height=200)
building = st.text_input("Building Name").upper()
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")

if st.button("Log Activity"):
    c.execute("INSERT INTO activities (date, mission, activity, building, startTime, endTime) VALUES (?, ?, ?, ?,?,?)",
              (date, mission,activity, building, str(start_time), str(end_time)))
    conn.commit()
    st.success("Activity logged successfully.")





