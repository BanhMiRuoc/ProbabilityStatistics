import itertools
import random
from fractions import Fraction

def cross(A, B):
    return [a + b for a in A for b in B]
Ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Suits = ['♡', '♢', '♣', '♠']
Cards = list(cross(Ranks, Suits))
# print(Cards)

B = list(itertools.combinations(Cards, 3))
A1 = []
A2 = []
for i in range(len(B)):
    count = 0
    for j in range(3):
        if B[i][j].count('K') == 1:
            count +=1
    if count == 2 or count == 1:
        A1.append(B[i])
    if count >= 1:
        A2.append(B[i])
print(len(A1)/len(B))
print(len(A2)/len(B))
