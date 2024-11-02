# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:49:08 2024

@author: acarriou
"""


def fibonacci(n):
    nb1 = 1
    nb2 = 1
    while n > 2:
        nb1,nb2 = nb2,nb1 + nb2
        n-=1
    return nb2

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(25))