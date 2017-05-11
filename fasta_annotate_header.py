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

Adds the name of the fasta file without extensions to header separated by |

Folder: Human.fasta
>Header1
ATGCGCTCCGA

to

>Header1|Human
ATGCGCTCCGA

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
count=0
if args.count is not None:
    count = args.count
out_lines = []
temp_line = ''
k =1
for line in infile:
    line = line.strip()
    j = 0;
    if line.find('>')!=-1:
        header = line.split()
        header2 =''
        m=0
        for section in header:
            header2 += header[m]+'_'
            m+=1
        accession = str(count) +'S'
        temp_zero = ''
	if len(accession) < 3:
	    accession = '0' + accession
        str_count = 10-(len(accession)+len(str(k)))
        while str_count > 0:
            temp_zero+='0'
            str_count-=1
        accession+= temp_zero + str(k)
        line = '>'+accession+' '
        line += header2[1:len(header2)-1]
        filename = args.input.split('/')
        filename = filename[len(filename)-1]
        filename = filename.split('.')
        filename = filename[0]
        #shortfilename = filename.split('_')
        #short ='_'
        #m=0
        #for section in shortfilename:
        #    short += shortfilename[m][:1]
        #line += short + str(randint(0,100)) 
        line += ' ' +filename
	k += 1
        #line = line[0] + 'lcl|' + line[1:]
    if len(line)>0:
        line +='\n'
        out_lines.append(line)
    
    #k is used for debugging
    #print k

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
sys.exit("fasta_annotate_header.py complete" )
