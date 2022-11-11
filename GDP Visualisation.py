# importing package
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np
#Reading csv data

filepath="GDP by Metro Area 2010-2015.csv"

def read_csv(filepath):
    """ Reading File Data from CSV
    """
    gdp = pd.read_csv(filepath)
    return gdp

gdp=read_csv(filepath)      #Storing CSV data into gdp variable
y=gdp['Rank'].iloc[0:10]    #Limiting no. of Rank from 0-10
x=gdp['USdata'].iloc[0:10]  #Limiting no. of US data from 0-10 
gdp


""" Comparitive Graph Plot/LinePlot of 10 Metro Cities
"""
def linearplt(x,y):
    """it shows the line plot between US MEtro Cities and their Rank Respectively"""
    plt.plot(x, y, color='green', marker='o')
    plt.title('Overall Rank Vs US Metro City Data', fontsize=14)
    plt.xlabel('US Mtro Areas', fontsize=14)
    plt.ylabel('Overall Rank', fontsize=14)
    plt.grid(True)   #showing grid on graph plot
    plt.show()

linearplt(x,y)


""" Comparitive BarPlot of 12 Metro Cities
"""

def histplt(data):
    """histogram of a Ranking by Cities OVerall Vs 2015"""
    
    fig = plt.figure()
    width = 5
    ax = fig.add_axes([0,0,1,1])
    ax.bar(gdp['Rank'].iloc[0:12], width, color='g')
    ax.bar(gdp['2015 Rank'].iloc[0:12],gdp['2015 Rank'].iloc[0:12], width, color='g')
    plt.title('Overall Rank Vs 2015 Rank Comparison')
    #plt.set(xlabel = 'Overall Rank', ylabel='2015 Rank')

histplt(gdp)

""" ScatterPlot of 12 Metro Cities
"""

def scatter(x,fig):
    
    """it shows the scatter plot between US MEtro Cities VS OVerall Ranking"""
    plt.subplot(5,2,fig)
    plt.scatter(gdp[x].iloc[0:20],gdp['USdata'].iloc[0:20],color='r')
    plt.title(x+' vs US Metro Data')
    plt.ylabel('2015 Rank')
    plt.xlabel(x)
    

plt.figure(figsize=(10,20))

scatter('Rank', 5)