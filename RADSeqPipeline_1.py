#!/bin/sh
##############
#RADSeq Analysis Pipeline Python Script
import os
import sys


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
# use fastxt toolkit barcode splitter progam
a="cat *R1* | /fh/fast/shou_w/bin/Robin/fastx/fastx_barcode_splitter.pl --bcfile barcodes.txt --bol --prefix reads/RJG_ --suffix '_L001_R1.fastq'"
b="cat *R2* | /fh/fast/shou_w/bin/Robin/fastx/fastx_barcode_splitter.pl --bcfile barcodes.txt --bol --prefix reads/RJG_ --suffix '_L001_R2.fastq'"
os.system(a)
os.system(b)

os.chdir('reads')

###############
# for each new sample, split by barcode, call the 'get_unmatched_to_matched.py' script to get unmatched reads, since half of reads should't
# have 4 bp barcode

f=open('../barcodes.txt')
ll=f.readlines()

for line in ll:
	line=line.split('\t')[0]
	print line
	
	
	#get the unmatched reads (those lacking 4 bp barcodes) and match to known sample reads by read name
	#usage: python get_unmatched_to_matched.py Known_reads.R1_fastq Known_reads.R2.fastq unmatched_reads.R1.fastq unmatched_reads.R2.fastq
	w='python /fh/fast/shou_w/bin/get_unmatched_to_matched.py RJG_'+line+'_L001_R1.fastq RJG_'+line+'_L001_R2.fastq RJG_unmatched_L001_R1.fastq RJG_unmatched_L001_R2.fastq'
	print(w)
	os.system(w)
	
	
	#concatenate all R1 and R2 files so and remove any intermediate files
	w='cat RJG_'+line+'_L001_R1.fastq RJG_'+line+'_L001_R1_new.fastq > RJG_'+line+'_L001_R1_all.fastq'
	z='cat RJG_'+line+'_L001_R2.fastq RJG_'+line+'_L001_R2_new.fastq > RJG_'+line+'_L001_R2_all.fastq'
	
	rmw='rm RJG_'+line+'_L001_R1.fastq'
	rmx='rm RJG_'+line+'_L001_R1_new.fastq'
	
	rmy='rm RJG_'+line+'_L001_R2.fastq'
	rmz='rm RJG_'+line+'_L001_R2_new.fastq'
	
	os.system(w)
	os.system(z)
	
	os.system(rmw)
 	os.system(rmx)
 	os.system(rmy)
 	os.system(rmz)
	
	
	###make a directory for the sample you are analyzing and move all read files to that directoty
	if not os.path.exists(line):
		os.makedirs(line)
		w='mv *'+line+'_L001_R1_all.fastq '+line+'/'
		os.system(w)
		w='mv *'+line+'_L001_R2_all.fastq '+line+'/'
		os.system(w)
		
		
	#trim 4bp barcode from R1 reads
	
	os.chdir(line)
	w='/fh/fast/shou_w/bin/Robin/fastx/fastx_trimmer -f 5 -i RJG_'+line+'_L001_R1_all.fastq -o RJG_'+line+'_L001_R1_all.trimmed.fastq -Q 33'
	os.system(w)
	
	w= 'bwa aln -n 3 /fh/fast/shou_w/NextGenSeq/reference/RM11.fasta  RJG_'+line+'_L001_R1_all.trimmed.fastq > RJG_'+line+'_L001_R1_all.sai'
	os.system(w)
	
	#bwa samse ../../../reference/RM11.fasta $i.sai $i$R2 >$i.3mismatch.sam
	
	w='bwa samse /fh/fast/shou_w/NextGenSeq/reference/RM11.fasta RJG_'+line+'_L001_R1_all.sai RJG_'+line+'_L001_R1_all.trimmed.fastq > '+line+'.3mismatch.sam' 
	os.system(w)

	#convert sam file to sorted bam (will be good for ordering markers), then back to sam file	
	#samtools view -bS file.sam | samtools sort - file_sorted
	
	w='samtools view -bS '+line+'.3mismatch.sam |samtools sort - '+line+'.3mismatch.sorted'
	os.system(w)
	

	#python ../../../scripts/calculate_fragment_length.py ../../../reference/Mfe1_sites_rm11.txt $i.markers $i.3mismatch.sam >$i.marker.Mbo1

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
	
	w= 'bwa aln -n 3 /fh/fast/shou_w/NextGenSeq/reference/RM11.fasta  RJG_'+line+'_L001_R2_all.fastq > RJG_'+line+'_L001_R2_all.sai'
	os.system(w)
	
	#bwa samse ../../../reference/RM11.fasta $i.sai $i$R2 >$i.3mismatch.sam
	
	w='bwa samse /fh/fast/shou_w/NextGenSeq/reference/RM11.fasta RJG_'+line+'_L001_R2_all.sai RJG_'+line+'_L001_R2_all.fastq> '+line+'.1.3mismatch.sam' 
	os.system(w)

	#convert sam file to sorted bam (will be good for ordering markers), then back to sam file	
	#samtools view -bS file.sam | samtools sort - file_sorted
	
	w='samtools view -bS '+line+'.1.3mismatch.sam |samtools sort - '+line+'.1.3mismatch.sorted'
	os.system(w)
	

	#python ../../../scripts/calculate_fragment_length.py ../../../reference/Mfe1_sites_rm11.txt $i.markers $i.3mismatch.sam >$i.marker.Mbo1

	#remove intermediate (unsorted) sam file
	w='rm *.sam'
	os.system(w)
	
	# convert sorted bam to sorted sam file
	
	w='samtools view -h '+line+'.1.3mismatch.sorted.bam > '+line+'.1.3mismatch.sorted.sam'
	os.system(w)

	#remove intermediate (unsorted) bam file
	w='rm *.bam'
	os.system(w)

	
	#python ../../../scripts/bin_marker_SAM.py $i.3mismatch.sam $i.markers

	w='python /fh/fast/shou_w/bin/bin_marker_SAM.py '+line+'.1.3mismatch.sorted.sam '+line+'.1.markers'
	os.system(w) 
	
	#python ../../../scripts/calculate_fragment_length.py ../../../reference/Mfe1_sites_rm11.txt $i.markers $i.3mismatch.sam >$i.marker.Mbo1
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
		