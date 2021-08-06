#make a dictionary of sequence naame and fastaa sequence
#get start and end position from gff file
#extract the region
import sys
import subprocess
from Bio import SeqIO
import re
import pandas as pd
import textwrap

def main():
    description="Extract sequences from a fasta file for selected IDs, using information in gff file."\
        "\nUsage:\t"\
            "python extract_gene_sequences.py <fasta_filename> <gff_filename> <comma separated list of IDs>"

    try:
        if sys.argv[1] == "-help" or sys.argv[1]=='--h':
            print(description)
            exit()
        fasta_file = sys.argv[1]
        gff_file=sys.argv[2]
        id_list=sys.argv[3].split(",")
    except IndexError:
        print ("Enough arguments not provided or too many arguments")
        print (description)
        exit()
    #its_seq_file = sys.argv[2]
    fasta_dict = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))

    gffs=pd.read_csv(gff_file, sep = '\t', names= ['seq_id', 'source', 'type', 'start', 'stop','a', 'b', 'c', 'description'])
    out_handle = open('extracted_sequences.fasta', 'w+')
    my_wrap = textwrap.TextWrapper(width = 80)
    for index, row in gffs.iterrows():
        type = row['type']
        seq_id = row['seq_id']
        description = row['description']
        #print (description)
        if pd.isna(description):
            continue
        
        for variable in id_list:
            if re.search('ID='+variable ,description):
                ID= variable
                start = int(row['start'] -1)
                stop=int(row['stop'] -1)
                seq_id = row['seq_id']
                #print (start, stop)
                text_1 = str(fasta_dict[seq_id].seq[start:stop])
                sequence = my_wrap.fill(text = text_1)
                out_handle.write(">%s\n%s\n" % (ID,sequence))
                sequence=''
    out_handle.close()

if __name__ == "__main__":
    del_file=subprocess.run(["rm","extracted_sequences.fasta"], stdout=subprocess.PIPE)
    #print ('the exitcode was %d' % del_file.returncode)
    main()