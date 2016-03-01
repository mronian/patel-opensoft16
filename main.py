from plot import Plot

def processPlot(img):

    plot = Plot(img)
    plot.findCorners()
    plot.findTicks()
    plot.findSeriesPoints()

    plot.recognizeText()
    plot.praseScaleValues()
    plot.praseCaptions()

    plot.rescaleSeries()

    return plot.table
