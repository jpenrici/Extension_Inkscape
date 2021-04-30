# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-
'''
    Objective:

        Insert images in SVG files.

    Details:

        Files in the Images directory.
        Txt list with the names of the files.
'''

import os
import sys

EOL = '\n'
EMPTY = ""
TARGET = ["#IMAGEBASE1#", "#IMAGEBASE2#", "#IMAGEBASE3#", "#IMAGEBASE4#"]

PATH, _ = os.path.split(os.path.realpath(__file__))
TEMPLATE = "template_landscape_A4.txt"
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

    images = []
    for filename in data:
        filename = filename.replace(EOL, EMPTY)
        if filename == EMPTY:
            continue
        if filename[0] == '#':
            continue
        images += [filename]

    page = 1
    bkp = svg[::]
    if len(images) % 4 != 0:
        images += (4 - (len(images) % 4)) * ["BLANK.png"]
            
    for i in range(len(images)):
        bkp = bkp.replace(TARGET[i%4], IMG_PATH + images[i])
        print(images[i])
        if (i + 1) % 4 == 0:
            output = "page_" + str(page) + ".svg"
            save(SVG_PATH + output, bkp)
            bkp = svg[::]
            page += 1


if __name__ == '__main__':

    # Test
    data = load("./list_images.txt")
    prepare(data)
