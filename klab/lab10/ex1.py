import numpy as np

# a
x = []
for i in range(10000):
    dice1 = np.random.randint(1, 7)
    dice2 = np.random.randint(1, 7)
    x.append(dice1 + dice2)

#b
X = np.unique(x)

#c
P = []
for value in X:
    count = x.count(value)
    probability = count / len(x)
    P.append(probability)

#d
exp = np.mean(x)
var = np.var(x)
standard_deviation = np.std(x)

print("Values of random variable X:", X)
print("Probability distribution function P(X):", P)
print("Expectation:", exp)
print("Variance:", var)
print("Standard deviation:", standard_deviation)