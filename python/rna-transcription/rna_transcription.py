def to_rna(dna_strand):

    new_strand = ""

    transcriptions = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }

    for complement in dna_strand:
        new_strand += transcriptions[complement]

    return new_strand
