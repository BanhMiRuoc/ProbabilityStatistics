#Given a close urn with 
# 2 blue balls, 3 red balls and 5 white balls.
# Choose 3 balls from the urn. Write an
# function to calculate the practical
# probability of the following evens 
# with n times of experiments.
import random
import itertools

def cross(A, B):
    return {a + b for a in A for b in B}
urn = cross('B', '12') | cross('R', '123') | cross('W', '12345')

def combos(items, n):
    return {' '.join(combo) for combo in itertools.combinations(items, n)}

U3 = combos(urn, 3)
#3 balls are same color
def a(n):
    count = 0
    if n > len(U3): n =len(U3)
    a = random.sample(list(U3), n)
    for i in a:
        if i.count('R') == 3 or i.count('B') == 3 or i.count('W') == 3:
            count +=1
    print(count/n)  
a(100)  
# 3 balls are different colors
def b(n):
    count = 0
    if n > len(U3): n =len(U3)
    a = random.sample(list(U3), n)
    for i in a:
        if i.count('R') == 1 and i.count('B') == 1 and i.count('W') == 1:
            count +=1
    print(count/n)  
b(100) 
#2 balls are same color
def c(n):
    count = 0
    if n > len(U3): n =len(U3)
    a = random.sample(list(U3), n)
    for i in a:
        if i.count('R') == 2 or i.count('B') == 2 or i.count('W') == 2:
            count +=1
    print(count/n)  
c(100) 
#2 red balls and 1 white ball
def d(n):
    count = 0
    if n > len(U3): n =len(U3)
    a = random.sample(list(U3), n)
    for i in a:
        if i.count('R') == 2 and i.count('W') == 1:
            count +=1
    print(count/n)  
d(100) 
# list all the cases that all 3 balls are white
def d():
    for i in U3:
        if i.count('W') == 3:
            print(i)
d()
       

            
