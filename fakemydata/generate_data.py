import numpy as np
import matplotlib.pyplot as plt
import uuid

def generate_data(xlow, xhigh, xintervalstyle, numberofdatapoints, noiselevel, idealcurvecode,
                  xlabel="x", ylabel="y", title="My Fake Data", grid="True", colorofpoints="", loglog="False",
                  lineofbestfit="False", colorofline="b", linewidth="0.8", orderofline="1"):

    if xintervalstyle == "regular":
        x = np.linspace(xlow, xhigh, num=numberofdatapoints)
    if xintervalstyle == "random":
        x = np.random.uniform(xlow, xhigh, size=(numberofdatapoints,))

    ywithoutnoise = eval(idealcurvecode)

    noiseSD = np.amax(ywithoutnoise)*noiselevel
    noise = np.random.normal(0, noiseSD, numberofdatapoints)

    y = ywithoutnoise + noise

    data = list(zip(x, y))

    tempdirname = '/tmp/aycc'

    if colorofpoints == "":
        settings = "o"
    else:
        settings = "".join(["o", colorofpoints])

    plt.plot(x, y, settings)

    if lineofbestfit == "True":
        plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, int(orderofline)))(np.unique(x)), color=colorofline, linewidth=linewidth)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xlim([xlow, xhigh])
    plt.grid(grid)
    plt.title(title)

    UUID = uuid.uuid1()
    file_end = ''.join([str(UUID), ".png"])
    strlist = [tempdirname, "/", file_end]
    imagepath = ''.join(strlist)
    plt.savefig(imagepath)
    plt.close()

    return data, file_end

if __name__ == "__main__":
    # User defined variables
    xlow = 0
    xhigh = 9
    xintervalstyle = "random"  # user puts in either "random" or "regular"
    numberofdatapoints = 100
    noiselevel = 0.12  # user defines this with a slider
    idealcurvecode = "8*x**2 + 5*x + 6"

    print(generate_data(xlow, xhigh, xintervalstyle, numberofdatapoints, noiselevel, idealcurvecode, lineofbestfit="True"))
