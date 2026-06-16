# 🧬 DNA Sequence Feature Extractor

A Python command-line tool that analyzes DNA sequences from FASTA files 
and extracts key biological features including GC content, k-mer frequencies, 
and codon usage patterns.

## Features
- Reads standard FASTA format files
- Calculates GC content and nucleotide composition
- Counts k-mer frequencies (default k=3)
- Generates codon usage table
- Produces 3 visualization charts saved as PNG files

## Requirements
- Python 3.12
- matplotlib
- seaborn

## Installation
pip install matplotlib seaborn

## How to Run

Default (uses sample E.coli genome):
python main.py

Custom FASTA file:
python main.py path/to/your/file.fasta

## Output
- Printed report with sequence stats, top k-mers and codons
- kmer_plot.png — bar chart of top 10 k-mer frequencies
- nucleotide_plot.png — pie chart of A/T/G/C composition
- codon_plot.png — bar chart of top 15 codon usage

## Sample Output
Analyzing: data/sample.fasta
ID: U00096.3 Escherichia coli str. K-12
Length: 4641652 bases
GC%: 50.79

## Author
Anjali Bhatt 
B.Tech Bioinformatics, IILM University
Batch 2025-2029

## What I Learned
- How to read and parse FASTA format files
- Calculating GC content and nucleotide composition
- K-mer frequency analysis and its biological significance
- Codon usage patterns in bacterial genomes
- Data visualization with matplotlib
- Building a command line tool in Python
- Version control with Git and GitHub