#!/bin/sh
## Written by Robin Green, Shou Lab, FHCRC##
## The purpose is to concatenate the 'L001' and 'L002' files for each 'R1' and 'R2' file for each sample
## End result: For each sample, I should expect a single 'R1' and 'R2' file. 



cd ../reads/matched/ # go to directory where I am keeping the results of the splitting



# define shell variables for naming
s1='_L001_R1.fastq'
s2='_L001_R2.fastq'
s3='_L002_R1.fastq'
s4='_L002_R2.fastq'

he='RJG_'  # this header will likely be changed for my data
en3='R1.fastq'
en4='R2.fastq'


en1='_R1.fastq'
en2='_R2.fastq'



#read each directory
ls |while read i;
do
	#echo $i
	cd $i # moving into the directory and concatenate files

	p=$(echo $i| cut -d '_' -f2);
	echo $p
	
	cat $he$p$s1 $he$p$s3 >$p$en1
	cat $he$p$s2 $he$p$s4 >$p$en2
 	
 	#rm $he$p$en4
 	rm $he*  # remove intermediate files that are not needed
	
	
	
	cd ../
done



cd ../unmatched/







p='unmatched'

echo $p
cat $he$p$s1 $he$p$s3 >$p$en1
cat $he$p$s2 $he$p$s4 >$p$en2
rm $he*


cd ../../scripts/