import sys
import argparse
from PIL import Image
import math
import os

def create_collage(src,dst):
    new_im = Image.new('RGB', (900,450))

    for image_name in os.listdir(src):
        img=src+image_name
        img=Image.open(img)

        width, height = img.size

        for j in range(0,900,width):
            for x in range(0,math.ceil(450/height)):
                new_im.paste(img, (j,x * height))
        new_im.save(dst+'/'+image_name)

if __name__ == '__main__':

    ap=argparse.ArgumentParser()

    ap.add_argument('-s','--source', type=str, default='true',
    help="path to source folder")
    ap.add_argument('-d','--destination', type=str, default='true',
    help="path to destination folder")
    args=vars(ap.parse_args())

    src = args["source"]
    dst = args["destination"]
    
    os.mkdir(dst)

    create_collage(src,dst)
