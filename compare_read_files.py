#the purpose of this script is to compare the read files from two RADSeq datasets. The reads are from the same sequencing run,
# yet when I run my RADSeq pipeline on the reads, the results are different. Reads taken from the first dataset (in the 'Euploid
# Panel directoty) produce clear and good results, but reads from the same run but in a different set of files produce 
# uninterpretable results. I noticed that the read lengths seem to differ between the first and second data set,so what I think
# happened was the seqeuencing facility trimmed the 4 bp barcodes by mistake. This script will sysetmatically check this.


# import needed libraries
import os
import sys
import argparse

#define parsing options
parser = argparse.ArgumentParser()
parser.add_argument('-firstreadfile',type=argparse.FileType('r'))
parser.add_argument('-secondreadfile', type=argparse.FileType('r'))

#parse arguments
args = parser.parse_args()

print('Opening file...')
ll=args.firstreadfile.readlines()

print('File opened')
i=0

lengths={}
while(i<len(ll)):
	line=ll[i]
	if ll[i][0]=='+':
		read=ll[i-1].rstrip('\n')
		#print len(read)
		if(len(read)) in lengths.keys():
			lengths[len(read)]+=1
		else:
			lengths[len(read)]=1
	i+=1
	
print lengths


print('Opening file...')
ll=args.secondreadfile.readlines()

print('File opened')
i=0

lengths={}
while(i<len(ll)):
	line=ll[i]
	if ll[i][0]=='+':
		read=ll[i-1].rstrip('\n')
		#print len(read)
		if(len(read)) in lengths.keys():
			lengths[len(read)]+=1
		else:
			lengths[len(read)]=1
	i+=1
	
print lengths

#results
#Opening file...
#File opened
#{24: 38084300, 1: 28636}
#Opening file...
#File opened
#{28: 42744510}

#It appears I was wrong. The most recent read files have reads that are 28 bp in length while the first
# read files have reads that are 24 bp in length. I'm guessing that if I trim away the first 4 bp of each read from the more recent
# data set, the results should be fine.