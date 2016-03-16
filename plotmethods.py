import corners
import seriesExtractor
import colorExtractor
import findxyticks
import plotxyseries
import colorquant
import plotLineExtractor
import scaleMethods
import getplots
import plotcheck

# import tickmethods_old as tickmethods
import tickmethods

import legendExtract

from ExtractTextBox import get_legend_textbox


methods = {

        "cornerFinder": corners.findCorners_1,

        "seriesPointsFinder": plotxyseries.getxyseries,

        "ticksFinder": findxyticks.findticks,

        "colorFinder": colorExtractor.getColors,

        "xtickstextFinder": tickmethods.getTicksText,

        "ytickstextFinder": tickmethods.getYTicksText,

        # "colorQuantization": colorquant.getQuantImage, 
        "colorQuantization": getplots.getPlots, 

        "plotLineExtractor": plotLineExtractor.extractPlotLine, 

        "parseScale": scaleMethods.parseScale, 

        "rescale": scaleMethods.reScale, 

        # "findLegend": get_legend_textbox, 
        "findLegend": legendExtract.extractLegend, 

        "plotCheck": plotcheck.plotCheck, 


}


