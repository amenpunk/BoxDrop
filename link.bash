#!/bin/bash
dir=$(zenity --file-selection --directory)
wget -O $dir/test.png "https://www.dropbox.com/s/exv8jzmar9hoz28/tortrix.png?dl=1"
