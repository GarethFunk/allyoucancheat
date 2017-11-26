from flask import Flask, render_template, request
import json
from plagiarise_with_translation import plagiarise_with_translation
from fakemydata.generate_data import generate_data

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
    #data_json, imagepath = generate_data(xlow, xhigh, xintervalstyle, numberofdatapoints, noiselevel, idealcurvecode)
    #json is a list of lists (each sublist has one x and one y in it)
    return data_json, render_template('fakemydata.html')

@app.route('/sentenceview')
def sentenceview():
    return render_template('sentenceview.html')

@app.route('/plagiarise', methods=['POST'])
def plagiarise():

    essay = request.form["essay"]
    shuffledessay = plagiarise_with_translation(essay)

    #convert essay to json file
    essay_json = json.dumps(shuffledessay)

    return essay_json

if __name__ == '__main__':
    app.run(debug=True)