from flask import Flask, render_template, request, redirect




app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
  
    listed = [i for i in range(10)]
    return str(listed)

    



if __name__ == '__main__':
    app.run(host='0.0.0.0')
