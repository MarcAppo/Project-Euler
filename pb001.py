# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:51:24 2018

@author: user
"""

def sum3and5multiple(n):
    """
    n an int >= 0
    returns the sum of all the multiples of 3 or 5 below n
    """
    result = 0
    for num in range(n):
        if num%3 == 0 or num%5 ==0:
            result += num
    return result

print(sum3and5multiple(1000))