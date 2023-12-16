import random
def simultor_dice4(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == 1 and dice2 == 6:
            count += 1
    return count/n
print(simultor_dice4(1000))