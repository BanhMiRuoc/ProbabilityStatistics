import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
#part1
iris_data = pd.read_csv('iris.csv')

plt.figure(figsize=(10, 6))
plt.scatter(iris_data['sepal_length'], iris_data['sepal_width'])
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(iris_data['sepal_length'], bins=20, edgecolor='black')
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()
#part2
sales_data = pd.read_csv('company-sales_data.csv')

plt.figure(figsize=(10, 6))
plt.plot(sales_data['month_number'], sales_data['total_profit'], marker='o', linestyle='-')
plt.title('Total Profit Over Months')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(sales_data['month_number'], sales_data['toothpaste'])
plt.title('Toothpaste Sales Over Months')
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(sales_data['month_number'], sales_data['facecream'], width=0.4, label='Facecream', align='edge')
plt.bar(sales_data['month_number'], sales_data['facewash'], width=-0.4, label='Facewash', align='edge')
plt.title('Facecream and Facewash Sales Over Months')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend()
plt.show()
#part2
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = re.findall(r'\b\w+\b', text.lower())

word_freq = Counter(words)

common_words = word_freq.most_common(30)
plt.figure(figsize=(15, 6))
plt.plot(*zip(*common_words), marker='o', linestyle='-', color='b')
plt.title('30 Most Common Words')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.show()
