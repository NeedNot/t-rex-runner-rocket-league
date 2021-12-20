from PIL import Image
import os, sys

path = os.path.dirname(os.path.abspath(__file__))
dirs = os.listdir( path )
mywidth = (276*2)



def resize_keep_aspect_ration():
    for item in dirs:
        img_path = path + "\\" + item
        if os.path.isfile(img_path):
            im = Image.open(img_path)
            f, e = os.path.splitext(img_path)
            wpercent = (mywidth / float(im.size[0]))
            hsize = int((float(im.size[1]) * float(wpercent)))

            im = im.resize((mywidth, hsize), Image.ANTIALIAS)
            im.save(f + '.png', 'PNG')

resize_keep_aspect_ration()