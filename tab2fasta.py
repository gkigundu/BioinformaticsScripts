#! python3
#!/usr/bin/env python3
#tab2fasta.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#September 27, 2016

docstring= """
#tab2fasta.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#September 27, 2016
DESCRIPTION
Converts tab delimited to FASTA
This script converts a 2 column (text based) tab delimited file to a fasta file.
The first column is assumed to be the header and second column is the sequence.
Max fasta sequence length will be 120 characters per line.

USAGE:
python tab2fasta.py -i <tab-file> -o <fasta-file>
output is optional
input required as file or stdin
"""

import sys
import argparse
from argparse import RawDescriptionHelpFormatter
import os

inFile=''

parser = argparse.ArgumentParser(description=docstring, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-o', '-out', '--output', help='Output file name', required=False)

## show values ##
if not sys.stdin.isatty():
    inFile = sys.stdin
    parser.add_argument('-i','-in','--input', help='Input file name',required=False)
else:
    parser.add_argument('-i','-in','--input', help='Input file name',required=True)
    inFile = parser.parse_args().input
    if not os.path.exists(inFile):
        sys.exit('Input file not found')
    
args = parser.parse_args()

#read file, check for 2 columns, append data to list
output=[]
with open(inFile, 'r') as infile:
    for line in infile:
        line= line.strip().split('\t')
        if len(line) == 1:
            print (line)
            sys.exit("input file has less than 2 columns")
        if len(line)>1:
            line[0]= '>' + line[0]
            output.append(line[0])
            seq = ''
            count = 100
            while len(line[1]) > count:
                output.append(line[1][count-100:count])
                count += 100
            count-=100
            if len(line[1]) > count:
                output.append(line[1][count:])
#print to screen or write to file
if args.output is not None:
    with open(args.output, 'w') as outFile:
        for line in output:
            outFile.write(line + '\n')  
    sys.exit("tab2fasta.py complete" )
else:
    for line in output:
        print(line)
