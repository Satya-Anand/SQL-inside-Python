import sqlite3
# Create a SQLite database and a table for sales data
# This script creates a SQLite database and populates it with sample sales data.
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()
# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

# Insert sample data
sales_data = [
    ('Apple', 10, 2.5),
    ('Banana', 5, 1.0),
    ('Orange', 8, 1.8),
    ('Apple', 7, 2.5),
    ('Banana', 10, 1.0),
    ('Orange', 4, 1.8),
    ('Mango', 6, 3.0),
    ('Grapes', 12, 2.0),
    ('Pineapple', 3, 3.5),
    ('Watermelon', 2, 4.0)
]

cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sales_data)
conn.commit()
conn.close()
