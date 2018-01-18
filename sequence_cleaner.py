import sys
import os
from Bio import SeqIO

def sequence_cleaner(fasta_file, min_length=0, por_n=100):
    # Create our hash table to add the sequences
    sequences={}
    #list of ids to check for duplicates
    ids=[]
    # Using the Biopython fasta parse we can read our fasta input
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        # Take the current sequence
        sequence = str(seq_record.seq).upper()
        # Check if the current sequence is according to the user parameters
        if (len(sequence) >= min_length and
            (float(sequence.count("N"))/float(len(sequence)))*100 <= por_n):
        # If the sequence passed in the test "is it clean?" and it isn't in the
        # hash table, the sequence and its id are going to be in the hash
            if sequence not in sequences:
                sequences[sequence] = seq_record.id
                ids.append(seq_record.id)
        # If it is already in the hash table, we're just gonna concatenate the ID
       # of the current sequence to another one that is already in the hash table
            elif seq_record.id not in ids:
                sequences[sequence] += "|" + seq_record.id
                ids.append(seq_record.id)
                


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
    fasta_file =  fasta_file + "_clean" + extension
    output_fasta_file = os.path.join(folder_path, fasta_file)
    with open(output_fasta_file, "w") as output_file:
        # Just read the hash table and write on the file as a fasta format
        for sequence in sequences:
            output_file.write(">" + sequences[sequence] + "\n")
            while len(sequence) > 100:
                output_file.write(sequence[:100] + "\n")
                sequence=sequence[100:]
            if len(sequence) > 0:
                output_file.write(sequence + "\n")

    print("CLEAN!!!\nPlease check " + output_fasta_file)


userParameters = sys.argv[1:]

try:
    if len(userParameters) == 1:
        userParameters[0] = userParameters[0].rstrip(os.sep)
        sequence_cleaner(userParameters[0])
    elif len(userParameters) == 2:
        userParameters[0] = userParameters[0].rstrip(os.sep)
        sequence_cleaner(userParameters[0], float(userParameters[1]))
    elif len(userParameters) == 3:
        userParameters[0] = userParameters[0].rstrip(os.sep)
        sequence_cleaner(userParameters[0], float(userParameters[1]),
                         float(userParameters[2]))
    else:
        print("There is a problem!")
        print(len(userParameters))
except Exception as e:
    print("There is a problem!")
    print(e)
