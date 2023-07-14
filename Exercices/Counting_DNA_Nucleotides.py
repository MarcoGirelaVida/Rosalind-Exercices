'''
EXERCICE 1 - ROSALIND - Counting DNA Nucleotides
DATE: 19-05-2023
AUTOR: Marco Girela Vida

PROBLEM:
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

def read_n_bytes_of_file(file_name : str, n_bytes : int) -> str:
    f = open(file_name, 'r')
    return f.read(n_bytes).strip()

'''
# Function to count the number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
def count_nucleotides(DNA: str) -> dict:

    n_nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for nucleotide in DNA:
        n_nucleotides[nucleotide] += 1
    
    return n_nucleotides
'''

# Solution find in Rosalind solutions forum aparently 10x faster slightly modify
def nucleotides_frecuency(DNA: str) -> dict:

    nucleotides_frec = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for nucleotide in nucleotides_frec:
        nucleotides_frec[nucleotide] = DNA.count(nucleotide)

    return nucleotides_frec


DNA : str = read_n_bytes_of_file("./Data/rosalind_dna.txt", 1000)
n_nucleotides = nucleotides_frecuency(DNA)

for nucleotide in n_nucleotides:
    print(nucleotide, " : ", n_nucleotides[nucleotide])