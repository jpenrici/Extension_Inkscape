# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
'''
	Objetivo alterar textos previamente conhecidos em um arquivo SVG.
'''	
import re
import os.path


# Variáveis
pathFile = "original.svg"  # Caminho do arquivo

# Lendo Arquivo
if os.path.exists(pathFile):
    print (pathFile + " exists ...")
    inputFile = open(pathFile, "r+")
    text = inputFile.read()
    inputFile.close()
else:
    print ("file not found.")
    print ("check file path.")
    print (pathFile)

# Substituindo textos pre-definidos dentro do arquivo original
listWords = ["num1", "num2", "num3", "num4", "num5", "num6", "num7", "other"]
for s in listWords:
    rex = re.compile(s)
    print ("Number of occurrences in original text: " + s)
    print (rex.findall(text))
    temp = rex.sub(s.upper(), text)	# maiúscula
    text = temp

# Gravando Arquivo
outputFile = open("result.svg", "w")
outputFile.write(temp)
outputFile.close()