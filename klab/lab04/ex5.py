import random
import itertools
def cross(A, B):
    return {a + b for a in A for b in B}
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
Suits = {'H', 'D', 'S', 'C'}

Cards = list(itertools.product(Ranks, Suits))
a = list(itertools.combinations(Cards, 5))
random.shuffle(a)
# print(len(a))
def ca(n):
    counta = 0
    for i in range(n):
        check = True
        for j in range(4, 0, -1):
            if a[i][j][0] - a[i][j-1][0] != 1:
                check = False
        if(check):
            counta+=1    
    print(counta/n)
# ca(len(a))
def b(n):
    countb = 0
    for i in range(n):
        a1 = random.sample(Cards, 5)
        check = True
        for j in range(4, 0, -1):
            if a1[j][0] - a1[j-1][0] != 1:
                check = False
        if(check):
            countb+=1 
    print((countb/n))
b(100000)