import re
import sys
import argparse


def collect_repeats(annotation_file, repeating_entries, repeat_list):
    file1 = open(annotation_file, 'r+')
    file2 = open(repeating_entries, 'w+')
    file3 = open(repeat_list, "w+")
    file4=open("TL", "w+")

    repeated_list=[]
    Truncatedlist=[]
    repeated_info=[]
    gene_list=[]
    query_num = []
    number = 0
    hypothetical_proteins =0
    transposase_num = 0
    #read the annotation file

    full_info = file1.readlines()
    for lines in full_info:
        gene_name = re.search(r'~.*?\,', lines).group()
        gene_list.append(gene_name)
        num = re.match(r'[0-9]+?\,', lines).group()
        
        #to avoid trailing space in the number
        num = int(num[0:-1])
        query_num.append(num)
    total_genes = len(gene_list)
    for i in range(1,len(gene_list)-1):
        #avoid considering if it is hypothetical proteins or transposase
        if gene_list[i]!= 'hypothetical protein CDS,' and not re.search(r'transposase', gene_list[i]):
            #if not hypothetical or transposase, see if it is same to its adjacent genes
            #query_num variable to ensure the compared genes are actually adjacent
            if gene_list[i] == gene_list[i+1] and query_num[i] == query_num[i+1]-1:
                #similar to previous entry
                repeated_list.append(gene_list[i])
                file2.write(full_info[i])
                number = number + 1
                    
            elif gene_list[i] == gene_list[i-1] and query_num[i] == query_num[i-1]+1:
                #similar to next entry
                repeated_list.append(gene_list[i])
                file2.write(full_info[i])
                number = number + 1
            else:
                Truncatedlist.append(gene_list[i])
        else: #hypothetical protein or transposase
            if re.search(r'transposase', gene_list[i]):
                transposase_num += 1
            else:
                hypothetical_proteins += 1

            
    for i in Truncatedlist:
        file4.write(i+"\n")
    file4.close()
        
    print("no. of genes:", total_genes)
    print ("number of hypothetical proteins:", hypothetical_proteins "\nNumber of transposase proteins: ", transposase_num)
    number2 = len(set(repeated_list))
    print ("frameshifts are possible in",number2, "genes which could be split into ", number, "genes")
    print ("number of genes that are not split but should be checked for possible truncation or over extension: ", total_genes-number)
    file3.write(str(repeated_list))
    file3.close()
    file2.close()
    return number

def main():
    parser = argparse.ArgumentParser(description='This is a program to get the adjacent repeating annotation which could possibly be due to frameshift error in a genome')
    parser.add_argument("annotation_csv_file", help="annotation '.csv' file contianing the annotation for the genome"\
        , type=str)
    parser.add_argument("repeated_entries", help="Name of file to output repeated annotations"\
        , type=str)
    args = parser.parse_args()
    annotation_file=args.annotation_csv_file
    repeating_entries = args.repeated_entries
    repeat_list = "Repeated_genes_list"

    frameshifts = collect_repeats(annotation_file, repeating_entries, repeat_list)
    print("number of frameshifts:",frameshifts)

if __name__=='__main__':
    main()