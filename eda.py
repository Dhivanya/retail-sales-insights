import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sales_data.csv')

print("=== DATASET INFO ===")
print(f"Rows: {len(df)}")
print(f"Columns: {df.columns.tolist()}")
print(f"\nMissing values:\n{df.isnull().sum()}")

print("\n=== BUSINESS INSIGHTS ===")
print(f"Total Revenue: ₹{df['revenue'].sum():,.0f}")
print(f"Average Order Value: ₹{df['revenue'].mean():,.0f}")
print(f"Best Selling Product: {df.groupby('product')['revenue'].sum().idxmax()}")
print(f"Best Region: {df.groupby('region')['revenue'].sum().idxmax()}")
print(f"Best Month: {df.groupby('month')['revenue'].sum().idxmax()}")

# Revenue by product
plt.figure(figsize=(10, 5))
df.groupby('product')['revenue'].sum().sort_values().plot(
    kind='barh', color='steelblue')
plt.title('Revenue by Product')
plt.xlabel('Total Revenue')
plt.tight_layout()
plt.savefig('revenue_by_product.png')
plt.show()
print("\nChart saved!")