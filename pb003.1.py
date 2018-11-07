# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:41:26 2018

@author: user
"""

def primeNumbers(n):
    """
    n is an int >= 0
    returns the list of all prime numbers up to n.
    """
    result = []
    for num in range(2,n+1):
        if all(num%i != 0 for i in range(2,num)):
            result.append(num)
    return result

L = primeNumbers(10000)
#print(primeNumbers(60))

def largestPrimeFactor(num, primeList):
    """
    num is an int >= 0
    primeList is a list of prime
    returns the largest prime factor of the number num.
    """
    result = []
    for prime in L:
        if num%prime == 0:
            result.append(prime)
    return result, num/result[-1]

print(largestPrimeFactor(600851475143, L))
#print(largestPrimeFactor(87625999, L))
#print(largestPrimeFactor(59569, L))
        
def isPrimeNumber(num):
    """
    num is an int >= 0
    returns True if num is a prime number.
    """
    return all(num%i != 0 for i in range(2,num))

#print(isPrimeNumber(30))