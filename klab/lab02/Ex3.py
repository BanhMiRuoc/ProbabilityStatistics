import random
def simultor_dice3(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == dice2:
            count +=1
    return count/n
print(simultor_dice3(100000))