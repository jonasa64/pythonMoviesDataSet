# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:26:27 2018

@author: Jonas
"""

import numpy as np
import matplotlib.pyplot as plt


def ploting_releasedate_number(dataframe_date):
    
    dataframe_date.value_counts().sort_index().plot()




def ploting_runtime_releasedate(dataframex , dataframey):
    
    
    
    x = np.array([dataframex])
    y = np.array([dataframey])
    
    
    
    
    print(x.dtype)
    print(y.dtype)
    
    plt.ylabel("relasedate")
    plt.xlabel("runtime")
    
    plt.scatter(x,y)