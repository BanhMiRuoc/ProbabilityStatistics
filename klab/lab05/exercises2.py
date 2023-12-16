import random, math

def flip_2_coins():
  heads = 0
  for i in range(2):
    if random.random() < 0.5:
      heads += 1
  return heads
#a
x = []
for i in range(10000):
  x.append(flip_2_coins())
#b'
X = set(x)
#c
P = [x.count(i)/len(x) for i in X]
print(P)
#d
expectation = sum(x) / len(x)
variance = sum((xi - expectation)**2 for xi in x) / len(x)
standard_deviation = variance**0.5

probability_at_least_one_head = 1 - x.count(0) / 10000

print("Expectation of random variable X:", expectation)
print("Variance of random variable X:", variance)
print("Standard deviation of random variable X:", standard_deviation)

print("Probability to have at least one head:", probability_at_least_one_head)