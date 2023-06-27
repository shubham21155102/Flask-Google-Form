import sqlite3

# Connect to the database
conn = sqlite3.connect('Athena.db')
c = conn.cursor()

# Retrieve all data from the table
c.execute("SELECT * FROM sqlite_sequence")
# c.execute("SELECT * FROM Authentication")
# c.execute("SELECT * FROM Blacklist")
# c.execute("SELECT * from Users")
# c.execute("SELECT name FROM sqlite_master WHERE type='table'")
# c.execute("SELECT * FROM Greetings")
data = c.fetchall()
# Print the retrieved data
for row in data:
    print(row);


# Close the database connection
conn.close()
