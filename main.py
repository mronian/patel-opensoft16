from plot import Plot
from image import Image
from imports import *
from findrects import getrectangles
from corners import findAllRects
from corner_detection import corner_detection

from getbounds import getbounds


def processPlot(plot):

    if plot.plotCheck() == False:
        print "Not a Plot!"
        return False

    # plot.show_corners()

    # bnds = getbounds(plot.img.img, plot.corners)

    plot.getColorQuant()
    plot.findLegendCorners()
    import pdb; pdb.set_trace()


    try:
        plot.findTicks()
        # plot.show_ticks()

        plot.findTickText()
        plot.findyTickText()
        # plot.show_ticktexts()
#
        plot.parseScaleValues()
    except:
        pass

    plot.getColorQuant()
    
    plot.getAllSeries()



def processPage(img):

    print "Finding all possible rectangles in the page"
    # rects = getrectangles(img)
    rects = findAllRects(img)
    # rects = corner_detection(img)
    # helpers.plotMulti(img.img, rects)

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
