#!/usr/bin/env python3
#embl_cds_xml_location_parser.py
#Gabriel Kigundu
#June 13, 2017

import os
import sys
import argparse
import requests
from argparse import RawDescriptionHelpFormatter
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import itertools

docstring = """

"""

parser = argparse.ArgumentParser(description=docstring, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-o', '-out', '--output', help='Output folder name', required=False)

if not sys.stdin.isatty():
    infile = sys.stdin
    parser.add_argument('-i','-in','--input', help='Input file name',required=False)
else:
    parser.add_argument('-i','-in','--input', help='Input file name',required=True)
    readfile = True
    infile = parser.parse_args().input
args = parser.parse_args()
    
##tree = ET.parse(infile)
##root = tree.getroot()
##print(root.tag, root.attrib)
##for child in root:
##    print (child.tag, child.attrib)
##for feature in root.findall('feature'):
##    print(feature)
soup=''
with open(infile) as f:
    accessions = []
    all_locations = []
    complements=[]
    joins = []
    soup = BeautifulSoup(f,'xml')
    for feature in soup.find_all('feature'):
        if feature['name'] == 'CDS':
            location = feature['location']
            if location.startswith('complement'):
                location = location[11:-1]
                complements.append('1')
            else:
                complements.append('0')
            if location.startswith('join'):
                location = location[5:-1]
                joins.append('1')
            else:
                joins.append('0')
            locations = location.split(',')
            acc = ''
            for index, location in enumerate(locations):
                location = location.split(':')
                acc = location[0]
                location = location[1]
                location = location.split('..')
                for k, num in enumerate(location):
                    if not num.isdigit():
                        print('Warning: location contains non numeric characters, '+ num)
                        num = list(num)
                        to_del = []
                        for i in range(len(num)-1, -1, -1):
                            if not num[i].isdigit():
                                to_del.append(i)
                        for i in to_del:
                            del num[i]
                        num = "".join(num)                        
                        location[k] = num
                        
                locations[index] = location
            all_locations.append(locations)
            accessions.append(acc)
outfile = 'print'
if args.output:
    if not os.path.exists(args.output):
        outfile = open(args.output, 'w')
    outfile = open(args.output, 'a')
for acc,comp, join, location in itertools.zip_longest(accessions,complements, joins, all_locations):
    strlocation =''
    for i in location:
        for j in i:
            strlocation += j + '\t'
    strlocation = strlocation[:-1]
    if args.output:
        outfile.write(acc + '\t'+comp+ '\t'+ join+ '\t'+ strlocation+ '\n')
    else:
        print(acc + '\t'+comp+ '\t'+ join+ '\t'+ strlocation )
#print(results[1])
if outfile != 'print':
    outfile.close()        
