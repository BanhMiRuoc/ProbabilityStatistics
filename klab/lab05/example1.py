import random, math
#random number of (1, 6)  
x = [random.randint(1, 6) for i in range(8000)]
X = set(x)
print(x)
print(X)
#probability to each value 
P = [x.count(i)/len(x) for i in X]
print(P)
#sum of probabilyty 1, 2, 3
FX = sum(P[:3])
print(FX)
#expectation of random variable
EX = 0
for x in X:
    EX += EX + (x*P[x-1])
print(EX)

VarX = 0
for x in X:
    VarX += + (x-EX)*(x-EX)*P[x-1]
print(VarX)

SD = math.sqrt(VarX)
print(SD)
    