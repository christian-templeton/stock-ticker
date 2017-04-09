#!/usr/bin/env python
from flask import Flask, render_template, request, redirect
# import libraries
import datetime
import pandas as pd
from pandas import DataFrame
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np





app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():

   # a data frame
    df1 = pd.DataFrame({
    'number': [1, 2, 3],
    'animal': ['cat', 'dog', 'mouse']
    })
df1
  
if __name__ == '__main__':
    app.run(host='0.0.0.0')
