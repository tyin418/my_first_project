import sqlite3

# Connect to SQLite database (Creates file if not exists)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create a users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert a new user
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
conn.commit()

# Fetch all users
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

print("User List:")
for user in users:
    print(user)

# Close the connection
conn.close()
