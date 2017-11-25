import numpy as np
import matplotlib.pyplot as plt

#User defined variables
xlow = 0
xhigh = 5
xinterval = "random" #user puts in either "random" or "regular"
numberofdatapoints = 10
precision = 3 #decimal precision
noiselevel =  0.08 #user defines this with a slider
idealcurve="8*x**2 + 5*x + 6"

if xinterval == "regular":
    x = np.linspace(xlow, xhigh, num=numberofdatapoints)
if xinterval == "random":
    x = np.random.uniform(xlow, xhigh, size=(numberofdatapoints,))

ywithoutnoise = eval(idealcurve)

noiseSD = np.amax(ywithoutnoise)*noiselevel
noise = np.random.normal(0, noiseSD, numberofdatapoints)

y = ywithoutnoise + noise

plt.plot(x, y, 'o')
plt.show()