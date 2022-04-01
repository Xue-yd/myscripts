#!/usr/bin/python

#usage: python extract_fa_by_chr.py in_fasta_file out_fasta_file chr_num

import sys
import pysam

in_fasta=sys.argv[1]
out_fasta=sys.argv[2]
chr_n=sys.argv[3]

fa=pysam.Fastafile(in_fasta)
chrs=fa.references
chroms=[]
for i in chrs:
	if i[1]!="W": #remove contig :NW_XXX
		chroms.append(i)

del chroms[16]  #remove mt contig
my_seqs={chrom:list(fa.fetch(chrom)) for chrom in chroms}
fa.close()

	
def write_fasta(seqs,chr_num,out_fasta_file,wrap=80):
	"""write sequeces to a fasta file.
	parameters
	----------
	
	seqs : dict[seq_id] -> seq
		Sequences indexed by sequence id.
	out_fasta : str
		Path to write the sequences to.
	wrap : int
	Number of AA/NT before the line is wrapped.
	chr_num
    """
	#chr_number=chr_num-1 
	#seq_list=seqs.get(chroms[chr_number])
	#seq="".join(seq_list)
	chr_num=int(chr_num)
	seq="".join(seqs.get(chroms[chr_num-1]))
	with open(out_fasta_file,'w') as fout:
		fout.write('>chr{}\n'.format(chr_num))
		for i in range(0,len(seq),wrap):
			fout.write('{}\n'.format(seq[i:i+wrap]))
        

write_fasta(my_seqs,chr_n,out_fasta,wrap=80)
