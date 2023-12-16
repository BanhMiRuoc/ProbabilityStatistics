import matplotlib.pyplot as plt
import math

def pmf_bernoulli(p, x):
    if x == 1:
        return p
    if x == 0:
        return 1 - p
    
def pmf_binom(k, n, p):
    n_k = math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
    return n_k*pow(p, k)*pow(1-p, n-k)

def plot_pmf_binom(n, p):
    K = list(range(0, n+1))
    P_binom = [pmf_binom(k, n, p) for k in K]
    plt.plot(K, P_binom, '-o')
    axes = plt.gca()
    axes.set_xlim([0, n])
    axes.set_ylim([0, 1.1 * max(P_binom)])
    plt.title('PMF of Bin(%i, %.2f)' % (n,p))
    plt.xlabel('Number k of successes')
    plt.ylabel('Probability of k successes')
    plt.show()
# plot_pmf_binom(15, 0.5)
    
def plot_pmf_bernoulli(p):
    X = [0, 1]
    P_bernoulli = [pmf_bernoulli(p, x) for x in X]
    plt.plot(X, P_bernoulli, 'o')
    
    plt.title('PMF of Bernoulli(p=%.2f)' %(p))
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()
# plot_pmf_bernoulli(0.5)
def pmf_poisson(k, lam):
    return (math.pow(lam, k) * math.exp(-lam))/ math.factorial(k)
def plot_pmf_poisson(n, lam):
    K = list(range(0, n + 1))
    P_poisson = [pmf_poisson(k, lam) for k in K]
    plt.plot(K, P_poisson, '-o')
    plt.title('PMF of Poisson(%i)' %lam)
    plt.xlabel('Number of Events')
    plt.ylabel('Probability of Number of Events')
    plt.show()
# plot_pmf_poisson(25, 5)
def pmf_geo(p, x):
    return p*(1 - p)**(x-1)
def plot_pmf_geo(p, n):
    X = list(range(1, n+1))
    P_geo = [pmf_geo(p, x) for x in X]
    plt.plot(X, P_geo, '-o')
    plt.title('PMF of Geometric(%.2f)' %p)
    plt.xlabel('n')
    plt.ylabel('Probability')
    plt.show()
plot_pmf_geo(0.3, 10)
