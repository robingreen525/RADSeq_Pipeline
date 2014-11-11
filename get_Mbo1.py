
import sys

f=open(sys.argv[1],'r')




Mbo1_5='GATC'
Mbo1_3='CTAG'
#Mbo1=sys.argv[2]
#Mfe1=sys.argv[3]


ll=f.readlines()

len_genome=len(ll)

i=0
while i<len_genome:
	line=ll[i]
	if line[0]=='>':  # for each chromosome
		ID=i
		chr=line.split()[0]
		head=line
		i+=1
		contig=''
		while ll[i][0]!='>': #build long string for each contig/chromosome
			line=ll[i].rstrip('\n')
			contig+=ll[i]
			i+=1
			if i==len_genome-1:
				break
		#print len(contig)
		j=0
		while j<len(contig):
			sub_4=contig[j:j+4]
			if sub_4==Mbo1_5 or sub_4==Mbo1_3: # find 4 cutter site
				print chr.rstrip('\n')[1:],j 
				
			j+=1
	
		if i==len_genome-1:
			break