import sys
from Bio import SeqIO

in_fasta=sys.argv[1]
out=sys.argv[2]

my_dict={}
for record in SeqIO.parse(open(in_fasta),"fasta"):
	id = str(record.description).split(':')[0][1:]
	lens=len(record.seq)
	my_dict[id]=lens

num=0
total=0

with open(out,"w") as fout:
	for key,value in my_dict.items():
		fout.write(key+"\t")
		fout.write(str(value)+"\n")
		total+=value
		num+=1
	
mean=total/num
print(mean)
