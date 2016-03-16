
from wand.image import Image
from wand.color import Color
from os import walk

import shutil
import os

def pdf2img(fpath, dest_width = 800):

    try:
        shutil.rmtree("tmp")
    except:
        pass
    try:
        os.mkdir("tmp")
    except:
        pass

    with Image(filename=fpath, resolution=200) as img:
         img.background_color = Color('white')
         img_width = img.width
         ratio = float(dest_width) / float(img_width)
         # img.resize(dest_width, int(ratio * img.height))
         img.compression_quality = 99
         img.format = 'jpeg'
         img.save(filename="tmp/page.jpg")

    out = []
    for (dirpath, dirnames, filenames) in walk("tmp"):
        out += filenames

    return out

import sys

try:
    fname = sys.argv[1]
except:
    fname = "freqPlotResults/testCase1.png"

# pdf2img(fname)

