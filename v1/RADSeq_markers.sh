#!/bin/sh

cd ../reads/matched/

R1='_R1_trimmed.fastq'
R2='_R2_new.fastq'



ls | while read i
	do 
		if [ -d $i ]; 
		then
			cd $i
			echo $i
			pwd
			#head $i$R2
			
			bwa aln -n 3 ../../../reference/saccharomyces_cerevisiae_rm11-1a_1_supercontigs.fasta $i$R2 >$i.sai
			bwa samse ../../../reference/saccharomyces_cerevisiae_rm11-1a_1_supercontigs.fasta $i.sai $i$R2 >$i.3mismatch.sam
			python ../../../scripts/bin_marker_SAM.py $i.3mismatch.sam $i.markers
			python ../../../scripts/calculate_fragment_length.py ../../../reference/Mfe1_sites_rm11.txt $i.markers $i.3mismatch.sam >$i.marker.Mbo1
			
			
			bwa aln -n 3 ../../../reference/saccharomyces_cerevisiae_rm11-1a_1_supercontigs.fasta $i$R1 >$i.1.sai
			bwa samse ../../../reference/saccharomyces_cerevisiae_rm11-1a_1_supercontigs.fasta $i.1.sai $i$R1 >$i.1.3mismatch.sam
			python ../../../scripts/bin_marker_SAM.py $i.1.3mismatch.sam $i.1.markers
			python ../../../scripts/calculate_fragment_length.py ../../../reference/Mbo1_sites_rm11.txt $i.1.markers $i.1.3mismatch.sam >$i.marker.Mfe1
			
			
			#remove intermediate files
			rm *.sai
			rm *.sam
			rm *.markers
			
			
			cat $i.marker.Mbo1	$i.marker.Mfe1 >$i.marker.complete
			
			
			
			
			cd ../
		fi
done

cd ../../scripts

