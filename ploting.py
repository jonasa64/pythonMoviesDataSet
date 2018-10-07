# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:26:27 2018
@author: Jonas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def releasedate_number(df):
    '''
    Generate a Series from the 'release_data' row in Dataframe, df, counting each
    appearance and sorting them, then plot it

    :param df: dataframe
    :return: matplotlib Plot
    '''

    df_dates = df['release_date']

    return df_dates.value_counts().sort_index().plot()


def runtime_releasedate(df):
    '''
    Generate Series based on 'runtime' and 'release_date' rows in Dataframe, df,
    making sure the release dates exist
    Generate NumPy arrays from indexed lists, then plot the two
    :param df: dataframe
    :return: matplotlib Plot
    '''

    df = df[df['release_date'].notnull()]

    df_x = df['runtime']
    df_y = df['release_date']

    data_x = range(0, len(df_x))
    data_y = range(0, len(df_y))

    x = np.array([data_x])
    y = np.array([data_y])

    plt.ylabel("Relase date")
    plt.xlabel("Runtime")

    return plt.scatter(x, y)
