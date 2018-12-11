# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
# Extensão para o Inkscape randomizar as cores RGB, o preenchimento e/ou
# contorno de objetos selecionados.

import random
import inkex
import simplestyle


class RandomRGB(inkex.Effect):

    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option("",   "--randomizeRed",
            action="store",
            type="inkbool",
            dest="randomizeRed",
            default=True,
            help="")
        self.OptionParser.add_option("",   "--randomizeGreen",
            action="store",
            type="inkbool",
            dest="randomizeGreen",
            default=True,
            help="")
        self.OptionParser.add_option("",   "--randomizeBlue",
            action="store",
            type="inkbool",
            dest="randomizeBlue",
            default=True,
            help="")
        self.OptionParser.add_option("",   "--randomizeFill",
            action="store",
            type="inkbool",
            dest="randomizeFill",
            default=True,
            help="")
        self.OptionParser.add_option("",   "--randomizeStroke",
            action="store",
            type="inkbool",
            dest="randomizeStroke",
            default=False,
            help="")
        self.OptionParser.add_option("",   "--keepColors",
            action="store",
            type="inkbool",
            dest="keepColors",
            default=False,
            help="")                               
                  
    def effect(self):
        for id, node in self.selected.iteritems():
            try:
                style = simplestyle.parseStyle(node.get('style'))
            except:
                inkex.errormsg(_("No style attribute found for id: %s") % id)
                continue

            if (self.options.randomizeFill == False and
                self.options.randomizeStroke == False):
                break

            if (self.options.keepColors):
                fill_red = style['fill'][1:3]
                fill_green = style['fill'][3:5]
                fill_blue = style['fill'][5:7]
                stroke_red = style['stroke'][1:3]
                stroke_green = style['stroke'][3:5]
                stroke_blue = style['stroke'][5:7]
            else:
                fill_red = "00"
                fill_green = "00"
                fill_blue = "00"
                stroke_red = "00"
                stroke_green = "00"
                stroke_blue = "00"

            if (self.options.randomizeFill):
                if (self.options.randomizeRed):
                    fill_red = "%02x" % random.randint(0, 0xFF)
                if (self.options.randomizeGreen):
                    fill_green = "%02x" % random.randint(0, 0xFF)
                if (self.options.randomizeBlue):
                    fill_blue = "%02x" % random.randint(0, 0xFF)
                fill = "#%s%s%s" % (fill_red, fill_green, fill_blue)
                style['fill'] = fill
                node.set('style', simplestyle.formatStyle(style))
            
            if (self.options.randomizeStroke):
                if (self.options.randomizeRed):
                    stroke_red = "%02x" % random.randint(0, 0xFF)
                if (self.options.randomizeGreen):
                    stroke_green = "%02x" % random.randint(0, 0xFF)
                if (self.options.randomizeBlue):
                    stroke_blue = "%02x" % random.randint(0, 0xFF)
                stroke = "#%s%s%s)" % (stroke_red, stroke_green, stroke_blue)
                style['stroke'] = stroke
                node.set('style', simplestyle.formatStyle(style))              

if __name__ == '__main__':
    e = RandomRGB()
    e.affect()
