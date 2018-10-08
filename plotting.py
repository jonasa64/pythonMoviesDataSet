# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:26:27 2018
@author: Jonas
"""

import analyze
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

def three_d_plot(df):
    buzzwords_100 = analyze.buzzword_count(df, 100)

    new_overview = []
    for overview in df['overview']:
        count = 0
        overview_stripped = str(overview).lower()
        overview_stripped = analyze.rem_punct(overview_stripped)
        words = overview_stripped.split()
        for word in words:
            if word in buzzwords_100:
                count += 1
        new_overview.append(count)

    df.overview = new_overview

    three_d = plt.figure().gca(projection='3d')
    three_d.scatter(df['revenue'], df['budget'], df['overview'])
    three_d.set_xlabel('Revenue')
    three_d.set_ylabel('Budget')
    three_d.set_zlabel('Buzzword count')

    return three_d
