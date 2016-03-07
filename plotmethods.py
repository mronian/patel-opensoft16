import corners
import seriesExtractor
import tickmethods
import colorExtractor
import findxyticks
import colourMasking

methods = {

        "cornerFinder": corners.findCorners_1,

        "seriesPointsFinder": seriesExtractor.extractSeriesPoints,

        "ticksFinder": findxyticks.findticks,

        "colorFinder": colorExtractor.getColors,

        "maskColor": colourMasking.colourMasking,

        "xtickstextFinder": tickmethods.getTicksText

}


