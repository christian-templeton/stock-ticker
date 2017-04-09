#!/usr/bin/env python
from flask import Flask, render_template, request, redirect
# import libraries
import datetime
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
import quandl

# import api key
quandl.ApiConfig.api_key = 'veCdQMWydzdrbYxvUqkr'



app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
# Retrieve data from quandl
tableau = quandl.get('WIKI/DATA')

# Create dataframe with most recent stock info
df = pd.DataFrame(tableau).tail(365)




df["dateform"] = [(str(df.index.month[i]) + '/' + str(df.index.date[i])[8:10] + '/' + str(df.index.date[i])[2:4]) for i in range(len(df['Adj. Close']))]


# Create a new data series date with the date in the preferred format using the strftime method
df["Date"] = [df.index.strftime('%-m' + '/' + '%d' + '/' + '%y') for i in range(len(df['Adj. Close']))]

# Create a new data series with the percentage that takes the change in Adj. Close price in the preferred format using the pct_change and round methods
df["Percentage"] =  (df['Adj. Close'].pct_change(periods=1, fill_method='pad', limit=None, freq=None)*100).round(decimals=1)








# Create a tuple that returns the date and percentage for the first 100 days of 2016

list(df.iterrows())[:5]


# Create a new data series percentage that takes the change in Adj. Close price in the preferred format
df["percentage"] = [float("{0:.1f}".format((df['Adj. Close'][i]/df['Adj. Close'][i-1]-1)*100)) for i in range(len(df['Adj. Close']))]

df["perc"] = [df['Adj. Close'].shift(periods=1, freq=None, axis=0)*100 for i in range(len(df['Adj. Close']))]


df["percentage"] = [float("{0:.1f}".format((df['Adj. Close'][i]/df['Adj. Close'][i-1]-1)*100)) for i in range(len(df['Adj. Close']))]


# Create a tuple that returns the date and percentage for the first 100 days of 2016
list(df.itertuples(index=False, name=None))[-100:][12:15]



    return df["perc"] = df['Adj. Close'].shift(periods=2, freq=None, axis=1)





  
if __name__ == '__main__':
    app.run(host='0.0.0.0')
