#!/usr/bin/python
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


for line in infile:
    line= line.strip().split('\t')
    if len(line) < 2:
        print line
        #sys.exit("input has less than 2 columns")
    print line
    if len(line)>1:
        count = 1
        header= '>' + line[0]
        while count < len(line)-1:
            header += ' ' + line[count]
            count +=1
        print header
        if writefile:
            outfile.write(header+'\n')
        else:
            print(header)
        seq = len(line)-1
        while len(line[seq]) > 120:
            if writefile:
                outfile.write(line[seq][:119]+'\n')
                line[seq]= line[seq][120:]
            else:
                print(line[seq][:119])
                line[seq]= line[seq][120:]
        if len(line[seq]) != 0:
            if writefile:
                outfile.write(line[seq]+'\n')
            else:
                print line[seq]
            line[seq] = ''

if readfile:
    print ("Input file: %s" % args.input )
    infile.close()
if writefile:
    print ("Output file: %s" % args.output )
    outfile.close()
sys.exit("tab2fasta.py complete" )
