import random
import itertools
def simualtor_poker2(n):
    Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
    Suits = {'H', 'D', 'C', 'S'}
    Cards = list(itertools.product(Ranks, Suits))

    count = 0
    for i in range(n):
        cards = random.sample(Cards, 4)
        
        if(cards[0][1] != cards[1][1] != cards[2][1] != cards[3][1]):
            count += 1
    return count / n       
print(simualtor_poker2(100))
