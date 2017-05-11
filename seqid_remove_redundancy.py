#!/usr/bin/python
#seqid_remove_redundancy.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#November 7, 2016

docstring= """
#seqid_remove_redundancy.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#September 27, 2016

DESCRIPTION

input list of seqids

"""

import sys
import argparse
from argparse import RawDescriptionHelpFormatter
from random import randint

infile=''
outfile=''
readfile=False
writefile = False

parser = argparse.ArgumentParser(description=docstring, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-o', '-out', '--output', help='Output file name', required=False)
parser.add_argument('-i','-in','--input', help='Input file name',required=True)
readfile = True
infile = open(parser.parse_args().input, 'r')
    
args = parser.parse_args()  

if args.output is not None:
    writefile = True
    outfile = open(args.output, 'w')

in_lines = []
temp = []
out_lines = []
temp_line = ''
for line in infile:
    in_lines.append(line.strip())
findex=0
for line in in_lines:
    index = 0
    count=0
    for line2 in in_lines:
        if line == line2:
            if count==0:
                count+=1
            else:
                print in_lines.pop(index)+'\t'+str(index)+'\t'+str(findex)
        index+=1
    findex+=1

print '---------------------------------------------------------------------------------------------------'
if writefile:
    for line in in_lines:
        outfile.write(line+'\n')
else:
    for line in in_lines:
        print line.strip()

if readfile:
    print ("Input file: %s" % args.input )
    infile.close()
if writefile:
    print ("Output file: %s" % args.output )
    outfile.close()
sys.exit("seqid_remove_redundancy.py omplete" )
