import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# Phần 3
# Đọc văn bản và tìm tần suất của từng từ
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Tách từ bằng cách sử dụng regex
words = re.findall(r'\b\w+\b', text.lower())

# Tính tần suất của từng từ
word_freq = Counter(words)

# Lấy 30 từ phổ biến nhất và vẽ đồ thị line plot
common_words = word_freq.most_common(30)
plt.figure(figsize=(15, 6))
plt.plot(*zip(*common_words), marker='o', linestyle='-', color='b')
plt.title('30 Most Common Words')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.show()
