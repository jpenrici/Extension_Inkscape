# -*- Mode: Python; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

import sys
import inkex
import simplestyle
from math import *
from simpletransform import computePointInNode


def coordinate(angle, radius):
    x = cos(radians(angle)) * radius
    y = sin(radians(angle)) * radius
    return (x, y)


def create_figure((x, y), size, num_curves):
    interior = size * 0.10  # 10% do tamanho
    arc = 360 // num_curves  # ângulo entre Mxy e XY
    inclination = arc // (num_curves * 2)  # abertura do ângulo para C1 e C2

    angle_M = 0
    M = coordinate(angle_M, interior)
    figure = "M " + str(M[0] + x) + "," + str(M[1] + y)

    for curves in xrange(0, num_curves):
        angle_C1 = angle_M + inclination
        angle_C2 = angle_C1 + arc - (2 * inclination)
        angle_XY = angle_M + arc
        C1 = coordinate(angle_C1, size)
        C2 = coordinate(angle_C2, size)
        XY = coordinate(angle_XY, interior)
        figure += " C " + str(C1[0] + x) + "," + str(C1[1] + y) + \
                  " " + str(C2[0] + x) + "," + str(C2[1] + y) + \
                  " " + str(XY[0] + x) + "," + str(XY[1] + y)
        angle_M += arc
    figure += " z"

    return figure


def draw(offset, size, num_curves, parent):

    sw = '0.5px'
    name = 'figure-flower'
    style = {'stroke': '#000000', 'stroke-width': sw, 'fill': 'none'}

    figure = create_figure(offset, size, num_curves)
    figure_attribs = {'style': simplestyle.formatStyle(style),
                      inkex.addNS('label', 'inkscape'): name, 'd': figure}
    inkex.etree.SubElement(parent, inkex.addNS('path', 'svg'), figure_attribs)


class Figure(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option("-s", "--size",
                                     action="store", type="int",
                                     dest="size")
        self.OptionParser.add_option("-n", "--num_curves",
                                     action="store", type="int",
                                     dest="num_curves")

    def effect(self):
        obj = self.current_layer
        offset = computePointInNode(list(self.view_center), obj)
        draw(offset, self.options.size, self.options.num_curves, obj)


if __name__ == '__main__':
    e = Figure()
    e.affect()
