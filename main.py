import os, filehandler, analyze, plotting
import pandas as pd
from random import choice, randint

# Define filename and url for the dataset
fname = "movies.csv"
url = "https://raw.githubusercontent.com/MikkelHansen95/dataset/master/movies_metadata.csv"

# Download required files/datasets
if not os.path.isfile(fname):
    filehandler.download(url,fname)

# Read the dataset and remove untitled entries
dataframe = pd.read_csv(fname, dtype='unicode', low_memory=False)
dataframe = dataframe[dataframe['title'].notnull()]


# Using 'analyze' retrieve portions of the needed data
adult = analyze.rated_adult(dataframe)
animation = analyze.genre(dataframe,'Animation')['title']
budget = analyze.budget(dataframe)['title']

#ploting the numbers of movies from a releasedate
plot1 = plotting.releasedate_number(dataframe)
plot1 = plot1.get_figure()

#ploting the runtime as x and date as y
plot2 = plotting.runtime_releasedate(dataframe)
plot2 = plot2.get_figure()

#plotting Revenue, Budget and Buzzword Count as X, Y, X in 3D plot
plot3 = plotting.three_d_plot(dataframe)
plot3 = plot3.get_figure()

# Select a random title from the budget dataframe, and reveal it's rank
randbudget = randint(0, len(budget) - 1)
rank = randbudget
budgetpart = "highest"
if randbudget > (len(budget) / 2):
    budgetpart = "lowest"
    rank = len(budget) - randbudget

if __name__ == '__main__':

    print('''
    
\tThese results are based on the {0} file downloaded from:
    
\t    {1}
        
\tThe file is loaded into a dataframe, which is then stripped of all rows, 
\twhere the title column has a value corresponding to null
    
\t#####################################################
\t#                                                   #
\t#                Questions and results              #
\t#                                                   #
\t#####################################################
        
    '''.format(fname, url))

# Print the results

    print("\t * How many movies are rated adult?")
    print("\n\t\t", adult,"movies are rated as adult.\n\n")

    print("\t * How many movies are listed as animation?")
    print("\n\t\t", len(animation), "movies are listed as animation.", "E.g.", '"' + animation.iloc[randint(0, len(animation) - 1)] + '"', "\n\n")

    print("\t * Which movie had the highest budget?")
    print('\n\t\t"' + budget.iloc[-1] + '"', "has had the highest budget,\n\t\t where as", '"' + budget.iloc[randbudget - 1] + '"', "had the", str(rank) + ".", budgetpart, "budget\n\n")

    print("\t * Which danish movie is most popular?")
    print('\n\t\t"' + analyze.popular(dataframe,'da')['title'].iloc[-1] + '"', "is the most popular danish movie!\n\n")

    print("\t * Which english action movie had the biggest revenue?")
    print('\n\t\t"' + analyze.revenue(dataframe,'Action','en')['title'].iloc[-1] + '"', "has had the biggest revenue so far\n\n")

    #plot1.savefig('plot1.png')
    #plot2.savefig('plot2.png')
    #plot2.savefig('plot2.png')