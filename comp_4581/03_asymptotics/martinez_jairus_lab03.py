import os
import math
import random
from time import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

FILENAME = 'factor_time.csv'

def isPrime(n: int):
    """
    Check if a number is prime.
    Args:
        n (int): The number to check.
    Returns:
        bool: True if the number is prime, False otherwise.
    The function performs the following checks:
        1. Returns False if n is less than 2, as numbers less than 2 are not prime.
        2. Returns True if n is 2, as 2 is the smallest prime number.
        3. Returns False if n is even and greater than 2.
        4. For odd numbers greater than 2, the function checks divisibility
           from 3 up to the square root of n, skipping even numbers.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def nBitPrime(n: int):
    """
    Generate a random prime number that is up to n bits long.
    Args:
        n (int): The number of bits.
    Returns:
        int: A random prime number up to n bits long.
    """
    if n < 1:
        raise ValueError("Number of bits must be at least 1")

    while True:
        random_number = int(random.random() * (2**n))
        if random_number >= 2 and isPrime(random_number):
            return random_number
        
def factor(pq: int):
    """
    Factorize a number into two prime factors.
    Args:
        pq (int): The number to be factorized, which is a product of two primes.
    Returns:
        tuple: A tuple containing the two prime factors (P, Q).
    """
    for i in range(2, int(math.sqrt(pq)) + 1):
        if pq % i == 0:
            P = i
            Q = pq // i
    return P, Q

def time_rsa_factor(function, pq: int):
    """
    Timing function for factor of RSA algos.
    Args:
        function (function): sorting function
        pq (int): The number to be factorized, which is a product of two primes.
    Returns:
        float: Time in milliseconds 
    """
    t1 = time()
    function(pq)
    t2 = time()
    return (t2 - t1) * 1000

def exponential_func(n: int, a: float, b: float):
    """Exponential function to fit"""
    return a * np.exp(b * n)

# NOTE: I think this is effective for large primes bc it removes a lot of unecessary numbers and cuts the cost for computation 
def sieve_of_eratosthenes(n: int):
    """
    Implements the Sieve of Eratosthenes algorithm to find all prime numbers up to a specified integer n.
    Args:
    n (int): The upper limit (inclusive) to find primes up to.
    Returns:
    list: A list of prime numbers up to n.
    """
    m = int(math.sqrt(n)) + 1
    primes = [x for x in range(n+1)]
    for i in range(2, m):
        for num in primes[:]:
            if num % i == 0:
                primes.remove(num)
    return primes

if __name__ == '__main__':

    print('\nPart 1: Generating PQ and Factoring\n')
    n = 10
    pq = nBitPrime(n) * nBitPrime(n)
    print(f'PQ = {pq}')

    print('Factors of PQ using factor():')
    print(factor(pq))

    print('\nPart 2: Timing the RSA Factor and Fitting Exponential Curve\n')
    if os.path.exists(FILENAME):
        df = pd.read_csv(FILENAME)
        print(df)
    else:
        data = []
        print(f"{'n':<8}{'Time_ms':<9}")
        for n in range(10, 34, 1):
            pq = nBitPrime(n) * nBitPrime(n)
            factor_time = time_rsa_factor(factor, pq)

            data_entry = {
                'n': n,
                'time_ms': factor_time
                }
            
            data.append(data_entry)
            
            print(f"{n:<8}{round(factor_time, 2):<9}")

        # save the data into a pandas df
        df = pd.DataFrame(data)
        df['time_years'] = df['time_ms'] * (1 / (1000 * 60 * 60 * 24 * 365.25))
        df.to_csv(FILENAME, index=False)

    n_data = df['n']
    time_data = df['time_ms']

    # Perform curve fitting
    params, covariance = curve_fit(exponential_func, n_data, time_data)

    # Extract parameters
    a_fit, b_fit = params

    # Predicted values using the fitted parameters
    time_fit = exponential_func(n_data, a_fit, b_fit)

    # Plotting the data and the fit
    plt.figure(figsize=(8, 6))
    plt.scatter(n_data, time_data)
    plt.plot(n_data.values, time_fit.values, label='Exponential Fit', color='red')
    plt.xlabel('n (n-bit Prime in pq = nBitPrime(n) * nBitPrime(n))')
    plt.ylabel('Time (ms)')
    plt.title('Exponential Fit of Factor Time vs. n-bit Prime, PQ')
    plt.legend()
    plt.grid(True)
    plt.show()

    print('\nPart 3: Prediction for n = 1024\n')
    # Prediction (n = 1024)
    ms_to_years = 1 / (1000 * 60 * 60 * 24 * 365.25)
    ms = exponential_func(np.array([1024], dtype=np.float128), a_fit, b_fit)[0]
    years = ms * (ms_to_years)
    print(f'\nEstimated milliseconds to Crack RSA:\n')
    print(ms)
    print(f'\nEstimated Years to Crack RSA:\n')
    print(years)

    print('\nPart 4: Sieve of Eratosthenes Implementation\n')
    # OPTIONAL SIEVE OF ERATOSTHENES
    n = 71
    print(f'n = {n}')
    prime_nums = sieve_of_eratosthenes(n)
    print(f'Primes: {prime_nums}')
    

# TERMINAL OUTPUT
# 
# Part 1: Generating PQ and Factoring
# 
# PQ = 200647
# Factors of PQ using factor():
# (283, 709)
# 
# Part 2: Timing the RSA Factor and Fitting Exponential Curve
# 
#      n         time_s        time_ms    time_years
# 0   10       0.056028       0.056028  1.775432e-12
# 1   11       0.031948       0.031948  1.012374e-12
# 2   12       0.118017       0.118017  3.739739e-12
# 3   13       0.504971       0.504971  1.600155e-11
# 4   14       0.577927       0.577927  1.831339e-11
# 5   15       1.029015       1.029015  3.260750e-11
# 6   16       1.822948       1.822948  5.776575e-11
# 7   17       0.725985       0.725985  2.300506e-11
# 8   18      15.141010      15.141010  4.797897e-10
# 9   19       3.506899       3.506899  1.111269e-10
# 10  20      15.697956      15.697956  4.974382e-10
# 11  21      36.669970      36.669970  1.162001e-09
# 12  22     184.776783     184.776783  5.855223e-09
# 13  23     470.363140     470.363140  1.490491e-08
# 14  24     486.286879     486.286879  1.540950e-08
# 15  25    1340.820074    1340.820074  4.248802e-08
# 16  26     926.338196     926.338196  2.935389e-08
# 17  27    2096.360922    2096.360922  6.642967e-08
# 18  28    3960.906029    3960.906029  1.255135e-07
# 19  29   24859.257221   24859.257221  7.877423e-07
# 20  30   58067.410946   58067.410946  1.840045e-06
# 21  31  120915.258884  120915.258884  3.831573e-06
# 22  32  230714.211941  230714.211941  7.310892e-06
# 23  33  770302.471876  770302.471876  2.440941e-05
# 
# FITTED EXPONENTIAL CURVE PLOT IS PLOTTED AS PNG - ATTATCHED TO SUBMISSION
#
# Part 3: Prediction for n = 1024
# 
# Estimated milliseconds to Crack RSA:
# 
# 1.5434646716561617878e+464
# 
# Estimated Years to Crack RSA:
# 
# 4.8909444053291811954e+453
# 
# Part 4: Sieve of Eratosthenes Implementation
# 
# n = 71
# Primes: [1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]