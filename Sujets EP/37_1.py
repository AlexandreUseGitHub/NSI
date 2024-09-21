#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:34:41 2024

@author: monordi
"""
def moyenne(tab):
    if tab == []:
        return None
    total=0
    for valeur in tab:
        total += valeur
    return total/len(tab)

moyenne([1,2,3,4,5,6,7,8,9,10])
