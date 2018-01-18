#!/usr/bin/env python3
#name_switcher.py
#By: Gabriel Kigundu
#gabrielkigundu@gmail.com
#Kennesaw State University
#September 27, 2016

docstring= """
#name_switch.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#September 27, 2016
DESCRIPTION
switch accession with provided accession or given provided a tab delimited file with accession, name as first 2 columns

USAGE:
python name_switch.py -i <input-file> -a <accession-file> -o <output-file>
output is optional
input required as file or stdin
accession-file is required
"""

import sys
import argparse
from argparse import RawDescriptionHelpFormatter
import os

inFile=''

parser = argparse.ArgumentParser(description=docstring, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-o', '-out', '--output', help='Output file name', required=False)
parser.add_argument('-a', '-acc', '--accession', help='Accession file name', required=True)
#set input file to stdin else get input file name
if not sys.stdin.isatty():
    inFile = sys.stdin
else:
    parser.add_argument('-i','-in','--input', help='Input file name',required=True)
    inFile = parser.parse_args().input
    if not os.path.exists(inFile):
	    sys.exit("Input file does not exist!!")
    
args = parser.parse_args()


   
#add accessions to dictionary
if not os.path.exists(args.accession):
		sys.exit("Input file does not exist!!")
nameSet ={}
with open(args.accession, 'r') as nameFile:
	for line in nameFile:
		line=line.strip().split("\t")
		if len(line) > 1:
			if len(line[0]) > 0:
				if line[1] in nameSet:
					sys.exit("Accessions listed multiple times in accession file")
				else:
					nameSet[line[0]] = line[1]

#read input file line by line and replace all occurrences of accessions in file
switched=[]
with open(inFile, 'r') as infile:
	for line in infile:
		if len(line)>0:
			for accession in nameSet:
				index = line.find(accession)
				if index !=-1:
					line = line[:index] + nameSet[accession] + line[index+len(accession):]
			switched.append(line)
#write to file or print to screen
if args.output is not None:
	with open(args.output, 'w') as outFile:
		for line in switched:
			outFile.write(line)
	sys.exit("name_switch.py complete" )
else:
    for line in switched:
        print (line.strip())
