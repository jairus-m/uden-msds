from time import time

def DACcoins(coins, amount):
    """
    Calcs the minimum number of coins required to produce the given amount of change
    using a divide-and-conquer approach. Copied from example in lab. 
    Args:
        coins (list): coin values
        amount (int): amount of change you want
    Returns:
        int: min number of coins required to make change
    """
    if amount == 0:  # The base case
        return 0
    else:  # The recursive case
        minCoins = float("inf")
        for currentCoin in coins:  # Check all coins
            # If we can give change
            if (amount - currentCoin) >= 0:
                # Calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) + 1
                # Keep the best
                minCoins = min(minCoins, currentMin)
        return minCoins

def DPcoins(coins, amount):
    """
    Calcs the minimum number of coins required to produce the given amount of change
    using a dynamic programming approach... also prints the coins used to produce the optimal number.
    Args:
        coins (list): coin values
        amount (int): amount of change you want
    Returns:
        int: min number of coins required to make change
    """
    # Create the initial tables
    min_coins = [float("inf")] * (amount + 1)
    coins_used = [-1] * (amount + 1)
    
    # Fill in the base case(s)
    min_coins[0] = 0  
    
    # Fill in the rest of the table
    for sub_amount in range(1, amount + 1):
        for coin in coins:
            if sub_amount >= coin:
                if min_coins[sub_amount - coin] + 1 < min_coins[sub_amount]:
                    min_coins[sub_amount] = min_coins[sub_amount - coin] + 1
                    coins_used[sub_amount] = coin
    
    # Perform the traceback to print result
    final_coins = []
    trace_amount = amount
    while trace_amount > 0:
        final_coins.append(coins_used[trace_amount])
        trace_amount -= coins_used[trace_amount]
    
    print(final_coins)  # Display the actual coins used
    return min_coins[amount] # return optimal number of coins

if __name__ == '__main__':

    C = [1, 5, 10, 12, 25]  # coin denominations (must include a penny)
    A = 29 # int(input('Enter desired amount of change: '))
    assert A >= 0

    print("DAC:")
    t1 = time()
    numCoins = DACcoins(C, A)
    t2 = time()
    print("optimal:", numCoins, " in time: ", round((t2 - t1) * 1000, 1), "ms")
    print()

    print("DP:")
    t1 = time()
    numCoins = DPcoins(C, A)
    t2 = time()
    print("optimal:", numCoins, " in time: ", round((t2 - t1) * 1000, 1), "ms")

# TERMINAL OUTPUT
# DAC:
# optimal: 3  in time:  7.7 ms
# 
# DP:
# [5, 12, 12]
# optimal: 3  in time:  0.1 ms