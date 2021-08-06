# Scripts
Some useful scripts for bioinformatics analyses of genomes

## 1. find_repeated_annotation.py
Use the script to get a list of genes which occur adjacently in a genome annotation. A single gene could have been split due to a frameshift error in the genome. 

Output:
  1. list of annotations that occured adjacently in the annotation file
  2. Number of transposases and hypothetical proteins 

### Usage
```
python find_repeated_annotation.py <annotation file name in .csv format> <output file name>
```

For help on the usage:
```
python find_repeated_annotaion.py --help 
```

## 2. Rotate_genome.py
Set the starting position of your genome at the desired point. E.g.Set dnaA as the starting gene in the genome

Usage:
```
python Rotate_genme.py <dnaA or desired gene postion number in the existing genome> <genome file name>
```

For help on the usage:

```
python Rotate_genome.py --help

```
## 3. extract_ITS_region.py
Extract ITS sequences from a fasta file, using information in gff file. Internal Transcribed Region is region between 16S and 23S ribosomal RNA sequences which are used for phylogenetic anlysis of organisms. This can be used to extract ITS sequences from genomes from GenBank and gff files for instance.
Output will be stored as ITS_sequences.fasta in your working folder. Works in unix/linux environment

Usage:  
```
python extract_ITS_region.py <fasta_filename> <gff_filename>
```
For help on the usage:

```
python extract_ITS_region.py --help|-h
```

## 3. extract_selected_IDs.py
Extract sequences from a fasta file for desired IDs in gff file. just provide the comma separated list of IDs e.g.: "cds-WP_011082914.1,cds-WP_011082919.1,cds-WP_011082920.1"
Output will be stored as extracted_sequences.fasta in your working folder.

Usage:  
```
python extract_selected_IDs.py <fasta_filename> <gff_filename>
```
For help on the usage:

```
python extract_selected_IDs.py --help|-h
```


contact menolin.shrma@gmail.com for any questions 
