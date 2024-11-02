# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:41:12 2024

@author: acarriou
"""


def ajoute_dictionnaires(d1,d2):
    d={}
    for cle, valeur in d1.items():
        if cle in d:
            d[cle] += valeur 
        else:
            d[cle] = valeur
    for cle, valeur in d2.items():
        if cle in d:
            d[cle] += valeur 
        else:
            d[cle] = valeur
    
    return d

assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}