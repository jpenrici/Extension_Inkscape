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

const string TAB1 {char(32),char(32),char(32),char(32)};
const string TAB2 = TAB1 + char(32) + char(32);
const string TAB3 = TAB2 + char(32) + char(32);
const string TAB4 = TAB3 + char(32) + char(32);

const int VBX = 600;
const int VBY = 100;
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
	"<svg width=\"" + to_string(VBX) + "px\" height=\"" + to_string(VBY)
	 + "px\" viewBox=\"0 0 " + to_string(VBX) + " " + to_string(VBY) + "\"",
	TAB1 + "xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">",
	TAB1 + "<title>Example</title>",
};

const vector<string> footer {"</svg>"};

vector<string> create_background(const int NUM){
	return {
		TAB1 + "<g",
		TAB2 + "inkscape:label=\"background_" + to_string(NUM) + "\"",
		TAB2 + "inkscape:groupmode=\"layer\"",
		TAB2 + "id=\"layer_bg" + to_string(NUM) + "\">",
		TAB2 + "<rect",
		TAB3 + "x=\"0\" y=\"0\"",
		TAB3 + "width=\"" + to_string(VBX) + "\" height=\"" + to_string(VBY) + "\"",
		TAB3 + "rx=\"0\" ry=\"0\"",
		TAB3 + "style=\"fill:" + COLOR_BG + ";fill-opacity:1.0\"",
		TAB3 + "/>",
		TAB1 + "</g>"
	};
}

vector<string> create_layer(const string text)
{
	vector<string> layers;
	for(int i = 0; i < text.size(); ++i) {
		string str = text.substr(0, i + 1);
		layers.push_back(TAB1 + "<g");
		layers.push_back(TAB2 + "inkscape:label=\"layer_" + to_string(i) + "\"");
		layers.push_back(TAB2 + "inkscape:groupmode=\"layer\"");
		layers.push_back(TAB2 + "id=\"layer_" + to_string(i) + "\">");
		// background
		layers.push_back(TAB2 + "<rect");
		layers.push_back(TAB3 + "x=\"0\" y=\"0\"");
		layers.push_back(TAB3 + "width=\"" + to_string(VBX) + "\" height=\"" + to_string(VBY) + "\"");
		layers.push_back(TAB3 + "rx=\"0\" ry=\"0\"");
		layers.push_back(TAB3 + "style=\"fill:" + COLOR_BG + ";fill-opacity:1.0\"");
		layers.push_back(TAB3 + "/>");
		// text
		layers.push_back(TAB2 + "<text");
		layers.push_back(TAB3 + "x=\"10\"");
		layers.push_back(TAB3 + "y=\"50\"");
		layers.push_back(TAB3 + "style=\"fill:" + COLOR_TXT
			+ ";font-family:Arial;font-size:36px;letter-spacing:2\">");
		layers.push_back(TAB4 + str + "_");
		layers.push_back(TAB2 + "</text>");
		layers.push_back(TAB1 + "</g>");
	}

	return layers;
}

void save(vector<string> out)
{
	ofstream svgOut("svgOut_layer.svg");

	for (string str_out: out) {
		cout << str_out << '\n';
		svgOut << str_out << '\n';
	}

	svgOut.close();
}

void construct(const string text)
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

	save(out);
}

int main()
{
	construct("Example of layer construction.");
	return 0;
}