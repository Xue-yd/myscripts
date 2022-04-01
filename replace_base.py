#!/usr/vin/python

#replace the reference alleles with the alternative alleles at all these SNP sites on the genome
#usage: python replace_base.py in_fasta_file snp_file out_fasta_file

import sys
import pysam

in_fasta=sys.argv[1]
snp_file=sys.argv[2]
out_fasta=sys.argv[3]

def get_seqs(in_fasta_file):
	"""
	get seqs from genome fasta file.

	dict_of_seqs : dict_of_seqs[seq_id] -> seq	

	Parameters
	----------

	in_fasta_file : str
		Path to read the sequences to.
	"""

	fa=pysam.Fastafile(in_fasta_file)
	chroms=fa.references
	dict_of_seqs={chrom:list(fa.fetch(chrom)) for chrom in chroms}
	fa.close()
	return dict_of_seqs

def replace_base(snp_file,dic):
	"""
	replace the references alleles with the alternative alleles at SNP sites.
	
	Parameters
	----------

	snp_file : str
		the file path of SNPs infomation file.
	
	dic : dic[seq_id] -> seq
		Sequences indexed by sequence id.
	
	"""
	snp_fh=open(sys.argv[2],'r')
	line=snp_fh.readline()
	while line:
		lines=line.split()
		lines[1]=int(lines[1])-1
		dic[lines[0]][lines[1]]=lines[3]
		line=snp_fh.readline()
	for key,value in dic.items():
		dic[key]="".join(value)
	snp_fh.close()
	return dic

def write_fasta(seqs,out_fasta_file,wrap=80):
	"""write sequeces to a fasta file.
	parameters
	----------
	
	seqs : dict[seq_id] -> seq
		Sequences indexed by sequence id.
	out_fasta : str
		Path to write the sequences to.
	wrap : int
	Number of AA/NT before the line is wrapped.
	""" 

	with open(out_fasta_file,'w') as fout:
		for seq_id,seq in seqs.items():
			fout.write('>{}\n'.format(seq_id))
			for i in range(0,len(seq),wrap):
				fout.write('{}\n'.format(seq[i:i+wrap]))
my_dict=get_seqs(in_fasta)
replaced_dict=replace_base(snp_file,my_dict)
write_fasta(replaced_dict,out_fasta,wrap=80)
