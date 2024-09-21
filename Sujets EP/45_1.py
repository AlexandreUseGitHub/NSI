#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:45:29 2024

@author: monordi
"""
def compte_occurrences(element_a_rechercher, tab_de_recherche):
    total=0
    for element_a_tester in tab_de_recherche:
        if element_a_tester == element_a_rechercher:
            total +=1
    return total

compte_occurrences(5, [])
compte_occurrences('a', ['a','b','c','a','d','e','a'])
compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4])