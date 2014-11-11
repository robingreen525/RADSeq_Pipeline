
cd ../reads/matched/


R1='_R1.fastq'
R2='_R2.fastq'
ls | while read i;
do
	echo $i;
	cd $i/;
	pwd;
	python ../../../scripts/get_unmatched_to_matched.py $i$R1 $i$R2 ../../unmatched/unmatched_R1.fastq ../../unmatched/unmatched_R2.fastq
	cd ../;
done