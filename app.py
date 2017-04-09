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
# Retrieve data from quandl
tableau = quandl.get('WIKI/DATA')
df = pd.DataFrame(tableau).tail(365)



app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():


    return df

  
if __name__ == '__main__':
    app.run(host='0.0.0.0')
