import numpy as np
import json

def generate_data(xlow, xhigh, xintervalstyle, numberofdatapoints, noiselevel, idealcurvecode):

    if xintervalstyle == "regular":
        x = np.linspace(xlow, xhigh, num=numberofdatapoints)
    if xintervalstyle == "random":
        x = np.random.uniform(xlow, xhigh, size=(numberofdatapoints,))

    ywithoutnoise = eval(idealcurvecode)

    noiseSD = np.amax(ywithoutnoise)*noiselevel
    noise = np.random.normal(0, noiseSD, numberofdatapoints)

    y = ywithoutnoise + noise

    data = list(zip(x, y))
    jsonobject = json.dumps(data)

    return jsonobject

if __name__ == "__main__":
    # User defined variables
    xlow = 0
    xhigh = 5
    xintervalstyle = "random"  # user puts in either "random" or "regular"
    numberofdatapoints = 10
    noiselevel = 0.08  # user defines this with a slider
    idealcurvecode = "8*x**2 + 5*x + 6"

    print(generate_data(xlow, xhigh, xintervalstyle, numberofdatapoints, noiselevel, idealcurvecode))
