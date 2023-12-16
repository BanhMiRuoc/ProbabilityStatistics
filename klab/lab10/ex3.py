import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
file_path = 'company-sales_data.csv'
data = pd.read_csv(file_path)

# Extracting data for toothpaste, shampoo, and facecream
products_of_interest = ['toothpaste', 'shampoo', 'facecream']
months = data['month_number']

# Selecting only the required columns for products of interest
products_data = data[['toothpaste', 'shampoo', 'facecream']]

# Plotting the data using a line chart
plt.figure(figsize=(10, 6))

for product in products_of_interest:
    plt.plot(months, products_data[product], marker='o', label=product)

plt.xlabel('Month')
plt.ylabel('Sales Units')
plt.title('Monthly Sales of Toothpaste, Shampoo, and Facecream')
plt.xticks(months)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the line chart
plt.show()