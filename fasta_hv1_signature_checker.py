#!/usr/bin/python
#ffasta_annotate_header.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#November 7, 2016

docstring= """
#fasta_correction.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#September 27, 2016

DESCRIPTION

Checks the sequence for a signature. This was created for dinoflagellate hv1 signature of R*WR**R
"""
"""
USAGE:
python fasta_correctiontab2fasta.py -i <tab-file> -o <outfile>

output is optional
input required as file or stdin\
"""

import sys
import argparse
from argparse import RawDescriptionHelpFormatter
from random import randint

infile=''
outfile=''
rejectedFile = ''
rejected = ''
readfile=False
writefile = False

parser = argparse.ArgumentParser(description=docstring, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-o', '-out', '--output', help='Output file name', required=False)
parser.add_argument('-c','-count','--count', help='count',required=False)
parser.add_argument('-i','-in','--input', help='Input file name',required=True)
readfile = True
infile = open(parser.parse_args().input, 'r')
    
args = parser.parse_args()  

if args.output is not None:
    writefile = True
    outfile = open(args.output, 'w')
    rejectedFile = args.output + "_Signature_missing"
    rejected = open(rejectedFile, 'w')
count=0
if args.count is not None:
    count = args.count
header = ""
sequence = ""
temp_line = ''
k=0
for line in infile:
    line = line.strip()
    if len(line) > 0:
        if line.find('>')!=-1:
            if k >0:
                i = 0
                for j in sequence:
                    if i < (len(sequence)-6):
                        if j == 'R' and sequence[i+2]=='W' and sequence[i+3] == 'R' and sequence[i+6] == 'R':
                            k = 0
                            if writefile:
                                outfile.write(header + "\n")
                                while len(sequence) > 120:
                                    outfile.write(sequence[0:120] + "\n")
                                    sequence = sequence[120:]
                                if sequence > 0:
                                    outfile.write(sequence + "\n")
                            else:
                                print header + "\n"
                                while len(sequence) > 120:
                                    print sequence[0:120]
                                    sequence = sequence[120:]
                                if len(sequence) > 0:
                                    print sequence
                            break
                    i +=1
                if k > 0:
                    k = 0
                    if writefile:
                        rejected.write(header + "\n")
                        while len(sequence) > 120:
                            rejected.write(sequence[0:120] + "\n")
                            sequence = sequence[120:]
                        if sequence > 0:
                            rejected.write(sequence + "\n")
                    else:
                        print header + "\n"
                        while len(sequence) > 120:
                            print sequence[0:120]
                            sequence = sequence[120:]
                        if len(sequence) > 0:
                            print sequence

                header = ""
                sequence = ""
            header = line
            k +=1
        else:
            sequence += line

if k >0:
    print
    i = 0
    for j in sequence:
        if i < (len(sequence)-6):
            if j == 'R' and sequence[i+2]=='W' and sequence[i+3] == 'R' and sequence[i+6] == 'R':
                k = 0
                if writefile:
                    outfile.write(header + "\n")
                    while len(sequence) > 120:
                        outfile.write(sequence[0:120] + "\n")
                        sequence = sequence[120:]
                    if sequence > 0:
                        outfile.write(sequence +"\n")
                else:
                    print header
                    while len(sequence) > 120:
                        print sequence[0:120]
                        sequence = sequence[120:]
                break
        i += 1
    if k > 0:
        k = 0
        if writefile:
            rejected.write(header + "\n")
            while len(sequence) > 120:
                rejected.write(sequence[0:120] + "\n")
                sequence = sequence[120:]
            if sequence > 0:
                rejected.write(sequence + "\n")
        else:
            print header + "\n"
            while len(sequence) > 120:
                print sequence[0:120]
                sequence = sequence[120:]
            if len(sequence) > 0:
                print sequence


if readfile:
    print ("Input file: %s" % args.input )
    infile.close()
if writefile:
    print ("Output file: %s" % args.output )
    print ("Rejected sequences in %s" % rejectedFile)
    outfile.close()
    rejected.close()
sys.exit("fasta_signature_checker.py complete" )
