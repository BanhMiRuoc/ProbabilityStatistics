import matplotlib.pyplot as plt
import math
#example
def generator_data(a, b, size):
    n = (b-a)/(size - 1)
    result = []
    s = a
    while s < b:
        result.append(s)
        s += n
    if len(result) < size:
        result.append(b)
    return result
X = generator_data(4, 6, 100)
print(X)

def pmf_uniform_cont(a, b):
    return 1/(b-a)
def plot_pmf_uniform_cont(a, b):
    X = generator_data(a, b, 100)
    if b!= a:
        P = [pmf_uniform_cont(a, b) for x in X]
        
    plt.plot(X, P, '-')
    plt.plot([a, a], [0, 1/(b-a)], 'g--')
    plt.plot([b, b], [0, 1/(b-a)], 'g--')
    
    plt.title('PDF of Uniform continuous distribution(%0.2f, %0.2f)'%(a,b))
    
    plt.show()
plot_pmf_uniform_cont(4, 6)
#ex-1
def pmf_normal(x, mu, sigma):
    return 1.0/(math.sqrt(2*math.pi*sigma*sigma))*math.exp(-(pow(x-mu,2))/(2*sigma*sigma))
def cdf_normal(x, mu, sigma):
    return (0.5*(1 + math.erf((x - mu)/(sigma*math.sqrt(2)))))

def plot_pmf_normal(mu, sigma):
    
    X = generator_data(mu - 4*sigma, mu + 4*sigma, 1000)
    P_normal = [pmf_normal(x, mu, sigma) for x in X]
    plt.plot(X, P_normal, '-')
    plt.title('PMF of Normal(%.2f, %.2f)' %(mu, sigma))
    plt.xlabel('X')
    plt.ylabel('P')
    plt.show()
plot_pmf_normal(0, 1.5)
def plot_cdf_normal(mu, sigma):
    X = generator_data(mu - 4*sigma, mu + 4*sigma, 1000)
    C_normal = [cdf_normal(x, mu, sigma) for x in X]
    plt.plot(X, C_normal, '-')
    plt.title('CDF of Normal(%.2f, %.2f)' %(mu, sigma))
    plt.xlabel('X')
    plt.ylabel('P')
    plt.show()
plot_cdf_normal(0, 1.5)   
'''
1) P(Z < 1.51) = phi(1.51) = .9345
2) P(Z <= 2.13) = phi(2.13) = .9834
3) P(Z < -0.87) = phi(-0.87) = 1 - phi(0.87) = 0.1922
4) P(Z > 1.11) = 1 - P(Z <= 1.11) = 0.1335
5) P(Z > -0.66) = 1 - P(Z <= -0.66) = 1 - phi(-0.66) = 1 - [1 - phi(0.66)] = 0.7454
6) P(0.28 < Z < 1.31) = phi(1.31) - phi(0.28) = 0.9049 - 0.6103 = 0.2946
7) P(-0.86 < Z < 0.12) = phi(0.12) - (1  - phi(0.86)) = 0.5478 - 0.1949 =  0.3529
8) P(-2.2 < Z < -0.16) = phi(-0.16) - phi(-2.2) = (1 - phi(0.16)) - (1 - phi(2.2)) = 0.4364 - 0.0139 = 0.4225
9) X ~ N (20, 3^2) & P(18 < X < 21) = P (Z < (21 - 20)/3) - P(Z < (18 - 20)/3)  = phi(0.33) - (1 - phi(0.67)) = 0.6293 - 0.2514 = 0.3779
10) X ~ N (1.5, 0.1^2) & P(-0.5 < X < 0.5) = P(Z < (0.5-1.5)/0.1) - P(Z < (-0.5-1.5)/0.1) = P(-10) -  P(-20) = 0
'''
print("1/ ",cdf_normal(1.51, 0, 1))
print("2/ ",cdf_normal(2.13, 0, 1))
print("3/ ",cdf_normal(-0.87, 0, 1))
print("4/ ",1 - cdf_normal(1.11, 0, 1))
print("5/ ",1- cdf_normal(-0.66, 0, 1))
print("6/ ",cdf_normal(1.31, 0, 1) - cdf_normal(0.28,0,1))
print("7/ ",cdf_normal(0.12, 0, 1) - cdf_normal(-0.86,0,1))
print("8/ ",cdf_normal(-0.16, 0, 1) - cdf_normal(-2.2,0,1))
print("9/ ",cdf_normal(21, 20, 3) - cdf_normal(18,20,3))
print("10/ ",cdf_normal(0.5, 1.5, 0.1) - cdf_normal(-0.5,1.5,0.1))
#ex2
# X ~ N (10, 1^2) & (9 < X < 12) = P(Z < (12-10)) - P(Z < (9-10)) = phi(2) - phi(-1) = 0.9772 - (1-0.8413) = 0.8185
print("ex2 ", cdf_normal(12,10,1) - cdf_normal(9,10,1))
