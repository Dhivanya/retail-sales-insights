import pandas as pd
import sqlite3

# Load CSV into SQLite
df = pd.read_csv('sales_data.csv')
conn = sqlite3.connect('sales.db')
df.to_sql('sales', conn, if_exists='replace', index=False)
print("✅ Data loaded into SQLite database!")

# Run SQL queries
def run_query(title, query):
    print(f"\n=== {title} ===")
    result = pd.read_sql_query(query, conn)
    print(result.to_string(index=False))

# Query 1 - Total Revenue
run_query("TOTAL REVENUE", """
    SELECT SUM(revenue) as Total_Revenue 
    FROM sales
""")

# Query 2 - Revenue by Product
run_query("REVENUE BY PRODUCT", """
    SELECT product, 
           SUM(revenue) as Total_Revenue,
           COUNT(*) as Total_Orders
    FROM sales
    GROUP BY product
    ORDER BY Total_Revenue DESC
""")

# Query 3 - Revenue by Region
run_query("REVENUE BY REGION", """
    SELECT region,
           SUM(revenue) as Total_Revenue,
           COUNT(*) as Total_Orders
    FROM sales
    GROUP BY region
    ORDER BY Total_Revenue DESC
""")

# Query 4 - Monthly Revenue
run_query("MONTHLY REVENUE", """
    SELECT month,
           SUM(revenue) as Monthly_Revenue,
           COUNT(*) as Orders
    FROM sales
    GROUP BY month
    ORDER BY Monthly_Revenue DESC
""")

# Query 5 - Order Status Breakdown
run_query("ORDER STATUS", """
    SELECT status,
           COUNT(*) as Count,
           SUM(revenue) as Revenue
    FROM sales
    GROUP BY status
    ORDER BY Count DESC
""")

# Query 6 - Top 3 Products per Region
run_query("TOP PRODUCT PER REGION", """
    SELECT region, product, SUM(revenue) as Revenue
    FROM sales
    GROUP BY region, product
    ORDER BY region, Revenue DESC
""")

# Query 7 - Average Order Value by Product
run_query("AVERAGE ORDER VALUE BY PRODUCT", """
    SELECT product,
           ROUND(AVG(revenue), 2) as Avg_Order_Value,
           ROUND(AVG(quantity), 2) as Avg_Quantity
    FROM sales
    GROUP BY product
    ORDER BY Avg_Order_Value DESC
""")

# Query 8 - High Value Orders above 500000
run_query("HIGH VALUE ORDERS", """
    SELECT order_id, product, region, revenue
    FROM sales
    WHERE revenue > 500000
    ORDER BY revenue DESC
    LIMIT 10
""")

# Query 9 - Cancelled Orders Loss
run_query("REVENUE LOST FROM CANCELLATIONS", """
    SELECT SUM(revenue) as Lost_Revenue,
           COUNT(*) as Cancelled_Orders
    FROM sales
    WHERE status = 'Cancelled'
""")

# Query 10 - Best Month per Region
run_query("BEST MONTH PER REGION", """
    SELECT region, month, SUM(revenue) as Revenue
    FROM sales
    GROUP BY region, month
    ORDER BY region, Revenue DESC
""")

conn.close()
print("\n✅ All SQL queries completed!")