import sqlite3
# Connect to the database
conn = sqlite3.connect('data.db')
c = conn.cursor()
# Retrieve all data from the table
# c.execute("SELECT * FROM sqlite_sequence")
c.execute("SELECT * FROM formdata")
# c.execute("SELECT name FROM sqlite_master WHERE type='table'")
data = c.fetchall()
# Print the retrieved data
for row in data:
    print(row);
# Close the database connection
conn.close()