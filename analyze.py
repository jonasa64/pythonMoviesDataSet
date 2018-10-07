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