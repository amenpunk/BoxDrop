#!/bin/bash

INPUT=./data.csv
OLDIFS=$IFS
IFS=','
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read name url
do
    wget $url
done < $INPUT
IFS=$OLDIFS
