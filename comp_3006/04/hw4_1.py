from collections import Counter
import random

def rollDice(x, y):
    '''
    This function simulates rolling a fair, x-sided die, y times.
    Args:
        x (int): the number of sides of the die
        y (int): # of repeated observations
    Returns:
        (list): list of all rolled observations.
    '''
    results = []
    for i in range(y):
        results.append(random.randint(1,x))
    return results

if __name__ == '__main__':
    results = rollDice(6,100)
    print(Counter(results))
