#!/bin/sh
#Protocol for RADSeq analysis (assuming RADSeq reads generated from Henikoff lab ChIP-Seq lanes)

# #if I want to rerun, must put read files back in scripts/../
# 
# 
# mkdir ../reads/
# 
# 
# 
# #1) Use barcode splitter [fastx tool kit] to split reads into respective samples by 4 bp barcodes (try_splitting.sh)
# 	#Note: Half of reads will not have 4 bp barcodes (orignally were on read with 6bp barcode that Andy used to parse away from other samples)
# 	
# bash try_splitting.sh	
# 	
# 	
# #2) Make directorys for each sample and move relevant samples into the correct directory (make_dirs.sh)
# bash make_dirs.sh
# 
# 
# 
# cd ../reads/
# mkdir matched
# mv * matched/
# mv matched/unmatched ./
# cd ../scripts/
# 
# #3) Concatenate all 'R1' and 'R2' files for each sample together (there are L001 and L002 files for R1 and R2 files, what does L001 and L002 mean-->Ask andy)(cat_files.sh)
# bash cat_files.sh
# 
# 
# 
# 
# #4) Of the 'unmatched' reads (did not have 4 bp barcodes), match to mate pairs based on read names in fastq files 
# bash get_unmatched.sh
# 
# 
# #5) Trim away 4 bp barcodes on 'R1' files prior to alignment.
# bash trim_4bp_barcode.sh
# 
# #6) Align both read files as single end reads, count marker sites, and consolidate data
# bash RADSeq_markers.sh
# 
# #7) move relevant files to euploid reference panel directory. Can be read from txt files
# mkdir ../reads/matched/euploid_panel
# 
# for line in $(cat euploid_panel.txt);
# do
# 	echo $line;
# 	pwd
# 	cd ../reads/matched/
# 	pwd
# 	mv $line* euploid_panel/ # add file check?
# 	cd ../../scripts/
# done


Rscript compile_euploid_panel.R