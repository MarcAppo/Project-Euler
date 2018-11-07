# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:01:18 2018

@author: user
"""

#A palindromic number reads the same both ways. The largest palindrome made
#from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def reverse(n):
    """
    n is an int > 0
    return reversed n such has if n = 123, reversed n = 321
    """
    Reversed = 0
    while n > 0:
        Reversed = 10 * Reversed + n%10
        n = n//10
    return Reversed

#print(reverse(123))

def isPalindrome(x):
    '''
    x is an int >= 0.
    returns True if x is a palindromic number
    '''
    return  x == reverse(x)

def largestPalindromicNum(firstProduct = 999):
    """
    Finds the largest palindrome made from the product of two 3-digit numbers.
    """
    maxPalindrome = 0
    for i in range(firstProduct, firstProduct//10, -1):
        for j in range(i, firstProduct//10, -1):
            if isPalindrome(i*j) and i*j > maxPalindrome:
                maxPalindrome = i*j
                result = (maxPalindrome, i, j)
    return result

print(largestPalindromicNum())

def previousPalindrome(biggest = 999999):
    """
    biggest is a 6 digit palindromic number.
    returns the previous 6 digit palindromic number.
    """
    leftpart = biggest//1000 - 1
    firstDigit, lastDigit = leftpart//100, leftpart%10
    rightpart = leftpart - (firstDigit - lastDigit) * 99
    previousPalindrome = leftpart*1000 + rightpart
    return previousPalindrome

def largestPalindrome(palindrome = 999999, firstProduct = 999):
    """
    Finds the largest palindrome made from the product of two 3-digit numbers.
    this function finds the optimal solution (906609, 993, 913)
    """
    while palindrome > 100000:
        print('testing', str(palindrome))
        for i in range(firstProduct, 99, -1):
            print(str(palindrome), '%', str(i), '=', str(palindrome%i))
            if palindrome%i == 0 and 100 <= palindrome//i <= 999:
                return (palindrome, i, palindrome/i)
        palindrome = previousPalindrome(palindrome)
    return None

#print(largestPalindrome(906609))

def generate6digitsPalindromes(high = 999999, low = 100000):
    """
    Generates all palindromic numbers 
    """
    result = []
    palindrome = high
    while palindrome > low:
        result.append(palindrome)
        palindrome = previousPalindrome(palindrome)
    return result

#print(generate6digitsPalindromes(palindrome = 999999))
