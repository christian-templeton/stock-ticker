#!/usr/bin/env python
from flask import Flask, render_template, request, redirect
import sys

name = input('What\'s your name?')
exclaim = '!'
multiply = exclaim * 3

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    if name == 'Christian':
        print 'Hello there ' + name + multiply
    else:
        print 'Hello there ' + name


if __name__ == '__main__':
    app.run(host='0.0.0.0')
