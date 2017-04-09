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
    acq = pd.read_html('https://en.wikipedia.org/wiki/List_of_mergers_and_acquisitions_by_Alphabet', header=0, parse_dates=False)

    acquisitions = acq[0]

    return acquisitions
  
if __name__ == '__main__':
    app.run(host='0.0.0.0')
