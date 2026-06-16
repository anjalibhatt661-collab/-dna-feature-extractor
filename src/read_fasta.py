def read_fasta(filepath):
    """Reads a FASTA file and returns a dictionary of sequences."""
    sequences = {}      # dictionary to store all sequences
    current_id = None   # tracks current sequence ID
    
    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()          # remove spaces/newlines
                if line.startswith('>'):     # ID line starts with >
                    current_id = line[1:]    # remove the > character
                    sequences[current_id] = ''  # start empty sequence
                else:
                    sequences[current_id] += line.upper()  # add sequence line
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found. Please check the path.")
    
    return sequences