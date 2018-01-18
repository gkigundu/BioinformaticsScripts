import os
import sys
from Bio import SeqIO

#/home/gkigundu/vsd/gabe/2-HMMER_Search_of_NR_Database/hmmer_squeezed_nogaps_rmredund90/vsd_hmmer/results_w_Palovcak_editing/pore/tmhmm

#filepath="/home/gkigundu/vsd/gabe/2-HMMER_Search_of_NR_Database/hmmer_squeezed_nogaps_rmredund90/vsd_hmmer/results_w_Palovcak_editing/pore/tmhmm/all_tmhmm_output.txt"
def tmhmm_output_parser(filepath, fasta_file, max_helices):
    file = open(filepath, 'r')

    acc = []
    hel = []
    ind = []
    count = 0
    for line in file:
        if line.startswith('#'):
            line = line.strip().split()
            if line[2] == 'Number':
                count+=1
                if int(line[6]) < max_helices:
                    acc.append(line[1].strip().split('|')[0])
                    hel.append(line[6].strip())
                    ind.append(count)
                    
                    
    file.close()
    header = []
    fullseq = []
    selHeader = []
    selSeq = []
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        seqid = str(seq_record.id).split('|')
        header.append(seqid[0])
        fullseq.append(str(seq_record.seq).upper())
    print(len(ind))
    #for index in ind:
    #    selHeader.append(header[index])
    #    selSeq.append(seq[index])
    for accession in acc:
        try:
            index = header.index(accession)
            selHeader.append(header[index])
            del header[index]
            selSeq.append(fullseq[index])
            del fullseq[index]
        except ValueError as e:
            print(accession)
            sys.exit('Did not find accession in file. Please use file with appropriate accessions')
    print(len(selHeader))
    print(len(selSeq))
    folderpath, filename = os.path.split(filepath)
    filename=filename.split('.')
    outputFile=''
    if len(filename) > 1:
        for i in range(0, len(filename)-1): outputFile += filename[i]
        outputFile += '_accessions.' + filename[-1]
    else: outputFile += filename[0] + '_accessions'
    outputfilepath = os.path.join(folderpath, outputFile)
    with open(outputfilepath, 'w') as output:
        output.write('accession\t# of Helices\tsequence index\n')
        for i, j, k in zip(acc, hel, ind): output.write(i + '\t' + j + '\t' + str(k)+ '\n')
    fastafolderpath, fastafilename = os.path.split(fasta_file)
    outputFasta = 'tmhmm_' + str(max_helices) + '_' + fastafilename
    outputfilepath = os.path.join(folderpath, outputFasta)
    print ('here')
    with open(outputfilepath, 'w') as output:
        for i, j in zip(selHeader, selSeq):
            output.write('>' +i + '\n')
            sequence = j
            while len(sequence) > 100:
                output.write(sequence[:100] + "\n")
                sequence=sequence[100:]
            if len(sequence) > 0:
                output.write(sequence + "\n")
    
userParameters = sys.argv[1:]

try:
    if len(userParameters) == 3:
        userParameters[0] = userParameters[0].rstrip(os.sep)
        userParameters[1] = userParameters[1].rstrip(os.sep)
        tmhmm_output_parser(userParameters[0], userParameters[1], int(userParameters[2]))
    else:
        print("There is a problem!")
        print(len(userParameters))
except Exception as e:
    print("There is a problem!")
    print(e)












