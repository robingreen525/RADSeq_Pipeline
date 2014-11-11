#!/bin/sh
## Written by Robin Green, Shou Lab, FHCRC##
## The purpose of this script is to split samples from paired-end RADSeq (courtesy of Henikoff lab, FHCRC)
## into each respecitve sample. The samples have already by parsed away using the same 6 bp barcode by Andy 
## Marty (FHCRC Sequencing core). I will use the fastx toolkit for this (http://hannonlab.cshl.edu/fastx_toolkit/commandline.html#fastx_trimmer_usage)

#Needed: barcodes.txt-- Barcode file with sample names.


cd ../

cat *L001_R1* | /fh/fast/shou_w/bin/Robin/fastx/fastx_barcode_splitter.pl --bcfile barcodes.txt --bol --prefix reads/RJG_ --suffix '_L001_R1.fastq'
cat *L001_R2* | /fh/fast/shou_w/bin/Robin/fastx/fastx_barcode_splitter.pl --bcfile barcodes.txt --bol --prefix reads/RJG_ --suffix '_L001_R2.fastq'

cat *L002_R1* | /fh/fast/shou_w/bin/Robin/fastx/fastx_barcode_splitter.pl --bcfile barcodes.txt --bol --prefix reads/RJG_ --suffix '_L002_R1.fastq'
cat *L002_R2* | /fh/fast/shou_w/bin/Robin/fastx/fastx_barcode_splitter.pl --bcfile barcodes.txt --bol --prefix reads/RJG_ --suffix '_L002_R2.fastq'

cd scripts/