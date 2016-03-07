import unittest
from plot import *
from image import *
import cv2
import helpers as helper
import matplotlib.pyplot as plt

class TestHelpers(unittest.TestCase):

    def setUp(self):
        self.img = Image("img/tstplot.jpg")
        self.plot = Plot(self.img)
        self.corners = [

            [145,  87],

            [145, 536],

            [860, 536],

            [860,  87],
        ]

    def test_OCR(self):

        print helper.getOCRText(self.img.img, self.corners)
