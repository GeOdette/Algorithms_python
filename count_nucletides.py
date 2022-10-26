

from numpy import PINF


dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'


def count_nucleotides(dna):
    count_a, count_g, count_c, count_t = 0, 0, 0, 0

    for base in dna:
        if base == 'A':
            count_a += 1
        elif base == 'C':
            count_c += 1
        elif base == 'G':
            count_g += 1
        elif base == 'T':
            count_t += 1
    return(count_a, count_c, count_g, count_t)


if __name__ == "__main__":
    counts = count_nucleotides(dna)
    count_a, count_g, count_c, count_t = counts
    print(f'A: {count_a}, G: {count_g}, C: {count_c}, T: {count_t}')
