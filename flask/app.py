from flask import Flask, render_template
import json
from fakemydata.generate_data import generate_data as gd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/fakemydata')
def fakemydata():
    #Request the following information from the user:
    #xlow - lowest x, often 0
    #xhigh - highest x
    #xintervalstyle - only takes 2 values, "regular" and "random"
    #numberofdatapoints
    #noiselevel - a value between 0 and 1, as determined by user on a sliding scale
    #idealcurvecode - python code for y
    json = gd(xlow, xhigh, xintervalstyle, numberofdatapoints, noiselevel, idealcurvecode)
    #json is a list of lists (each sublist has one x and one y in it)
    return json, render_template('fakemydata.html')

@app.route('/inputview')
def inputview():
    return render_template('inputview.html')

@app.route('/sentenceview')
def sentenceview():
    return render_template('sentenceview.html')

@app.route('/plagiarise', methods = ['POST'])
def plagiarise():
    essay = request.data
    shuffledessay = plagiarise_with_translation

    #convert esssay to json file

    return json

if __name__ == '__main__':
    app.run(debug=True)