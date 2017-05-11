#!/usr/bin/python
#seqret_phylip_corrector.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#December 16, 2016

docstring= """
#seqret_phylip_corrector.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#December 16, 2016

DESCRIPTION

input phylip interleaved file that was created by emboss seqret
adds a space between the header and sequence

"""

import sys
import argparse
from argparse import RawDescriptionHelpFormatter
from random import randint

infile=''
outfile=''


parser = argparse.ArgumentParser(description=docstring, formatter_class=RawDescriptionHelpFormatter)
#parser.add_argument('-o', '-out', '--output', help='Output file name', required=False)
parser.add_argument('-i','-in','--input', help='Input file name',required=True)
infile = open(parser.parse_args().input, 'r')
args = parser.parse_args()

in_lines = []
out_lines = []
for line in infile:
    in_lines.append(line)
infile.close()

for line in in_lines:
    if len(line) > 0:
        if line[0].isdigit():
            line= line[:10] + ' ' + line[10:]
    out_lines.append(line)

outfile = open(parser.parse_args().input, 'w')
for line in out_lines:
    outfile.write(line)

print ("Converted file: %s" % args.input )
infile.close()
outfile.close()
sys.exit("seqret_phylip_corrector.py complete" )
