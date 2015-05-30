#!/bin/sh
## Written by Robin Green, Shou Lab, FHCRC##
## The purpose of this script is to create directories for each sample to store the RADSeq fastq files in.


cd ../reads/   # go to directory where I am keeping the results of the splitting


# define shell variables for naming
s1='_L001_R1.fastq'
s2='_L001_R2.fastq'
s3='_L002_R1.fastq'
s4='_L002_R2.fastq'

he='RJG_'

#for each sample in tmp directory, create dirctory  and move files with same sample name into this directory

ls |while read i;
   do
   
    h=$(echo $i| cut -d '_' -f1); # 'JP' name, will prevent duplicate directories from being made (won't have JP)
    p=$(echo $i| cut -d '_' -f2);
  
    mkdir $p # sample name


    if [ "$h"=="RJG" ]; ##if fastq file, only fastq files have RJG_ header in name
    then	

    ## move all RJG header samples with name into new sample directory
	echo $p
	
	
	d=$he$p$s1
	mv $d $p/
	d=$he$p$s2
	mv $d $p/
	d=$he$p$s3
	mv $d $p/
	d=$he$p$s4
	mv $d $p/
	
    fi
   done

cd ../scripts/