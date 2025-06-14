import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect('sales_data.db')

# SQL query to calculate total quantity and revenue per product
query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# Load results into DataFrame
df = pd.read_sql_query(query, conn)

# Close connection
conn.close()

# Print the DataFrame
print("Sales Summary:\n")
print(df)

# Plot a simple bar chart for revenue per product
plt.figure(figsize=(8,5))
df.plot(kind='bar', x='product', y='revenue', legend=False, color='cyan')
plt.title('Total Revenue by Product')
plt.ylabel('Revenue (₹)')
plt.xlabel('Product')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_chart.png")  # Optional
plt.show()
