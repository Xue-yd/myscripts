import random
import sys
from Bio import SeqIO

in_fasta=sys.argv[1]
out=sys.argv[2]

my_dict={}
name_ids=[]
for record in SeqIO.parse(open(in_fasta),"fasta"):
    name = str(record.description).split('.')[0][1:]
    name_ids.append(name)
    my_dict[name]=record.seq

num_list=[]
useful_name_list=[]
while len(num_list) < 500:
    num = random.randint(0,699)
    if num not in num_list:
        num_list.append(num)
        useful_name_list.append(name_ids[num])
print(num_list)

print(my_dict)

useful_dict={}
for i in useful_name_list:
    useful_dict[i]=my_dict[i]

def write_fasta(seqs, out_fasta_file, wrap=80):
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

    with open(out_fasta_file, 'w') as fout:
        for seq_id, seq in seqs.items():
            fout.write('>{}\n'.format(seq_id))
            for i in range(0, len(seq), wrap):
                fout.write('{}\n'.format(seq[i:i + wrap]))

write_fasta(useful_dict,out)