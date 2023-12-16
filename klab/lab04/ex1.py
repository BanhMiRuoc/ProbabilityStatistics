#Rolling two fair dice. Write a function to calculate 
# the practical probability of the following evens
# with n times of experiments. 
import random
#both dice are the same
def a(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if(dice1 == dice2):
            count+=1
    print(count/n)
#both dice are different
def b(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if(dice1 != dice2):
            count+=1
    print(count/n)
#both dice are even
def c(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if(dice1%2 == 0 and dice2%2 == 0):
            count+=1
    print(count/n)
#both dice are odd
def d(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if(dice1%2 != 0 and dice2%2 != 0):
            count+=1
    print(count/n)
#one even dice, other is odd
def e(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if((dice1 + dice2)%2 != 0):
            count+=1
    print(count/n)
#both dice are 6
def f(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == dice2 == 6:
            count+=1
    print(count/n)
#sum of both dice are greater than 10
def g(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 + dice2 > 10):
            count += 1
    print(count/n)
    
a(100)
b(100)
c(100)
d(100)
e(100)
f(100)
g(100)


          
        