from flask import Flask, render_template, request, redirect
import pandas as pd
from pandas import DataFrame





app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
  


    return 'Hello there '



if __name__ == '__main__':
    app.run(host='0.0.0.0')
