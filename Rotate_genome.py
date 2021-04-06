import sys
import argparse
import re

def change_start(start_pos, contig_file1):

    new_file=open("reset_start"+re.search(r'[A-Za-z0-9]*', contig_file1).group()+'.fa', 'w+')
    contig_file=open(contig_file1, 'r')
    string=''
    for line in contig_file.readlines():
        if re.search('>', line):
            name=line
        else:
            string+=line.strip()

    string2=string[start_pos-1:] + string[0:start_pos-1]
    genome_length = len(string2)
    new_file.write(name)
    for i in range(0,genome_length,70):  ##write only 70 characters per line
        new_file.write(string2[i:i+70]+"\r\n")

    new_file.close()
    contig_file.close()

def main():
    parser = argparse.ArgumentParser(description='This is a program to set the DNA start position at desired point')
    parser.add_argument("dnaA_position", help="start position of dnaA gene in the genome sequence", type=int)
    parser.add_argument("genome_file_name", help="fasta file contianing the genome sequence. File should have single genome sequence"\
        , type=str)
    args = parser.parse_args()
    start_pos=args.dnaA_position
    contig_file1=args.genome_file_name
    change_start(start_pos, contig_file1)



if __name__=='__main__':
    main()
