from flask import Flask, render_template, request, redirect




app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
  

   

    list1 = range(120)
    list2 = range(518)

    comp1 = [i for i in range(len(list2))]

    return comp1



if __name__ == '__main__':
    app.run(host='0.0.0.0')
