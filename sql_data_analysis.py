import sqlite3
import pandas as pd

# Connect to SQLite database (or create one)
conn = sqlite3.connect("business.db")
cursor = conn.cursor()

# Create table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    category TEXT,
    price REAL,
    quantity INTEGER
)
""")

# Insert data
cursor.executemany("INSERT INTO sales (product, category, price, quantity) VALUES (?, ?, ?, ?)", [
    ("Laptop", "Electronics", 1000, 5),
    ("Smartphone", "Electronics", 800, 8),
    ("Desk", "Furniture", 150, 10),
])

conn.commit()

# Query data
df = pd.read_sql("SELECT category, SUM(price * quantity) AS total_revenue FROM sales GROUP BY category", conn)
print(df)

# Close connection
conn.close()
