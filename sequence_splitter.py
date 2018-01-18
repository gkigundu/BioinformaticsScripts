#alignment splitter

import sys
import os
from Bio import SeqIO

def sequence_splitter(fasta_file, index):
    # Create our hash table to add the sequences
    sequences={}
    domain1={}
    domain2={}
    #list of ids to check for duplicates
    ids=[]
    # Using the Biopython fasta parse we can read our fasta input
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        # Take the current sequence
        sequence = str(seq_record.seq).upper()
        sequence1 = sequence[:index]
        sequence2 = sequence[index:]
        # Check if the current sequence is according to the user parameters
        sequences[sequence] = seq_record.id
        domain1[seq_record.id] = sequence1
        domain2[seq_record.id] = sequence2
    # Write the split sequences
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
    fasta_file1 =  fasta_file + "_vsd" + extension
    fasta_file2 =  fasta_file + "_pore" + extension
    output_fasta_file1 = os.path.join(folder_path, fasta_file1)
    output_fasta_file2 = os.path.join(folder_path, fasta_file2)
    with open(output_fasta_file1, "w") as output_file:
        # Just read the hash table and write on the file as a fasta format
        for seqid in domain1:
            output_file.write(">" + seqid + "\n")
            sequence = domain1[seqid]
            while len(sequence) > 100:
                output_file.write(sequence[:100] + "\n")
                sequence=sequence[100:]
            if len(sequence) > 0:
                output_file.write(sequence + "\n")
    with open(output_fasta_file2, "w") as output_file:
        # Just read the hash table and write on the file as a fasta format
        for seqid in domain2:
            output_file.write(">" + seqid + "\n")
            sequence = domain2[seqid]
            while len(sequence) > 100:
                output_file.write(sequence[:100] + "\n")
                sequence=sequence[100:]
            if len(sequence) > 0:
                output_file.write(sequence + "\n")
                
userParameters = sys.argv[1:]

try:
    if len(userParameters) == 1:
        userParameters[0] = userParameters[0].rstrip(os.sep)
        sequence_splitter(userParameters[0])
    elif len(userParameters) == 2:
        userParameters[0] = userParameters[0].rstrip(os.sep)
        sequence_splitter(userParameters[0], int(userParameters[1]))
    else:
        print("There is a problem!")
        print(len(userParameters))
except Exception as e:
    print("There is a problem!")
    print(e)
