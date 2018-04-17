def dna_to_rna(dna):
    rna = ''
    for letter in dna:
        if letter == 'A':
            rna += 'U'
        elif letter == 'T':
            rna += 'A'
        elif letter == 'C':
            rna += 'G'
        else:
            rna += 'C'

    return rna
