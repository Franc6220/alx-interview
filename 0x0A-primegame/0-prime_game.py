#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """ Returns a list where True means the index is prime """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(n**0.5)  + 1):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
    return primes

def isWinner(x, nums):
    """
    Determines the winner after x rounds of the Prime Game.

    x: Number of rounds.
    nums: List of n values for each round.

    Returns the name of the player with the most wins (Maria or Ben),
    or None if the result is a tie.
    """
    if not nums or x < 1:
        return None

    # Precompute prime numbers up to the maximum possible n (10,000)
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Array to store the number of primes <= i for each i
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Variables to track the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
