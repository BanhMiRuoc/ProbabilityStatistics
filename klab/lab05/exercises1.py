import math
import numpy as np

#a
x = np.random.choice([0, 1, 2, 3, 4, 5], 3650, p = [0.1, 0.2, 0.3, 0.2, 0.15, 0.05])
# print(x)
x = list(x)
X = set(x)
# print(x)

#b
P = [x.count(i)/len(x) for i in X]
print(P)

#c
#Mean
EX = 0
for x in X:
    EX += (x * P[x - 1])
print("Mean", EX)

#Variance
VarX = 0
for x in X:
    VarX += (x - EX)*(x - EX)*P[x - 1]
print("Variance", VarX)

#Standard Deviation
SD = math.sqrt(VarX)
print("Standard Deviation", SD)

#d
FX = sum(P[3:])
print(FX)