# -*- coding: utf-8 -*-
"""
Created on Thu May  3 01:43:51 2018

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

def facto(seq):
    """
    seq is a sequence of int >= 0
    returns factorial of the seq.
    """
    result = 1
    for i in seq:
        result *= i
    return result

def smallestMultiple(x = 10):
    """
    x is an int >= 0
    Finds the smallest positive number that is evenly divisible
    by all of the numbers from 1 to x
    """
    result = facto(primeNumbers(x)) * 2520# smallestMultiple(10) = 2520
    for p in primeNumbers(10):
        test = result / p
        print('testing', test)
        if all(test%i == 0 for i in range(1,x+1)):
            result = test
    return result
    
print(smallestMultiple(20))