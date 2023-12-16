import itertools
import random

Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'H', 'D', 'C', 'S'}
Cards = list(itertools.product(Ranks, Suits))
#4 cards same suit
def a(n):
    count = 0
    for i in range(n):
        cards = random.sample(Cards, 4)
        countH = sum(1 for card in cards if card[1] == 'H')
        countD = sum(1 for card in cards if card[1] == 'D')
        countC = sum(1 for card in cards if card[1] == 'C')
        countS = sum(1 for card in cards if card[1] == 'S')
        if(countH == 4 or countD == 4 or countC == 4 or countS == 4):
            count += 1
    print(count/n)        
# a(100)
# 4 cards are different suit
def b(n):
    count = 0
    for i in range(n):
        cards = random.sample(Cards, 4)
        countH = sum(1 for card in cards if card[1] == 'H')
        countD = sum(1 for card in cards if card[1] == 'D')
        countC = sum(1 for card in cards if card[1] == 'C')
        countS = sum(1 for card in cards if card[1] == 'S')
        if(countH == 1 and countD == 1 and countC == 1 and countS == 1):
            count += 1
    print(count / n)
# b(100)      
#cùng màu 
def c(n):
    count = 0
    for i in range(n):
        cards = random.sample(Cards, 4)
        countH = sum(1 for card in cards if card[1] == 'H')
        countD = sum(1 for card in cards if card[1] == 'D')
        countC = sum(1 for card in cards if card[1] == 'C')
        countS = sum(1 for card in cards if card[1] == 'S')
        if(countH == 0 and countD == 0) or (countC == 0 and countS == 0):
            count += 1
    print(count / n)
# c(100)
# tứ quí
def d(n):
    count = 0
    for i in range(n):
        cards = random.sample(Cards, 4)
        if(cards[0][0] == cards[1][0] == cards[2][0] == cards[3][0]):
            count += 1
    print(count / n)  
# d(100000)     
#cùng là số
def e(n):
    count = 0
    for i in range(n):
        cards = random.sample(Cards, 4)
        if(checkNum(cards[0][0]) and checkNum(cards[1][0]) and checkNum(cards[2][0]) and checkNum(cards[3][0])):
            count += 1
    print(count / n) 
def checkNum(n):
    check = False
    for i in range(10):
        if (n == i): 
            check = True
    return check
# e(100) 
#cùng là chữ
def f(n):
    count = 0
    for i in range(n):
        cards = random.sample(Cards, 4)
        if (checkChar(cards[0][0]) and checkChar(cards[1][0]) and checkChar(cards[2][0]) and checkChar(cards[3][0])):
            count += 1
    print(count / n) 
def checkChar(n):
    check = True
    for i in range(10):
        if (n == i): 
            check = False
    return check
f(100)