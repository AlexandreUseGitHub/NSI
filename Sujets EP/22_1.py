# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:27:13 2024

@author: acarriou
"""


def recherche_indices_classement(elt, tab):
    l1,l2,l3 = [],[],[]
    for indice in range(len(tab)):
        if tab[indice] < elt: l1.append(indice)
        if tab[indice] == elt: l2.append(indice)
        if tab[indice] > elt: l3.append(indice)
    return (l1,l2,l3)

assert recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]) == ([0, 3, 7], [1, 6], [2, 4, 5])
assert recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]) == ([0, 2, 5], [], [1, 3, 4])
assert recherche_indices_classement(3, [1, 1, 1, 1]) == ([0, 1, 2, 3], [], [])
assert recherche_indices_classement(3, []) == ([], [], [])
