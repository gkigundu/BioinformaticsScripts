#! python3
#!/usr/bin/env python3
#fasta2tab.py
#By: Gabriel Kigundu
#gabrielkigundu@gmail.com
#Kennesaw State University
#September 27, 2016

docstring= """
#fasta2tab.py
#By: Gabriel Kigundu
#gabrielkigundu@gmail.com
#Kennesaw State University
#September 27, 2016
DESCRIPTION
Converts FASTA to tab delimited
This script converts fasta file to a a 2 column (text based) tab delimited file.

USAGE:
python fasta2tab.py -i <fasta-file> -o <tab-file>
output is optional
input required as file or stdin
"""

import sys
import argparse
from argparse import RawDescriptionHelpFormatter
import os

infile=''

parser = argparse.ArgumentParser(description=docstring, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-o', '-out', '--output', help='Output file name', required=False)

#check stdin and set input
if not sys.stdin.isatty():
    inFile = sys.stdin
    parser.add_argument('-i','-in','--input', help='Input file name',required=False)
else:
    parser.add_argument('-i','-in','--input', help='Input file name',required=True)
    inFile = parser.parse_args().input
    if not os.path.exists(inFile):
        sys.exit("Input file not found: " + inFile)
args = parser.parse_args()

output = []
with open(inFile, 'r') as infile:
    line = infile.readline()
    while(True):
        fastaSeq = ""
        if line.startswith('>'):
            fastaSeq += line.strip()[1:] + '\t'
            line=infile.readline()
            while( True):
                if line.startswith('>') or not line:
                    break
                else:
                    fastaSeq += line.strip()
                line=infile.readline()
            fastaSeq += '\n'
            output.append(fastaSeq)
        if not line:
            break

if args.output is not None:
    with open(args.output, 'w') as outFile:
        for line in output:
            outFile.write(line)
    sys.exit("fasta2tab.py complete" )
else:
    for line in output:
        print(line)
