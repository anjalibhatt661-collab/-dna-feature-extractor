def gc_content(seq):
    """Calculates GC percentage of a DNA sequence."""
    g = seq.count('G')
    c = seq.count('C')
    return round((g + c) / len(seq) * 100, 2)

def basic_stats(seq):
    """Returns basic statistics of a DNA sequence."""
    if len(seq) == 0:
        print("Warning: empty sequence found, skipping.")
        return None
    return {
        'length': len(seq),
        'A': seq.count('A'),
        'T': seq.count('T'),
        'G': seq.count('G'),
        'C': seq.count('C'),
        'GC%': gc_content(seq)
    }
def kmer_frequency(seq, k=3):
    """Counts all k-mers of length k in a DNA sequence."""
    kmers = {}                          
    for i in range(len(seq) - k + 1):  
        kmer = seq[i:i+k]              
        kmers[kmer] = kmers.get(kmer, 0) + 1  
    return dict(sorted(kmers.items(),
                key=lambda x: x[1], reverse=True))  
def codon_usage(seq):
    """Counts codon usage in a DNA sequence."""
    codons = {}                         
    for i in range(0, len(seq) - 2, 3): 
        codon = seq[i:i+3]              
        codons[codon] = codons.get(codon, 0) + 1   
    return dict(sorted(codons.items(),
                key=lambda x: x[1], reverse=True))  