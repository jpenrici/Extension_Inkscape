# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-
'''
    Objective:

        Insert images (photos) in SVG files.

    Details:

        Files in the Images directory.
        Txt list with the names of the files.

    Requires:

        Python Imaging Library (PIL)

'''

import os
import sys
from PIL import Image

EOL = '\n'
EMPTY = ""
TARGET = "#IMAGEBASE#"

PATH, _ = os.path.split(os.path.realpath(__file__))
TEMPLATE = "template_landscape_21x15cm.txt"
IMG_PATH = PATH + "/Images/"
SVG_PATH = PATH + "/Output/"


def load(path):
    lines = []
    print("Loaded: {}".format(path))
    try:
        f = open(path)
        lines = [line for line in f]
        f.close()
    except Exception:
        print("error: couldn't open file.")
        pass

    return lines


def save(path, text):
    print("Saved: {}".format(path))
    try:
        f = open(path, "w")
        f.write(text)
        f.close()
    except Exception:
        print("error: cannot save " + path)
        exit(0)


def convert(data):
    text = ""
    for item in data:
        text += item 

    return text


def prepare(data):
    svg = convert(load(TEMPLATE))

    if not os.path.exists(SVG_PATH):
        print("Create " + SVG_PATH)
        os.makedirs(SVG_PATH)

    for filename in data:
        filename = filename.replace(EOL, EMPTY)
        if filename == EMPTY:
            continue
        if filename[0] == '#':
            continue

        path = IMG_PATH + filename
        try:
            img = Image.open(path)
            img_width, img_height = img.size

            info = "Prepare {}\nImage {} x {}".format(filename, img_width,
                img_height)

            if img_width < img_height:
                info += "\tRotate ..."
                imgr = img.transpose(Image.ROTATE_90)
                filename = "rotate_" + filename
                path = IMG_PATH + filename
                imgr.save(path)
            print(info)

            out = svg.replace(TARGET, path)
            filename = filename.split('.')[0]
            save(SVG_PATH + filename + ".svg", out)
                   
        except:
            print("There is something wrong.")
            continue


if __name__ == '__main__':

    # Test
    data = load("./list_images.txt")
    prepare(data)
