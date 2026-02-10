# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 12:02:13 2026

@author: HP
"""

import numpy as np

scores=np.random.randint(50,101,size=(5,3))

mean_scores=scores.mean(axis=0)
centered_scores=scores-mean_scores

print("original Scores (5 Students, 3 Subjects) : ")
print(scores)

print("\nMean of each subject : ")
print(mean_scores)

print("\nCentered Scores : ")
print(centered_scores)