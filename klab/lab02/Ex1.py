import random
def simualtor_dice1(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1%2 == 0 and dice2%2 == 0:
            count += 1
    return count/n
print(simualtor_dice1(1000))