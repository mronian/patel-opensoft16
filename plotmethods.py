import corners
import seriesExtractor
import tickmethods
import colorExtractor
import findxyticks

methods = {

        "cornerFinder": corners.findCorners_1,

        "seriesPointsFinder": seriesExtractor.extractSeriesPoints,

        "ticksFinder": findxyticks.findticks,

        "colorFinder": colorExtractor.getColors

}


