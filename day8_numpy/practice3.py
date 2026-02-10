# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:09:07 2026

@author: HP
"""

import numpy as np
arr=np.arange(12)
reshaped=arr.reshape(3,4)
print(reshaped)


a=np.array([[1,2]])
b=np.array([[3,4]])
vstacked=np.vstack((a,b))
print(vstacked)

hstacked=np.hstack((a,b))
print(hstacked)