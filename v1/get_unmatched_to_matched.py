## Written by Robin Green, Shou Lab, FHCRC##
# The purpose of this script is to scan the 'unmatched reads' in the RADSeq files and match them to sample reads (ones retrieved from
# from splitting 4bp barcodes) based on read names (paired end reads have the same name other than the '1' or '2' saying what direction
# the read is going). 
# End result: 2 files (labeled with 'new') of previously unmatched reads that match to the sample reads (in just the one directory for a given sample, use the shell script 
# 'get_unmatched.sh' for all samples)



#usage: python get_unmatched_to_matched.py Known_reads.R1_fastq Known_reads.R2.fastq unmatched_reads.R1.fastq unmatched_reads.R2.fastq



import sys

f=open(sys.argv[1],'r')
r=open(sys.argv[2],'r')
uf=open(sys.argv[3],'r')
ur=open(sys.argv[4],'r')

ll=f.readlines() #open R1 file of known sample reads

#make dictionaries for storing read sequences and quality scores

forward_match_seq={}
forward_match_score={}

reverse_match_seq={}
reverse_match_score={}

forward_unmatch_seq={}
forward_unmatch_score={}

reverse_unmatch_seq={}
reverse_unmatch_score={}


for1={}
rev1={}
unfor1={}
unrev1={}



# for going into needed directory from 'scripts' directory
new_for=sys.argv[1].split('/')[-1]
new_for=new_for.split('.')
new_for=new_for[0]+'_new.'+new_for[1]

new_rev=sys.argv[2].split('/')[-1]
new_rev=new_rev.split('.')
new_rev=new_rev[0]+'_new.'+new_rev[1]



n=open(new_for,'w')
k=open(new_rev,'w')

i=0
# build dictionary of matched forward reads for reference
while  i < len(ll):
	#line1=line
	line=ll[i]
	line1=line
	if line[0:3]=='@DH':
		line=line.rstrip('\n')
		
		line=line.split()[0]
		forward_match_seq[line]=ll[i+1].rstrip('\n')
		forward_match_score[line]=ll[i+3].rstrip('\n')
		line1=line1.split()[1]
		for1[line]=line1
		if i%100000==0:
			print i,len(ll),float(i)/float(len(ll))*100
	i+=1
	
i=0
# build dictionary of matched forward reads for reference

f.close()
	
ll=r.readlines()
while  i < len(ll):
	line=ll[i]
	line1=line
	if line[0:3]=='@DH':
		line=line.rstrip('\n')
		
		line=line.split()[0]
		reverse_match_seq[line]=ll[i+1].rstrip('\n')
		reverse_match_score[line]=ll[i+3].rstrip('\n')
		line1=line1.split()[1]
		rev1[line]=line1
		if i%100000==0:
			print i,len(ll),float(i)/float(len(ll))*100
			
	i+=1
	
	
r.close()
i=0
	
ll=uf.readlines()
while  i < len(ll):
	line=ll[i]
	line1=line
	if line[0:3]=='@DH':
		line=line.rstrip('\n')
		
		line=line.split()[0]
		forward_unmatch_seq[line]=ll[i+1].rstrip('\n')
		forward_unmatch_score[line]=ll[i+3].rstrip('\n')
		line1=line1.split()[1]
		unfor1[line]=line1
		if i%100000==0:
			print i,len(ll),float(i)/float(len(ll))*100
	
	i+=1
	
	
uf.close()
i=0
	
ll=ur.readlines()

while  i < len(ll):
	line=ll[i]
	line1=line
	if line[0:3]=='@DH':
		line=line.rstrip('\n')
		line=line.split()[0]
		reverse_unmatch_seq[line]=ll[i+1].rstrip('\n')
		reverse_unmatch_score[line]=ll[i+3].rstrip('\n')
		line1=line1.split()[1]
		unrev1[line]=line1
		if i%1000000==0:
			print i,len(ll),float(i)/float(len(ll))*100
			
			
	
	i+=1	
	

ur.close()



i=0
length=len(forward_match_seq.keys())

print 'set'

dif=set(reverse_unmatch_seq.keys())-set(forward_match_seq.keys())

union=set(reverse_unmatch_seq.keys())-dif ## only keys in forward_match_seq_keys()



for key in forward_match_seq.keys():
	i+=1
	if i%10000==0:
		print i,len(forward_match_seq.keys()),float(i)/float(len(forward_match_seq.keys()))*100
	if key in union:
		k.write(key)
		k.write(' ')
		k.write(unrev1[key])
		k.write('\n')
		k.write(reverse_unmatch_seq[key])
		k.write('\n')
		k.write('+')
		k.write('\n')
		k.write(reverse_unmatch_score[key])
		k.write('\n')
		
		
dif=set(forward_unmatch_seq.keys())-set(reverse_match_seq.keys())

union=set(forward_unmatch_seq.keys())-dif ## only keys in reverse_match_seq_keys()		
	
for key in reverse_match_seq.keys():
	i+=1
	if i%10000==0:
		print i,len(reverse_match_seq.keys()),float(i)/float(len(reverse_match_seq.keys()))*100
	if key in union:
		n.write(key)
		n.write(' ')
		n.write(unfor1[key])
		n.write('\n')
		n.write(forward_unmatch_seq[key])
		n.write('\n')
		n.write('+')
		n.write('\n')
		n.write(forward_unmatch_score[key])
		n.write('\n')
			
	
	
	
print'closing'
n.close()
k.close()	
	

		
		
