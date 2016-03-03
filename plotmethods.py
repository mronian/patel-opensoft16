import corners
import seriesExtractor
import tickmethods
import colorExtractor

methods = {

        "cornerFinder": corners.findCorners_1,

        "seriesPointsFinder": seriesExtractor.extractSeriesPoints,

        "xticksFinder": tickmethods.getTicks,

        "colorFinder": colorExtractor.getColors

}


