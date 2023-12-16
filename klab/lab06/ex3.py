import matplotlib.pyplot as plt
import math

def pmf_geo(p, x):
    return p*(1 - p)**(x-1)
# print(pmf_geo(0.4, 3))
def plot_pmf_geo(p, n):
    X = list(range(1, n+1))
    P_geo = [pmf_geo(p, x) for x in X]
    plt.plot(X, P_geo, '-o')
    plt.title('PMF of Geometric(%.2f)' %p)
    plt.xlabel('n')
    plt.ylabel('Probability')
    plt.show()
plot_pmf_geo(0.4, 10)