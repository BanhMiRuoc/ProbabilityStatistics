import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

# Hàm mật độ xác suất của phân phối normal
def pmf_normal(x, mu, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-((x - mu)**2) / (2 * sigma**2))

# Hàm phân phối tích lũy của phân phối normal
def cdf_normal(x, mu, sigma):
    return 0.5 * (1 + erf((x - mu) / (sigma * np.sqrt(2))))

# (a) Vẽ đồ thị mật độ xác suất
x_values = np.linspace(-10, 10, 1000)
pdf_values = pmf_normal(x_values, 3, 4)

plt.plot(x_values, pdf_values, label='PDF - Normal Distribution')
plt.title('Probability Density Function of Normal Distribution')
plt.xlabel('X')
plt.ylabel('p(X)')
plt.legend()
plt.show()

# (b) Vẽ đồ thị phân phối tích lũy
cdf_values = cdf_normal(x_values, 3, 4)

plt.plot(x_values, cdf_values, label='CDF - Normal Distribution')
plt.title('Cumulative Distribution Function of Normal Distribution')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.legend()
plt.show()

# (c) Tính xác suất P{2 < X < 7} cho biến ngẫu nhiên X với mean mu=3 và phương sai sigma**2=16
lower_bound = 2
upper_bound = 7
probability_range = cdf_normal(upper_bound, 3, 4) - cdf_normal(lower_bound, 3, 4)

print(f"P{{2 < X < 7}} = {probability_range}")