# -*- Mode: Python; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

import os, sys

EOL = '\n'
DELIM = ';'

def load(filename):
    data = []
    try:
        f = open(filename)
        for line in f:
            data += [line.replace(EOL, "")]
        f.close()
    except Exception:
        pass          
    return data

def save(filename, text):
    try:
        filename = open(filename, "w")
        filename.write(text)
        filename.close()
    except Exception:
        exit(0)

def convert(data):
    txt = ""
    for line in data:
        txt += line + EOL
    return txt

def prepare(svg_original, data):

    svg = svg_original

    for i in range(1, len(data)):

        # csv[0]: Name;Page;Number;Key;Text;File (Out)
        d = data[i].split(DELIM)
        if (len(d) != 6):
            continue
        
        key = d[3]
        text  = d[4]
        svg_out = d[5]

        # svg
        if (svg != svg_out):
            svg_txt = convert(load(svg_original))
            svg = svg_out
            print("File:", svg)
        
        # replace keys
        svg_txt = svg_txt.replace(key, text)
        save(svg, svg_txt)
        print(key, "==>", text)


def main():

    svg_original = "invitations.svg"
    data_csv = "list.csv"

    data = load(data_csv)
    prepare(svg_original, data)


if __name__ == '__main__':
    main()