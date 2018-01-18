#!/usr/bin/env python3
import os
import sys
import argparse
import requests
from argparse import RawDescriptionHelpFormatter

docstring = """
Having a list of accessions, this program downloads biocyc identifiers corresponding to those accessions.

"""
infile=''
outfile=''
db=''
org= ''
readfile=False
writefile = False

parser = argparse.ArgumentParser(description=docstring, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-o', '-out', '--output', help='Output folder name', required=False)
parser.add_argument('-d', '-db', '--database', help='Database e.g. KEGG, PUBCHEM, UNIPROT.', required=True)
parser.add_argument('-org', '--organism', help='Organism ID', required=True)
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
db = args.database.strip()
org= args.organism.strip()
#read accessions
accessions = []
for line in infile:
    line = line.strip()
    accessions.append(line)
#remove last comma
#acc = acc[:-1]
    
#create url
#https://websvc.biocyc.org/[ORGID]/foreignid?ids=[DATABASE-NAME]:[FOREIGNID]
baseurl = 'https://websvc.biocyc.org/' + org + '/foreignid?ids=' + db + ':'

count=0
for acc in accessions:
    count += 1
    url = baseurl + acc + '&fmt=json'
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
sys.exit("test_requests.py complete" )
