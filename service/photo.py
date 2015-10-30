__author__ = 'Canon'

from PIL import Image
from StringIO import StringIO

def crop_save_img(filename, data, x1, y1, x2, y2):
    imgIO = StringIO(data)
    img = Image.open(imgIO)
    croped_img = img.crop((x1, y1, x2, y2))
    dot_pos = filename.rfind('.')
    absfilename = filename[:dot_pos]
    croped_img.save(absfilename+'.jpg', 'JPEG')
