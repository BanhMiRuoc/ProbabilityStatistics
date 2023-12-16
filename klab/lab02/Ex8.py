import itertools
import random

def cross(A, B):
    return {a + b for a in A for b in B}

urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')

def combos(items, n):
    return {' '.join(combo) for combo in itertools.combinations(items, n)}

U6 = combos(urn, 6)
def simultor_ball(n):
    count = 0
    for j in random.sample(list(U6), n):
        if (j.count('B') == 2 and j.count('W') == 2 and j.count('R') == 2 ):
            count +=1
    return count/n
        
print(simultor_ball(1000))