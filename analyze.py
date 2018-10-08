import string
import pandas as pd

''' Functions to analyze data from a dataframe structured as the 
    Dataset "movies_metadata.csv" from kaggle.com
'''

def rated_adult(df):
    '''
    Count the number of occurances where adult is set to True in the dataframe, df
    :param df: dataframe
    :return: returns the number of occurances
    '''

    result = df['adult'].value_counts()['True']

    return result


def genre(df, gen):
    '''
    Generate a dataframe where 'gen' occurs in the 'genres' row of the dataframe, df
    :param df: dataframe
    :param gen: genre
    :return: new dataframe
    '''
    result = df[df['genres'].str.contains(gen, na=False)]

    return result


def country(df, country):
    '''
    Generate a dataframe from dataframe, df, where the 'original_language' row contains the country code, country
    :param df: dataframe
    :param country: country/country code
    :return: new dataframe
    '''

    result = df[df['original_language'].str.contains(country, na=False)]

    return result


def budget(df):
    '''
    sort a dataframe, df, by the row 'budget' and return it
    :param df: dataframe
    :return: new dataframe
    '''

    result = df.sort_values(by=['budget'])

    return result


def popular(df, coun=None):
    '''
    If a country is specified, generate a dataframe, result, where the 'original_language' row contains
    the country code, country.
    Sort the dataframe by the row 'vote_average' and return it
    :param df: dataframe
    :param coun: country/country code
    :return: new dataframe
    '''

    result = df
    if country:
        result = country(result, coun)

    result = result.sort_values(by=['vote_average'])

    return result


def revenue(df, gen=None, coun=None):
    '''
    If a country is specified, generate a dataframe, result, where the 'original_language' row contains
    the country code, country.
    If a genre is specified,  generate a dataframe, result, where 'gen' occurs in the 'genres' row of the dataframe, df
    Sort the dataframe by the row 'revenue' and return it
    :param df: dataframe
    :param gen: genre
    :param coun: country/country code
    :return: new dataframe
    '''

    result = df
    if country:
        result = country(result, coun)

    if gen:
        result = genre(result, gen)

    result = result.sort_values(by=['revenue'])

    return result

def rem_punct(str):
    punct = string.punctuation
    no_punct = ''
    for char in str: #for each character in the string, check if its not a punctioation. If so - add it to the return string
       if char not in punct:
           no_punct += char

    return(no_punct)

def buzzword_count(df, top):
    buzzwords = {}
    for overview in df['overview']:
        overview_stripped = str(overview).lower()
        overview_stripped = rem_punct(overview_stripped)
        words = overview_stripped.split()
        for word in words:
            buzzwords.setdefault(word, 0)
            buzzwords[word] += 1

    buzzwords_100 = list(reversed(sorted(buzzwords, key=buzzwords.__getitem__)))

    return buzzwords_100[0:top]