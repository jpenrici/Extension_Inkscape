# layer_text_SVG.cpp #

compile:
	g++ layer_text_SVG.cpp -o layer_text_SVG

execute:
	./layer_text_SVG


# usage #	

Inkscape:
	Open svgOut_layer.svg
	Save as svgOut_layer.xcf

GIMP:
	Open svgOut_layer.xcf
	Export as svgOut_layer.gif
		Mark "As animation"
		Mark "Loop forever"
		Mark "Use delay entered above for all frames"