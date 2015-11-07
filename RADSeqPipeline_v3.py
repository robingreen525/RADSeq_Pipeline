#!/bin/sh
##############
#RADSeq Analysis Pipeline Python Script
import os
import sys
import time
import datetime


##############
##provide directory to where everything should be done
dir=sys.argv[1]
print(dir)
os.chdir(dir)
#os.system('pwd')


##############
# create a reads directory where reads will be put after splitting by barcode
if not os.path.exists('reads'):
    os.makedirs('reads')



##############
# split by barcode of sample (specified during library preparation). Barcodes are in 'barcode.txt' file
# use fastxt toolkit barcode splitter program
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print st,'> Splitting R1 files by barcode'
a="cat *R1* | /fh/fast/shou_w/bin/Robin/fastx/fastx_barcode_splitter.pl --bcfile barcodes.txt --bol --prefix reads/RJG_ --suffix '_R1.fastq'"
os.system(a)

# I only the R1 files will have the 4 bp barcodes for each sample. I need to use the read names for the R2 reads to match them 


os.chdir('reads')

#put all R2 reads into one file
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print st,'> Concatenating R2 files'
a='cat RJG_unmatched_R1.fastq ../*R2* >R2.fastq'
os.system(a)





f=open('../barcodes.txt')
ll=f.readlines()



for line in ll:
	line=line.split('\t')[0]
	
	################
	# # for each new sample, split by barcode, call the 'get_unmatched_to_matched_v3.py' script to get unmatched reads, since half of reads should't
	# # have 4 bp barcode
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	print st,'> Starting read pairing for ',line
	a='python /fh/fast/shou_w/bin/get_unmatched_to_matched_v3.py RJG_'+line+'_R1.fastq R2.fastq RJG_'+line+'_R2_new.fastq'
	os.system(a)
	
	#make a directory for the sample you are analyzing and move all read files to that directoty
	if not os.path.exists(line):
 		os.makedirs(line)
 		w='mv *'+line+'_R1.fastq '+line+'/'
 		os.system(w)
 		w='mv *'+line+'_R2_new.fastq '+line+'/'
 		os.system(w)
 		
 	#trim 4bp barcode from R1 reads

 	os.chdir(line)
 	w='/fh/fast/shou_w/bin/Robin/fastx/fastx_trimmer -f 5 -i RJG_'+line+'_R1.fastq -o RJG_'+line+'_R1.trimmed.fastq -Q 33'
 	os.system(w)
	
	w= 'bwa aln -n 3 /fh/fast/shou_w/NextGenSeq/reference/RM11.fasta  RJG_'+line+'_R1.trimmed.fastq > RJG_'+line+'_R1.sai'
	os.system(w)
	
	#bwa samse ../../../reference/RM11.fasta $i.sai $i$R2 >$i.3mismatch.sam
	
	w='bwa samse /fh/fast/shou_w/NextGenSeq/reference/RM11.fasta RJG_'+line+'_R1.sai RJG_'+line+'_R1.trimmed.fastq > '+line+'.3mismatch.sam' 
	os.system(w)

	#convert sam file to sorted bam (will be good for ordering markers), then back to sam file	
	#samtools view -bS file.sam | samtools sort - file_sorted
	
	w='samtools view -bS '+line+'.3mismatch.sam |samtools sort - '+line+'.3mismatch.sorted'
	os.system(w)
	

	#remove intermediate (unsorted) sam file
	w='rm *.sam'
	os.system(w)
	
	# convert sorted bam to sorted sam file
	
	w='samtools view -h '+line+'.3mismatch.sorted.bam > '+line+'.3mismatch.sorted.sam'
	os.system(w)

	#remove intermediate (unsorted) bam file
	w='rm *.bam'
	os.system(w)

	
	#python ../../../scripts/bin_marker_SAM.py $i.3mismatch.sam $i.markers

	w='python /fh/fast/shou_w/bin/bin_marker_SAM.py '+line+'.3mismatch.sorted.sam '+line+'.markers'
	os.system(w) 
	
	#python ../../../scripts/calculate_fragment_length.py ../../../reference/Mfe1_sites_rm11.txt $i.markers $i.3mismatch.sam >$i.marker.Mbo1
	w='python /fh/fast/shou_w/bin/calculate_fragment_length.py  /fh/fast/shou_w/NextGenSeq/reference/Mfe1_sites_rm11.txt '+line+'.markers '+line+'.3mismatch.sorted.sam > '+line+'.markers.Mfe1'
	os.system(w)


	############
	#repeat for Mbo1 sites
	
	w= 'bwa aln -n 3 /fh/fast/shou_w/NextGenSeq/reference/RM11.fasta  RJG_'+line+'_R2_new.fastq > RJG_'+line+'_R2.sai'
	os.system(w)
	
	#bwa samse ../../../reference/RM11.fasta $i.sai $i$R2 >$i.3mismatch.sam
	
	w='bwa samse /fh/fast/shou_w/NextGenSeq/reference/RM11.fasta RJG_'+line+'_R2.sai RJG_'+line+'_R2_new.fastq > '+line+'.1.3mismatch.sam' 
	os.system(w)

#convert sam file to sorted bam (will be good for ordering markers), then back to sam file	
# 	#samtools view -bS file.sam | samtools sort - file_sorted
# 	
	w='samtools view -bS '+line+'.1.3mismatch.sam |samtools sort - '+line+'.1.3mismatch.sorted'
	os.system(w)
	

# 	#python ../../../scripts/calculate_fragment_length.py ../../../reference/Mfe1_sites_rm11.txt $i.markers $i.3mismatch.sam >$i.marker.Mbo1
# 
# 	#remove intermediate (unsorted) sam file
	w='rm *.sam'
	os.system(w)
# 	
# 	# convert sorted bam to sorted sam file
	
	w='samtools view -h '+line+'.1.3mismatch.sorted.bam > '+line+'.1.3mismatch.sorted.sam'
	os.system(w)
# 
# 	#remove intermediate (unsorted) bam file
	w='rm *.bam'
	os.system(w)
# 
# 	
# 	#python ../../../scripts/bin_marker_SAM.py $i.3mismatch.sam $i.markers
# 
	w='python /fh/fast/shou_w/bin/bin_marker_SAM.py '+line+'.1.3mismatch.sorted.sam '+line+'.1.markers'
	os.system(w) 
	
# 	#python ../../../scripts/calculate_fragment_length.py ../../../reference/Mfe1_sites_rm11.txt $i.markers $i.3mismatch.sam >$i.marker.Mbo1
	w='python /fh/fast/shou_w/bin/calculate_fragment_length.py  /fh/fast/shou_w/NextGenSeq/reference/Mbo1_sites_rm11.txt '+line+'.1.markers '+line+'.1.3mismatch.sorted.sam > '+line+'.markers.Mbo1'
	os.system(w) 

	os.makedirs('final')
	
	w='cat '+line+'.markers.Mbo1 '+line+'.markers.Mfe1 > final/'+line+'.markers.complete'
	os.system(w)
	
	w='rm *'
	os.system(w)
	
	w=' mv final/* ./'
	os.system(w)
	
	w='rm -rf final/'
	os.system(w)	
	



	
	
	
	
	os.chdir('../')	
	
	
	