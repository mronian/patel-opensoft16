from plot import Plot
from image import Image
from imports import *
from findrects import getrectangles


def processPlot(plot):

    if plot.plotCheck() == False:
        print "Not a Plot!"
        return False

    plot.getColorQuant()
    # plot.show_corners()

    try:
        plot.findTicks()
        plot.show_ticks()

        plot.findTickText()
        plot.findyTickText()

    # plot.show_ticktexts()

        plot.parseScaleValues()
    except:
        pass

    plot.getAllSeries()



def processPage(img):

    print "Finding all possible rectangles in the page"
    rects = getrectangles(img)

    for rect in rects:
        plot = Plot(img)
        plot.corners = rect
        processPlot(plot)

import sys

try:
    fname = sys.argv[1]
except:
    fname = "freqPlotResults/testCase1.png"

img = Image(fname)
# plot = Plot(img)
# plot.findCorners()
# processPlot(plot)
processPage(img)
