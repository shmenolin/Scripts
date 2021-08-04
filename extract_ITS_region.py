#make a dictionary of sequence naame and fastaa sequence
#get start and end position from gff file
#extract the region
import sys
import os
from Bio import SeqIO
import re
import pandas as pd
import textwrap

def main():
    description="Extract ITS sequences from a fasta file, using information in gff file."\
        " Internal Transcribed Region is region between 16S and 23S ribosomal RNA sequences.\nOutput will be stored as ITS_sequences.fasta\nUsage:\t"\
            "python extract_ITS_region.py <fasta_filename> <gff_filename>"
    if sys.argv[1] == "-help" or sys.argv[1]=='--h':
        print(description)
        exit()

    fasta_file = sys.argv[1]
    gff_file=sys.argv[2]
    #its_seq_file = sys.argv[2]
    fasta_dict = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))

    #make a file for 16S and 23S start stop
    cmd="grep -E '\trRNA\t' {} | grep -E '16S ribosomal RNA|23S ribosomal RNA' > rRNAs.gff".format(gff_file)
    os.system(cmd)
    rRNAs=pd.read_csv('rRNAs.gff', sep = '\t', names= ['seq_id', 'source', 'type', 'start', 'stop','a', 'b', 'c', 'description'])
    os.system('rm ITS_sequences.fasta')
    out_handle = open('ITS_sequences.fasta', 'w+')
    _16S_start=_23S_start = 0
    my_wrap = textwrap.TextWrapper(width = 80)
    for index, row in rRNAs.iterrows():
        descrip = row['description']
        seq_id = row['seq_id']
        if re.search(r'16S ribosomal',descrip):
            _16S_start = row['start'] -1
            _16S_stop=row['stop'] -1
            seq_id = row['seq_id']
        elif re.search(r'23S ribosomal',descrip):
            _23S_start = row['start'] -1
            _23S_stop = row['stop'] -1
        if _16S_start and _23S_start:
            if _23S_start > _16S_start:
                start = _16S_stop-1
                stop = _23S_start-1
            elif _23S_start < _16S_start:
                start = _23S_stop-1
                stop = _16S_start-1

            text_1 = str(fasta_dict[seq_id].seq[start:stop])
            its_sequence = my_wrap.fill(text = text_1)
            out_handle.write(">%s_its_sequence\n%s\n" % (seq_id,its_sequence))
            _16S_start=_23S_start = 0
    out_handle.close()

if __name__ == "__main__":
    main()
    
