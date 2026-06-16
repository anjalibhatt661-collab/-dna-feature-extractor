import sys
from src.read_fasta import read_fasta
from src.features import basic_stats, kmer_frequency, codon_usage
from src.visualize import plot_kmer, plot_nucleotide_composition, plot_codon_usage

# Accept file path from terminal or use default
filepath = sys.argv[1] if len(sys.argv) > 1 else 'data/sample.fasta'

print("🧬 DNA Sequence Feature Extractor")
print("=" * 40)
print(f"Analyzing: {filepath}")
print("=" * 40)

sequences = read_fasta(filepath)

for seq_id, seq in sequences.items():
    print(f"\nID: {seq_id}")
    print("-" * 40)

    # Basic Stats
    stats = basic_stats(seq)
    print(f"Length:  {stats['length']} bases")
    print(f"A: {stats['A']}  T: {stats['T']}  G: {stats['G']}  C: {stats['C']}")
    print(f"GC%:    {stats['GC%']}")

    # K-mer Frequency
    kmers = kmer_frequency(seq, k=3)
    print("\nTop 5 K-mers (k=3):")
    for kmer, count in list(kmers.items())[:5]:
        print(f"  {kmer}: {count}")

    # Codon Usage
    codons = codon_usage(seq)
    print("\nTop 5 Codons:")
    for codon, count in list(codons.items())[:5]:
        print(f"  {codon}: {count}")

    # Charts
    print("\nGenerating k-mer chart...")
    plot_kmer(kmers)

    print("Generating nucleotide chart...")
    plot_nucleotide_composition(stats)

    print("Generating codon chart...")
    plot_codon_usage(codons)

print("\n" + "=" * 40)
print("Analysis complete! Charts saved.")