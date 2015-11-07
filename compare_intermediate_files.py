# the purpose of this script is to compare intermediate files generated during my RADSeq pipeline
# to determine where the discrepency between the first set of reads run and the second set.
#the reads are from the same sequencing run, yet when I run my RADSeq pipeline on the reads, the results are different.
# Reads taken from the first dataset (in the 'Euploid
# Panel directoty) produce clear and good results, but reads from the same run but in a different set of files produce 
# uninterpretable results. 

#import libraries to use

import os
import sys
import argparse

#define parsing options
parser = argparse.ArgumentParser()
parser.add_argument('-correctdir',dest='correct')
parser.add_argument('-incorrectdir', dest='incorrect')
parser.add_argument('-sample', dest='sample') 

#parse arguments
args = parser.parse_args()

sample=args.sample
correct=args.correct
incorrect=args.incorrect

correct_Mfe1=correct+'/reads/'+sample+'/'+sample+'.markers.Mfe1'
incorrect_Mfe1=incorrect+'/reads/'+sample+'/'+sample+'.markers.Mfe1'


f=open(correct_Mfe1,'r')
r=open(incorrect_Mfe1,'r')

correct_markers={}

ll=f.readlines()
for line in ll:
	line =line.split()
	key=line[0]+'_'+line[1]
	correct_markers[key]=line

f.close()

incorrect_markers={}

ll=r.readlines()
for line in ll:
	line =line.split()
	key=line[0]+'_'+line[1]
	incorrect_markers[key]=line

		

print "Markers in Correct Mfe File : "+str(len(correct_markers.keys()))
print "Markers in Incorrect Mfe File : "+str(len(incorrect_markers.keys()))

keys_a=set(correct_markers.keys())
keys_b=set(incorrect_markers.keys())

intersection = keys_a & keys_b
print "Overlap in two files : "+str(len(intersection))



#results for Mfe1 markers file for WY1335
#Markers in Correct Mfe File : 9876
#Markers in Incorrect Mfe File : 10534
#Overlap in two files : 3807

#results for Mfe1 markers file for JR30
#Markers in Correct Mfe File : 10649
#Markers in Incorrect Mfe File : 10672
#Overlap in two files : 4078