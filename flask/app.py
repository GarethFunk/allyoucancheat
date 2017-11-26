from flask import Flask, render_template, request, Response
import json

from fakemydata.generate_data import generate_data
from plagiarise_with_translation import plagiarise_with_translation

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/fakemydata')
def fakemydata():
    # Request the following information from the user:
    # xlow - lowest x, often 0
    # xhigh - highest x
    # xintervalstyle - only takes 2 values, "regular" and "random"
    # numberofdatapoints
    # noiselevel - a value between 0 and 1, as determined by user on a sliding scale
    # idealcurvecode - python code for y
    # data_json = generate_data(xlow, xhigh, xintervalstyle, numberofdatapoints, noiselevel, idealcurvecode)
    # json is a list of lists (each sublist has one x and one y in it)
    return render_template('graph.html')


@app.route('/getdata', methods=['POST'])
def generatedata():
    return json.dumps(generate_data(float(request.form["x-min"]),
                         float(request.form["x-max"]),
                         request.form["x-interval-style"],
                         int(request.form["num-points"]),
                         float(request.form["noise-level"]),
                         request.form["ideal-curve"],
                         title=request.form["graph-name"]))


@app.route('/sentenceview')
def sentenceview():
    return render_template('sentenceview.html')

@app.route('/g/<graphpath>')
def getgraph(graphpath):
    in_file = open('/tmp/aycc/' + graphpath, "rb")
    data = in_file.read()
    in_file.close()
    return Response(data, mimetype='image/png')


@app.route('/plagiarise', methods=['POST'])
def plagiarise():
    essay = request.form["essay"]
    shuffledessay = plagiarise_with_translation(essay)

    # convert essay to json file
    essay_json = json.dumps(shuffledessay)

    return essay_json


if __name__ == '__main__':
    app.run(debug=True)
