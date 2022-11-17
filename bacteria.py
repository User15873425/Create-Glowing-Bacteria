def split_plasmid(sequence, restriction_site):
    return sequence[:(idx := sequence.find(restriction_site) + 1)], sequence[idx:]


def cut_gfp(sequence, restriction_sites):
    return sequence[sequence.find(restriction_sites[0])+1:sequence.rfind(restriction_sites[1])+1]


def ligation(plasmid_sequence, gfp_sequence):
    return gfp_sequence.join(plasmid_sequence)


def complementary(sequence):
    return ''.join({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}[i] for i in sequence)


with open(input()) as f:
    plasmid_strand, split_site, gfp_strand, cut_ends = list(map(str.split, f.readlines()))
final_strand = ligation(split_plasmid(*plasmid_strand, *split_site), cut_gfp(*gfp_strand, cut_ends))
print(final_strand, complementary(final_strand), sep='\n')
