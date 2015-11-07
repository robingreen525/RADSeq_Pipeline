# the purpose of this script is to generate RADSeq plots for each sample.

#usage example
#python generate_RADSeq_plots.py -dir /fh/fast/shou_w/NextGenSeq/RadSeq/20150320/Sample_021115/reads -barcodefile /fh/fast/shou_w/NextGenSeq/RadSeq/20150320/Sample_021115/barcodes.txt 


import os
import sys

import argparse

#define parsing options
parser = argparse.ArgumentParser()
parser.add_argument('-dir', dest='dir')
parser.add_argument('-barcodefile',type=argparse.FileType('r'))


args = parser.parse_args()

# get the path where the data are stored. will be used with other strings later
path=args.dir

strains=[]
### use the barcode file flag to get the list of strains to analyze
ll=args.barcodefile.readlines()
for line in ll:
	line=line.split('\t')
	strains.append(line[0])

for strain in strains:
	print strain
	w='Rscript /fh/fast/shou_w/NextGenSeq/RadSeq/plot_RADSeq_sample_commandline.R '+strain+' '+path
	print(w)
	os.system(w)