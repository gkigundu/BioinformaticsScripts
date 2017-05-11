#!/usr/bin/python
#alignment_editor.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#September 27, 2016

docstring= """
#alignment_editor.py
#By: Gabriel Kigundu
#gabrielKigundu@gmail.com
#Kennesaw State University
#February 24, 2017

DESCRIPTION

Given a left and right column boundary and a side (l or r), this program moves residues to the specified side while moving gaps to the opposite side within the specified boundaries.
example:

alignment_editor.py -i input_file -o output_file -lb 5 -rb 10 -s l

input_file   AMND-DTS--EDSFW

output file  AMNDDTS---EDSFW


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
parser.add_argument('-lb', '-LB', '--left_boundary', help='Left Boundary', required=True)
parser.add_argument('-rb', '-RB', '--right_boundary', help='Right Boundary', required=True)
parser.add_argument('-s', '-side', '--side_to_move', help='Side to move residues', required=True)

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

lb=args.left_boundary
rb=args.right_boundary
s=args.side_to_move
s=s.lower()
try:
    lb = int(lb)
    rb = int(rb)
except ValueError:
    sys.exit("Please enter numbers only for the boundary parameters")
if lb >= rb:
    sys.exit("Left boundary must be less than right boundary")
if s.isalpha():
    if s == 'left' or s == 'l':
        s='l'
    elif s == 'right' or s == 'r':
        s='r'
    else:
        sys.exit("Please enter 'r', 'l', 'left', or 'right'")
else:
    sys.exit("Please enter letters only for the side to move parameter")


out_lines = []
out_lines2 = []
temp_line = ''
temp_line2 = ''

for line in infile:
        if line.startswith('>'):
            if len(temp_line2) > 0:
                out_lines2.append(temp_line2)
                temp_line2 = ''
            temp_line = line.strip()
            out_lines.append(temp_line)
        else:
            temp_line2 += line.strip()
if len(temp_line2) >0:
    out_lines2.append(temp_line2)

max_length= 0
for line in out_lines2:
    if len(line) > max_length:
        max_length = len(line)
    for line2 in out_lines2:
        if len(line) > len(line2):
            sys.exit("sequences must be of equal length")
print 'Number of sequences: ', len(out_lines)
print 'Sequence length: ', max_length+1
rb -=1
lb -=1
if rb > max_length:
    sys.exit("Right boundary must be less than sequence length")
print 'Left Boundary: ', lb
print 'Right Boundary: ', rb
count = 1
index = 0
out_lines3 = []
for line in out_lines2:
    print 'sequence ', count
    count +=1
    if s =='r':
        index = rb
        indexLB = lb
        while index >= indexLB:
            if line[index] == '-':
                if index == max_length:
                    line = line[:lb] + '-' + line[lb:index]
                else:
                    line = line[:lb] + '-' + line[lb:index] + line[index+1:]
                indexLB +=1
            else:
                index -=1
    if s=='l':
        index = lb
        indexRB = rb
        while index <= indexRB:
            #print 'index ', index, ' ', line[index]
            #print 'line length: ', len(line)
            if line[index] == '-':
                #print line
                if rb == max_length:
                    line = line[:index] + line[index+1:rb+1] + '-' 
                else:
                    line = line[:index] + line[index+1:rb+1] + '-' + line[rb+1:] 
                #print line
                indexRB -=1
            else:
                index +=1
         
    out_lines3.append(line)

index=0
if writefile:
    for line in out_lines:
	outfile.write(line+ '\n')
	line2 = out_lines3[index]
	while len(line2) > 120:
            outfile.write(line2[:120]+ '\n')
            line2 = line2[120:]
        if len(line2) > 0:
            outfile.write(line2+ '\n')
            line2=''
        index +=1
else:
    for line in out_lines:
        print line, '\n'
        line2 = out_lines3[index]
	while len(line2) > 120:
            print (line2[:120]), '\n'
            line2 = line2[120:]
        if len(line2) > 0:
            print line2, '\n'
            line2=''
        index +=1

if readfile:
    print ("Input file: %s" % args.input )
    infile.close()
if writefile:
    print ("Output file: %s" % args.output )
    outfile.close()
sys.exit("alignment_editor.py complete" )

