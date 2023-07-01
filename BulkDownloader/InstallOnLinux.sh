#!/bin/bash

if [ ! -d ~/.local/bin ] 
then       
	mkdir ~/.local/bin
fi

if [ ! -d ~/.local/src ] 
then       
	mkdir ~/.local/src
fi

if [ -d ~/.local/src/BulkDownloader ]
then
	echo "source directory really exist, can't procced"
	exit
else
	mkdir ~/.local/src/BulkDownloader
	cp main.py ~/.local/src/BulkDownloader/main.py
	ln -s ~/.local/src/BulkDownloader/main.py ~/.local/bin/BulkDownloader
	chmod +x ~/.local/src/BulkDownloader/main.py 
	chmod +x ~/.local/bin/BulkDownloader
fi



