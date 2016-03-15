from plot import Plot
from image import Image
from imports import *

def processPlot(img):

    plot = Plot(img)
    plot.findCorners()

    if plot.plotCheck() == False:
        print "Not a Plot!"
        return False

    plot.getColorQuant()
    # plot.show_corners()


    plot.findTicks()
    plot.show_ticks()

    plot.findTickText()
    plot.findyTickText()

    # plot.show_ticktexts()

    plot.parseScaleValues()

    plot.getAllSeries()

    clr = 151
    while clr != -1:
        clr = int(raw_input())
        img = plot.extractPlotLine(clr)
        img2 = Image("img/series_green.jpg") 
        img2.gray = img
        points = plot.findSeriesPoints(img2)
        helpers.plotPoints(plot.img.img, points)
        plot.img.reload()

    # import pdb; pdb.set_trace()

    # plot.findSeriesPoints()
    #
    # plot.recognizeText()
    # plot.praseScaleValues()
    # plot.praseCaptions()
    #
    # plot.rescaleSeries()
    #
    # return plot.table

import sys

try:
    fname = sys.argv[1]
except:
    fname = "freqPlotResults/testCase1.png"
img = Image(fname)
processPlot(img)
