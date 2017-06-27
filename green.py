#!/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import os
import getopt
import numpy as np
from PIL import Image
from scipy import misc

default_r_value = (0, 0)
default_c_level = 30
default_g_level = 20


def usage():
    print(
        """
        Usage: python green.py source_pic [option]
        -h or --help: show this usage
        -r or --resize: resize the picture. Default: %s not resize. Format:(h, w) 
        -c or --compress: compress picture. Default: %d. Format:(0, 100]
        -g or --green: make picture more green times. Default: %d. Format: [0, oo)
        -s or --save: location save the work. Default: Script path and named green+filename. Format: Full path.
        """ % (default_r_value, default_c_level, default_g_level)
    )


def work_func(img_path, resize_value, compress_level, green_level, save_path):
    green_number = 0.4
    srv_img = Image.open(img_path)
    resize_value=tuple(eval(resize_value))
    if min(resize_value) != 0:
        srv_img = srv_img.resize((resize_value))
    srv_img.save(save_path, quality=compress_level)
    d_img = Image.open(save_path)
    d_img_array = np.array(d_img)
    rows, cols, channels = d_img_array.shape

    for i in range(green_level):
        for row in range(rows):
            for col in range(cols):

                r = d_img_array.item(row, col, 0)
                g = d_img_array.item(row, col, 1)
                b = d_img_array.item(row, col, 2)

                y = 0.299*r + 0.587*g + 0.114*b
                u = -0.147*r - 0.289*g + 0.436*b - green_number
                v = 0.615*r - 0.515*g - 0.100*b - green_number

                r = y + 1.14*v
                g = y - 0.39*u - 0.58*v
                b = y + 2.03*u

                d_img_array.itemset((row, col, 0), r)
                d_img_array.itemset((row, col, 1), g)
                d_img_array.itemset((row, col, 2), b)

    misc.imsave(save_path, d_img_array)


def main(argv):
    if os.path.exists(sys.argv[1]):
        srv_path = sys.argv[1]
    else:
        print("MUST GIVE A EXIST FILE!")
        sys.exit(1)

    try:
        opts, args = getopt.getopt(sys.argv[2:], "hr:c:g:s:", ["help", "resize=", "compress=", "green=", "save="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    r_value = default_r_value
    c_level = default_c_level
    g_level = default_g_level
    d_path = './green-' + os.path.basename(srv_path)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-r", "--resize"):
            r_value = arg
        elif opt in ("-c", "--compress"):
            c_level = arg
        elif opt in ("-g", "--green"):
            g_level = arg
        elif opt in ("-s", "--save"):
            d_path = arg

    work_func(srv_path, r_value, c_level, g_level, d_path)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
        sys.exit()
    main(sys.argv[1:])
