#!/usr/bin/env python3
#embl_genome_batch_retrieval.py
#Gabriel Kigundu
#May 26, 2017

docstring = """
Having a list of embl accessions, this program downloads the sequences corresponding to those accessions.
For more info, visit www.ebi.ac.uk/ena/browse/data-retrieval-rest#retrieval_multiple_identifiers
"""

#embl allows retrieval of data using the base url http://www.ebi.ac.uk/ena/data/view/
import os
import sys
import argparse
import requests
from argparse import RawDescriptionHelpFormatter

infile=''
outfile=''
readfile=False
writefile = False

parser = argparse.ArgumentParser(description=docstring, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-o', '-out', '--output', help='Output folder name', required=False)

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
    if args.output.endswith(os.sep):
        args.output = args.output[:-1]
    if not os.path.exists(args.output):
        try:
            os.makedirs(args.output)
        except Exception as e:
            print(e)
            sys.exit('could not create output folder')
    writefile = True
        

#read accessions
accessions = []
for line in infile:
    line = line.strip()
    accessions.append(line)
#remove last comma
#acc = acc[:-1]
    
#create url
baseurl = 'http://www.ebi.ac.uk/ena/data/view/display=xml&'

count = 0
for acc in accessions:
    count += 1
    url = baseurl + acc
    request = requests.get(url).text
    if writefile:
        temp_output = os.path.join(args.output, acc)
        with open(temp_output, 'w') as outfile:
            outfile.write(request)
            outfile.write('\n')
        print(count)
    else:
        print(request)

if readfile:
    print ("Input file: %s" % args.input )
    infile.close()
sys.exit("embl_genome_batch_retrieval.py complete" )
