#!/usr/bin/python
#fasta2tab.py
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

Converts FASTA to tab delimited

This script converts fasta file to a a 2 column (text based) tab delimited file.

"""
"""
USAGE:
python tab2fasta.py -i <tab-file> -o <outfile>

output is optional
input required as file or stdin
"""

import sys
import argparse
from argparse import RawDescriptionHelpFormatter

infile=''
outfile=''
readfile=False
writefile = False

parser = argparse.ArgumentParser(description=docstring, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-o', '-out', '--output', help='Output file name', required=False)

## show values ##
if not sys.stdin.isatty():
    infile = sys.stdin
    parser.add_argument('-i','-in','--input', help='Input file name',required=False)
else:
    parser.add_argument('-i','-in','--input', help='Input file name',required=True)
    readfile = True
    infile = open(parser.parse_args().input, 'r')
    
args = parser.parse_args()

if args.output is not None:
    writefile = True
    outfile = open(args.output, 'w')


out_lines = []
temp_line = ''

for line in infile:
        if line.startswith('>'):
            if len(out_lines) >0:
                temp_line+= '\n'
            out_lines.append(temp_line)
            temp_line = line.strip() + '\t'
        else:
            temp_line += line.strip()
if len(out_lines) >0:
    temp_line+= '\n'
    out_lines.append(temp_line)
if writefile:
    for line in out_lines:
	outfile.write(line)
else:
    f
        ##print out_lines, '\n'

if readfile:
    print ("Input file: %s" % args.input )
    infile.close()
if writefile:
    print ("Output file: %s" % args.output )
    outfile.close()
sys.exit("fasta2tab.py complete" )
