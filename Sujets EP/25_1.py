#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:59:24 2024

@author: monordi
"""
def recherche_min(tab):
    return tab.index(min(tab))


"""
def recherche_min(tab):
    minimum = tab[0]
    indiceMinimum = 0
    for indiceNombre in range(1,len(tab)-1):
        if tab[indiceNombre] < minimum:
            indiceMinimum = indiceNombre
            minimum = tab[indiceNombre]
    return minimum
"""
assert recherche_min([5, 3, 2, 2, 4]) == 2
assert recherche_min([-5, 8, 96, -9856, 0]) == 3
assert recherche_min([0]) == 0
assert recherche_min([0, 55, 0]) == 0
assert recherche_min([0, 55, -10]) == 2
assert recherche_min([7, -2, 4, -2, 3, 1]) == 1
