import matplotlib.pyplot as plt
import math

def pmf_poisson(k, lam):
    return (math.pow(lam, k) * math.exp(-lam))/ math.factorial(k)
print(pmf_poisson(2,3))
def plot_pmf_poisson(n, lam):
    K = list(range(0, n + 1))
    P_poisson = [pmf_poisson(k, lam) for k in K]
    plt.plot(K, P_poisson, '-o')
    plt.title('PMF of Poisson(%i)' %lam)
    plt.xlabel('Number of Events')
    plt.ylabel('Probability of Number of Events')
    plt.show()
plot_pmf_poisson(5, 3)