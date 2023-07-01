#!/bin/bash

if [ ! -d ~/.local/bin ] 
then       
	mkdir ~/.local/bin
fi

if [ ! -d ~/.local/src ] 
then       
	mkdir ~/.local/src
fi

if [ -d ~/.local/src/BMPConv ]
then
	echo "source directory really exist, can't procced"
	exit
else
	mkdir ~/.local/src/BMPConv
	cp main.py ~/.local/src/BMPConv/main.py
	ln -s ~/.local/src/BMPConv/main.py ~/.local/bin/BMPConv
	chmod +x ~/.local/src/BMPConv/main.py 
	chmod +x ~/.local/bin/BMPConv
fi



