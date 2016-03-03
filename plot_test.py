import unittest
from plot import *
from image import *
import cv2

class TestPlot(unittest.TestCase):

    def setUp(self):
        img = Image("img/tstplot.jpg")
        self.plot = Plot(img)

    def test_finding_corners(self):
        """
        Setup: 
            - Input Test Image (Already done)
        
        Assertion:
            - Compare the area of contour with the actual area
        
        Things to Find:
            - Area of Bounding Rectangle
            
        """
        self.plot.findCorners()
        print "\n\nCorners:\n\n", self.plot.corners
        assert cv2.contourArea(self.plot.corners) > 321000

    def test_xtick_coordinates(self):
        """
        Setup: 
            - Input Test Image (Already done)
            - Corners
        
        Assertion:
            - Check if the calculated 1st tick point is approximately correct
        
        Things to Find:
            - Corner Points
            - Actual Coordinates of the 1st tick point
            
        """

    def test_xtick_text(self):
        """
        Setup: 
            - Input Test Image (Already done)
            - Corners
            - 1st Tick Point Coordinates
        
        Assertion:
            - Check the OCR on bounding rect and match it with actual text
        
        Things to Find:
            - Corner Points
            - Actual Coordinates of the 1st tick point
            - Actual text content corresponding to 1st tick
            
        """
    def test_finding_seriespoints(self):
        """
        
        """

        self.plot.corners = [

            [[145,  87]],

            [[145, 536]],

            [[860, 536]],

            [[860,  87]],
        ]
        self.plot.findSeriesPoints()
        print self.plot.seriesPoints

