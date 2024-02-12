import sqlite3
import os

# Remove the existing database file if it exists
if os.path.exists('example.db'):
    os.remove('example.db')

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cur = conn.cursor()

# Create a table
cur.execute('''CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY,
                product TEXT,
                quantity INTEGER,
                price REAL
            )''')

# Insert some data into the table
cur.execute("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", ('Apple', 10, 2.5))
cur.execute("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", ('Banana', 15, 1.8))
cur.execute("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", ('Orange', 20, 1.0))

# Commit changes
conn.commit()

# Perform SQL queries
# Select all records
cur.execute("SELECT * FROM sales")
all_records = cur.fetchall()
print("All records:")
for record in all_records:
    print(record)

# Select records with quantity greater than 10
cur.execute("SELECT * FROM sales WHERE quantity > 10")
quantity_gt_10 = cur.fetchall()
print("\nRecords with quantity greater than 10:")
for record in quantity_gt_10:
    print(record)

# Select total sales value
cur.execute("SELECT SUM(quantity * price) FROM sales")
total_sales = cur.fetchone()[0]
print("\nTotal sales value:", total_sales)

# Close the connection
conn.close()
