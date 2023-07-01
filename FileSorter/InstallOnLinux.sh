#!/bin/bash

if [ ! -d ~/.local/bin ] 
then       
	mkdir ~/.local/bin
fi

if [ ! -d ~/.local/src ] 
then       
	mkdir ~/.local/src
fi

if [ -d ~/.local/src/FileSorter ]
then
	echo "source directory really exist, can't procced"
	exit
else
	mkdir ~/.local/src/FileSorter
	cp main.py ~/.local/src/FileSorter/
	ln -s ~/.local/src/FileSorter/main.py ~/.local/bin/FileSorter
	chmod +x ~/.local/src/FileSorter/main.py 
	chmod +x ~/.local/bin/FileSorter
fi



