cd ../reads/matched/


R1='_R1.fastq'
RN='_R1_trimmed.fastq'

ls | while read i;
do
	echo $i;
	cd $i/;
	pwd;
	/fh/fast/shou_w/bin/Robin/fastx/fastx_trimmer -f 5 -i $i$R1 -o $i$RN -Q 33
	cd ../
done

cd ../../scripts/