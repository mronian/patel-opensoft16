from plot import Plot
import sys
from image import Image
from imports import *
from findrects import getrectangles
from corners import findAllRects
from corner_detection import corner_detection

from getbounds import getbounds
from getout import getOutput
from pdftoimg import pdf2img


def processPlot(plot):

    if plot.plotCheck() == False:
        print "Not a Plot!"
        return False

    # plot.show_corners()
    # plot.getColorQuant()
    # plot.findLegendCorners()

    try:
        plot.findTicks()
        # plot.show_ticks()
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

    out = plot.generate_output()

    return out

    # print out
    #
    # getOutput([[out]])



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

imgs = pdf2img(fname)

out = []
for fimg in imgs:
    print "Processing File", fimg
    if "jpg" not in fimg and "jpeg" not in fimg:
        continue

    img = Image("tmp/"+fimg)
    try:
        pageout = processPage(img)
        out.append(pageout)
    except:
        pass

print "Writing Output to a pdf file"

getOutput(out)

print "Done! Check output.pdf"



