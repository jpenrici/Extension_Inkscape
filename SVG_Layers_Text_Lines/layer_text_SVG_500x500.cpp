/* Exemplo de construção automática de camadas em SVG
 * Objetivo construir um subtexto em cada camada.
 * Depois usar o svgOut_layer.svg para gerar svgOut_layer.xcf com Inkscape
 * e svgOut_layer.gif com GIMP
*/
#include <iostream>
using std::cin;
using std::cout;
using std::string;
using std::to_string;

#include <fstream>
using std::ofstream;

#include <vector>
using std::vector;

const string SPC {char(32), char(32)};
const string SPC1 = SPC + SPC;
const string SPC2 = SPC1 + SPC;
const string SPC3 = SPC2 + SPC;
const string SPC4 = SPC3 + SPC;
const string SPC5 = SPC4 + SPC;

const int VBX = 500;
const int VBY = 500;
const string FONT_SIZE = "36";
const string COLOR_BG = "#000000";
const string COLOR_TXT = "#00FF00";

const vector<string> arquiteture {
	"#header#",
	"#background#",
	"#layers#",
	"#footer#"
};

const vector<string> header {
	"<?xml version=\"1.0\" standalone=\"no\"?>",
	"<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"",
	"\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">",
	"<svg width=\"" + to_string(VBX) + "px\" height=\"" + to_string(VBY) +
	"px\" viewBox=\"0 0 " + to_string(VBX) + " " + to_string(VBY) + "\"",
	SPC1 + "xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">",
	SPC1 + "<title>Example</title>",
};

const vector<string> footer {"</svg>"};

vector<string> create_background(const int NUM)
{
	return {
		SPC1 + "<g",
		SPC2 + "inkscape:label=\"background_" + to_string(NUM) + "\"",
		SPC2 + "inkscape:groupmode=\"layer\"",
		SPC2 + "id=\"layer_bg" + to_string(NUM) + "\">",
		SPC2 + "<rect",
		SPC3 + "x=\"0\" y=\"0\"",
		SPC3 + "width=\"" + to_string(VBX) + "\" height=\"" + to_string(VBY) + "\"",
		SPC3 + "rx=\"0\" ry=\"0\"",
		SPC3 + "style=\"fill:" + COLOR_BG + ";fill-opacity:1.0\" />",
		SPC1 + "</g>"
	};
}

vector<string> create_layer(const string text)
{
	int x = 10, y = 10, i = 0;
	vector<string> layers;
	for(int i = 0; i < text.size(); ++i) {
		int pos = i + 1;
		string str = text.substr(0, pos);
		string style_text = "style=\"font-style:normal;font-variant:normal;"
			"font-weight:normal;font-stretch:normal;font-size:"
			+ FONT_SIZE +"px;line-height:125"
			"%;font-family:monospace;-inkscape-font-specification:monospace;"
			"font-variant-ligatures:normal;font-variant-caps:normal;"
			"font-variant-numeric:normal;font-feature-settings:normal;"
			"text-align:start;letter-spacing:0px;word-spacing:0px;"
			"writing-mode:lr-tb;text-anchor:start;fill:"
			+ COLOR_TXT + ";"
			"fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;"
			"stroke-linejoin:miter;stroke-opacity:1\"";
		// layer
		layers.push_back(SPC1 + "<g");
		layers.push_back(SPC2 + "inkscape:label=\"layer_" + to_string(pos) + "\"");
		layers.push_back(SPC2 + "inkscape:groupmode=\"layer\"");
		layers.push_back(SPC2 + "id=\"layer_" + to_string(pos) + "\">");
		// background
		layers.push_back(SPC2 + "<rect");
		layers.push_back(SPC3 + "x=\"0\" y=\"0\"");
		layers.push_back(SPC3 + "width=\"" + to_string(VBX) + "\" height=\"" + to_string(VBY) + "\"");
		layers.push_back(SPC3 + "rx=\"0\" ry=\"0\"");
		layers.push_back(SPC3 + "style=\"fill:" + COLOR_BG + ";fill-opacity:1.0\"");
		layers.push_back(SPC3 + "id=\"rect4_" + to_string(pos)+ "\" />");
		// Text
		layers.push_back(SPC2 + "<flowRoot");
		layers.push_back(SPC3 + "xml:space=\"preserve\"");
		layers.push_back(SPC3 + "id=\"flowRoot_" + to_string(pos) + "\"");
		layers.push_back(SPC3 + style_text + "><flowRegion");
		layers.push_back(SPC5 + "id=\"flowRegion_" + to_string(pos) + "\"");
		layers.push_back(SPC5 + "style=\"fill:" + COLOR_TXT + "\">");
		layers.push_back(SPC4 + "<rect");
		layers.push_back(SPC5 + "id=\"rect_" + to_string(pos) + "\"");
		layers.push_back(SPC5 + "x=\"" + to_string(x) + "\" y=\"" + to_string(y) + "\"");		
		layers.push_back(SPC5 + "width=\"" + to_string(VBX - x) + "\" height=\"" + to_string(VBY - y) + "\"");	
		layers.push_back(SPC5 + "style=\"fill:" + COLOR_TXT + "\"/>");
		layers.push_back(SPC4 + "</flowRegion><flowPara");
		layers.push_back(SPC5 + "id=\"flowPara_" + to_string(pos) + "\">" + str + "_");
		layers.push_back(SPC4 + "</flowPara></flowRoot>");
		layers.push_back(SPC1 + "</g>");
	}
	return layers;
}

void save(vector<string> out, string filename)
{
	ofstream svgOut(filename + ".svg");
	for (string str_out: out) {
		cout << str_out << '\n';
		svgOut << str_out << '\n';
	}
	svgOut.close();
}

void construct(const string text, const string filename)
{
	vector<string> in, out, layers;
	layers = create_layer(text);
	for(string str: arquiteture) {
		in.clear();
		if (str == "#header#") in = header;
		if (str == "#background#") in = create_background(0);
		if (str == "#layers#") in = layers;
		if (str == "#footer#") in = footer;
		for (string str_in: in) {
			out.push_back(str_in);
		}
	}
	save(out, filename);
}

int main()
{
	// test
	string text =
		"01..#.#.#.#.#.#.#.#.#."
		"02..#.#.#.#.#.#.#.#.#."
		"03..#.#.#.#.#.#.#.#.#."
		"04..#.#.#.#.#.#.#.#.#."
		"05..#.#.#.#.#.#.#.#.#."
		"06..#.#.#.#.#.#.#.#.#."
		"07..#.#.#.#.#.#.#.#.#."
		"08..#.#.#.#.#.#.#.#.#."
		"09..#.#.#.#.#.#.#.#.#."
		"10..#.#.#.#.#.#.#.#!"		// last minor line 
	;

	construct(text, "svgOut_layer_500x500");

	return 0;
}