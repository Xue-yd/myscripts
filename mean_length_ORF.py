import sys
from Bio import SeqIO


my_dict={}
for record in SeqIO.parse("C:\\Users\\17710\\Desktop\\Amel.gene.longest.orf.fa","fasta"):
    id = str(record.description).split('.')[0][1:]
    lens=len(record.seq)
    my_dict[id]=lens

total=0
for key,value in my_dict.items():
    print(key,value)
    total+=value

mean=total/999
print(mean)