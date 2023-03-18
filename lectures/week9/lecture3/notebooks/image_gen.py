# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:33:22 2022

@author: Nick
"""

import csv
from matplotlib import pyplot as plt

import numpy as np

X = []
y = []

with open('marks_vs_study.csv','r') as f:
    csv_file = csv.reader(f)
    next(csv_file)
    for line in csv_file:
        x = float(line[0])
        y = float(line[1])
        
        X.append([x, 1])
        y.append([y])
        
print(X)
print(y)