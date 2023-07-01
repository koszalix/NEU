#!/bin/bash

if [ ! -d ~/.local/bin ] 
then       
	mkdir ~/.local/bin
fi

if [ ! -d ~/.local/src ] 
then       
	mkdir ~/.local/src
fi

if [ -d ~/.local/src/PDFTitleExtractor ]
then
	echo "source directory really exist, can't procced"
	exit
else
	mkdir ~/.local/src/PDFTitleExtractor
	cp main.py ~/.local/src/PDFTitleExtractor/
	ln -s ~/.local/src/PDFTitleExtractor/main.py ~/.local/bin/PDFTitleExtractor
	chmod +x ~/.local/src/PDFTitleExtractor/main.py 
	chmod +x ~/.local/bin/PDFTitleExtractor
fi



