from plot import Plot
import sys
from image import Image
from imports import *
from findrects import getrectangles
from corners import findAllRects
from corner_detection import corner_detection

from getbounds import getbounds
# from getout import getOutput
from print2 import Output
from pdftoimg import pdf2img


def processPlot(plot):

    if plot.plotCheck() == False:
        print "Not a Plot!"
        return False

    plot.show_corners()
    # plot.getColorQuant()

    plot.findLegendCorners()
    try:
        plot.findTicks()
        plot.show_ticks()
        plot.getBounds()
        plot.findTickText()
        plot.findyTickText()
        plot.getAxisCaption()
        # plot.show_ticktexts()
        plot.parseScaleValues()
    except:
        pass

    plot.getColorQuant()
    
    plot.getAllSeries()

    plot.mapLegendToPlots()

    try:
        out = plot.generate_output()
    except Exception,e:
        print e

    Output([ ("tmp/page-1.jpg", [out])])
    return out

    # print out
    #



def processPage(img):

    print "Finding all possible rectangles in the page"
    rects = findAllRects(img)

    plotOuts = []
    for rect in rects:
        plot = Plot(img)
        plot.corners = rect
        try:
            pout = processPlot(plot)
        except:
            pass

        if pout != False:
            plotOuts.append(pout)

    return plotOuts

try:
    fname = sys.argv[1]
except:
    print "Please input the pdf file"
    import os
    os.exit()

img = Image(fname)
pageout = processPage(img)
