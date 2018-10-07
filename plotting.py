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
    df = df[df['runtime'].notnull()]

    df_x = df['release_date'].tolist()
    df_y = df['runtime'].tolist()

    df_x = [x.split("-")[2] + "/" + x.split("-")[1] for x in df_x]

    plt.xlabel("Relase date")
    plt.ylabel("Runtime")

    df_x = [pd.to_datetime(d, format='%d/%M') for d in df_x]
    plt.xticks(rotation=90)

    df_y = [float(i) for i in df_y]
    plt.yticks(np.arange(0, max(df_y), step=35.0))

    return plt.scatter(df_x, df_y, 1)