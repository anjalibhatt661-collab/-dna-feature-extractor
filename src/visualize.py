import matplotlib.pyplot as plt

def plot_kmer(kmer_dict, top_n=10):
    top = dict(list(kmer_dict.items())[:top_n])  # get top n kmers
    plt.figure(figsize=(10, 5))
    plt.bar(top.keys(), top.values(), color='steelblue')  # bar chart
    plt.title('Top K-mer Frequencies')
    plt.xlabel('K-mer')
    plt.ylabel('Count')
    plt.xticks(rotation=45)   # rotate labels so they don't overlap
    plt.tight_layout()
    plt.savefig('kmer_plot.png')  # save as image
    plt.show()

def plot_nucleotide_composition(stats_dict):
    bases = ['A', 'T', 'G', 'C']
    counts = [stats_dict['A'], stats_dict['T'], 
              stats_dict['G'], stats_dict['C']]
    colors = ['#ff6b6b', '#ffd93d', '#6bcb77', '#4d96ff']  # colors for each base
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=bases, colors=colors, 
            autopct='%1.1f%%', startangle=90)
    plt.title('Nucleotide Composition')
    plt.tight_layout()
    plt.savefig('nucleotide_plot.png')  # save as image
    plt.show()

def plot_codon_usage(codon_dict, top_n=15):
    top = dict(list(codon_dict.items())[:top_n])  # get top n codons
    plt.figure(figsize=(12, 5))
    plt.bar(top.keys(), top.values(), color='mediumpurple')
    plt.title('Top Codon Usage')
    plt.xlabel('Codon')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('codon_plot.png')  # save as image
    plt.show()