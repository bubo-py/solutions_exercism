
def distance(strand_a, strand_b):
    a = [letter for letter in strand_a]
    b = [letter for letter in strand_b]
    if len(strand_a) != len(strand_b):
        raise ValueError('lengths of both given strands are not the equal')

    else:
        hamming = []
        for n in range(len(a)):
            if a[n] != b[n]:
                hamming.append(a[n])
        return len(hamming)
