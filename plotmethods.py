import corners
import seriesExtractor
import tickmethods
import colorExtractor
import findxyticks
# import colourMasking
import plotxyseries
import colorquant
import plotLineExtractor
import scaleMethods


methods = {

        "cornerFinder": corners.findCorners_1,

        "seriesPointsFinder": plotxyseries.getxyseries,

        "ticksFinder": findxyticks.findticks,

        "colorFinder": colorExtractor.getColors,

        # "maskColor": colourMasking.colourMasking,

        "xtickstextFinder": tickmethods.getTicksText,

        "ytickstextFinder": tickmethods.getYTicksText,

        "colorQuantization": colorquant.getQuantImage, 

        "plotLineExtractor": plotLineExtractor.extractPlotLine, 

        "parseScale": scaleMethods.parseScale, 

        "rescale": scaleMethods.reScale, 


}


