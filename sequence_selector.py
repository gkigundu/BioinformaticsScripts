#! /usr/bin/env python3
import sys
import argparse
from argparse import RawDescriptionHelpFormatter
import os
from Bio import SeqIO
docstring="""
This program takes a multiple fasta file and a list of accessions and returns sequences matching those accessions in multiple fasta file.

The accession list should only contain accessions and nothing else.


"""
parser = argparse.ArgumentParser(description=docstring, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-a', '-acc', '--accessions', help='list of accessions', required=True)
parser.add_argument('-o', '-out', '--output', help='Output file name', required=True)
if not sys.stdin.isatty():
    infile = sys.stdin
    parser.add_argument('-i','-in','--input', help='Input file name',required=False)
else:
    parser.add_argument('-i','-in','--input', help='Input file name',required=True)
    readfile = True
    infile = parser.parse_args().input

args = parser.parse_args()
acc = args.accessions
output = args.output

def sequence_selector(fasta_file, accessions, output):
    #read accessions
    acc = []
    with open(accessions, 'r') as f:
        for line in f:
            acc.append(line.upper().strip())
    # Create our hash table to add the sequences
    sequences={}
    # Using the Biopython fasta parse we can read our fasta input
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        seq_record.id = seq_record.id.upper()
        if '|' in seq_record.id:
            seq_record.id = seq_record.id.split('|')
        else:
            seq_record.id = [seq_record.id]
        found = False
        for ID in seq_record.id:
            if ID in acc:
                sequence = str(seq_record.seq).upper()
                sequences[sequence] = ID
    # Write the clean sequences
    # Create a file in the same directory where you ran this script
    #strip slash or backslash of path
    folder_path, fasta_file = os.path.split(fasta_file)
    #if input file is input.fa, output file will be input_clean.fa
    file_name_split = fasta_file.split('.')
    fasta_file = ""
    extension =""
    if len(file_name_split) == 1:
        fasta_file = file_name_split[0]
    else:
        extension = '.' + file_name_split[-1]
        for i in range(0,len(file_name_split)-1):
            fasta_file += file_name_split[i] + '.'
        fasta_file = fasta_file[:-1]
    if output:
        #fasta_file =  fasta_file + "_" + str(len(sequences)) + extension
        output_fasta_file = output
        with open(output_fasta_file, "w") as output_file:
            # Just read the hash table and write on the file as a fasta format
            for sequence in sequences:
                output_file.write(">" + sequences[sequence] + "\n")
                while len(sequence) > 100:
                    output_file.write(sequence[:100] + "\n")
                    sequence=sequence[100:]
                if len(sequence) > 0:
                    output_file.write(sequence + "\n")
        print("Output file: " + output_fasta_file)
    else:
        for sequence in sequences:
            print(">" + sequences[sequence])
            while len(sequence) > 100:
                print(sequence[:100] + "\n")
                sequence=sequence[100:]
            if len(sequence) > 0:
                print(sequence + "\n")

try:
    sequence_selector(infile,acc,output)
except Exception as e:
    print("There is a problem!")
    print(e)
    sys.exit()
sys.exit("sequence_selector.py complete\nRun sequence_cleaner.py to remove possible duplicates" )
