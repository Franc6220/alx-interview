#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If the total is 0 or less, return 0.
             If the total cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin and update dp for each value from the coin's value to total
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means we can't make the amount with the given coins
    return dp[total] if dp[total] != float('inf') else -1
