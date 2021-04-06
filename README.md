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

For help on the usage:

```
python Rotate_genome.py

```

contact menolin.shrma@gmail.com for any questions 
