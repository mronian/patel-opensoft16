import unittest
from plot import *
from image import *
import cv2

class TestPlot(unittest.TestCase):

    def setUp(self):
        img = Image("img/tstplot.jpg")
        self.plot = Plot(img)

    def test_finding_corners(self):
        self.plot.findCorners()
        print "\n\nCorners:\n\n", self.plot.corners
        assert cv2.contourArea(self.plot.corners) > 321000

    def test_finding_seriespoints(self):

        self.plot.corners = [

            [[145,  87]],

            [[145, 536]],

            [[860, 536]],

            [[860,  87]],
        ]
        self.plot.findSeriesPoints()
        print self.plot.seriesPoints

