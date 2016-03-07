import corners
import seriesExtractor
import tickmethods
import colorExtractor
import findxyticks
import colourMasking
import plotxyseries

methods = {

        "cornerFinder": corners.findCorners_1,

        "seriesPointsFinder": plotxyseries.getxyseries,

        "ticksFinder": findxyticks.findticks,

        "colorFinder": colorExtractor.getColors,

        "maskColor": colourMasking.colourMasking,

        "xtickstextFinder": tickmethods.getTicksText,

        "ytickstextFinder": tickmethods.getYTicksText,


}


