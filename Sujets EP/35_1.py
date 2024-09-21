#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:39:55 2024

@author: monordi
"""
def annee_temperature_minimale(t_moy,annes):
    return (min(t_moy),annes[t_moy.index(min(t_moy))])


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
assert annee_temperature_minimale(t_moy, annees) == (12.5, 2016)