'''
Srihari R
To convert pdf to images using the following CLI command
python pdftojpg.py <filename>
Images are saved as imag0.jpg, imag1.jpg and so on.
'''

import sys
from wand.image import Image

filename=sys.argv[1]

for i in range(0, 100):
    try:
        name=filename+'['+str(i)+']'
        print 'Converting Page no: '+str(i+1)
        img=Image(filename=name,resolution=500)
        print 'Saving image'
        name='imag'+str(i)
        img.save(filename=name+'.jpg')
    except:
        break
    
