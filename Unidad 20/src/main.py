# Imports
import sqlite3
import pandas as pd
import os

# Define constants
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(ROOT_DIR, 'databases')
DB_NAME = 'olympics.db'
DB_PATH = os.path.join(DB_DIR, DB_NAME)

# Get DataFrame
df_medals = pd.read_csv("http://winterolympicsmedals.com/medals.csv")

# Subset by USA Gold Medals since 1950
df_medals_usa_1950 = df_medals[
    (df_medals['Medal'] == 'Gold')
    & (df_medals['Year'] >= 1950)
    & (df_medals['NOC'] == 'USA')
    ]

# Connect to database
conn = sqlite3.connect(DB_PATH)
# Create a cursor
cursor = conn.cursor()
# Create a 'medals' table
query = """CREATE TABLE IF NOT EXISTS medals (
            Year INTEGER,
            City TEXT,
            Sport TEXT,
            Discipline TEXT,
            NOC TEXT,
            Event TEXT,
            'Event gender' TEXT,
            Medal TEXT
            )"""
cursor.execute(query)
conn.commit()

# Store subset dataframe into 'medals' table
df_medals_usa_1950.to_sql(
    'medals',
    con=conn,
    if_exists='replace',
    index_label='IdMedal'
    )

# Check data in database
query = "SELECT * FROM medals LIMIT 10"
cursor.execute(query)
results = cursor.fetchall()
for r in results:
    print(r)

# Close connection
conn.close()
