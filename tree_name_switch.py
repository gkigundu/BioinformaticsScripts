#!/usr/bin/python
#fasta_header_switch.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#September 27, 2016

docstring= """
#fasta_header_switch.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#September 27, 2016

DESCRIPTION

switch header with provided accession or organism provided a tab delimited file with accesion, organism and header

"""
"""
USAGE:
python fasta_header_switch.py -i <fasta-file> -a <accession-file> -o <outfile>

output is optional
input required as file or stdin
"""

import sys
import argparse
from argparse import RawDescriptionHelpFormatter

infile=''
outfile=''
afile=''
readfile=False
writefile = False

parser = argparse.ArgumentParser(description=docstring, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-o', '-out', '--output', help='Output file name', required=False)
parser.add_argument('-a', '-acc', '--accession', help='Accession file name', required=True)
#parser.add_argument('-c', '-chc', '--choice', help='Switch choice', required=True)
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
#choice = args.choice


out_lines = []
temp_line = ''
infile = open(parser.parse_args().input, 'r')
for line in infile:
    out_lines.append(line)
infile.close()


afile=open(args.accession, 'r')
for line2 in afile:
    line2=line2.strip()
    if line2== '':
        continue
    line2 = line2.split('\t')
    if len(line2) < 2:
        print line2
        print len(line2)
        sys.exit('Incorrect format for accession file. requires Accession, organims and header')
    infile = open(args.output, 'r')
    found = False
    j=0
    for line in out_lines:
	if len(line)>0:
            temp = line2[0]
            if line.find(temp)!=-1:
                i = line.find(temp)
                end = i+10
                found = True
                temp2 = line[:i]
                temp3 = line[end:]
                temp_line = temp2 + line2[1] + temp3
                out_lines[j]=temp_line
        j +=1
    if not found:
        print "Not Found"
        print line2

afile.close()




if writefile:
    for line in out_lines:
	outfile.write(line)
else:
    for line in out_lines:
        print line.strip()

if readfile:
    print ("Input file: %s" % args.input )
    infile.close()
if writefile:
    print ("Output file: %s" % args.output )
    outfile.close()
sys.exit("fasta_header_switch.py complete" )
