# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:57:40 2018

@author: user
"""

def fibUpTo(n):
    """
    n is an int
    calculates the terms in the Fibonacci sequence whose values do not exceed n
    returns the sum of the even-valued terms
    """
    fibTerms = [1,2]
    term = 0
    result = 2
    while term < n:
        term = fibTerms[-1] + fibTerms[-2]
        fibTerms.append(term)
        if term%2 == 0:
            result += term
    return result

print(fibUpTo(4000000))