'''
Created a file named transcribe.py. In this file, I created a function
named dna to rna that takes one parameter. The function should translate the template
DNA sequence to its mRNA and return the mRNA.
'''

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
