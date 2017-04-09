#!/usr/bin/env python
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    name = input('What\'s your name?')
    exclaim = '!'
    multiply = exclaim * 3
    return 'Hello there ' + name + multiply
  
if __name__ == '__main__':
    app.run(host='0.0.0.0')
