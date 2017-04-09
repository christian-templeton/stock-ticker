#!/usr/bin/env python
from flask import Flask, render_template, request, redirect
import sys

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    name = input('Hi, I\'m Rye and I\'m a serviceDoodle. What\'s your name?')
    print 'Nice to meet you', name + '!!!!!'


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    app.run(host='0.0.0.0')
