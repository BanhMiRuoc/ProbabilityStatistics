import itertools
import random
def simualtor_poker1(n):
    Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
    Suits = {'H', 'D', 'C', 'S'}
    Cards = list(itertools.product(Ranks, Suits))
    
    count = 0
    for i in range(n):
        cards = random.sample(Cards, 5)
        countH = sum(1 for card in cards if card[1] == 'H')
        if(countH == 5):
            count += 1
    return count / n        
print(simualtor_poker1(10000))

