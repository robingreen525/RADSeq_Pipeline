
Protocol for RADSeq analysis (assuming RADSeq reads generated from Henikoff lab ChIP-Seq lanes)

1) Use barcode splitter [fastx tool kit] to split reads into respective samples by 4 bp barcodes (try_splitting.sh)
	Note: Half of reads will not have 4 bp barcodes (orignally were on read with 6bp barcode that Andy used to parse away from other samples)
2) Make directorys for each sample and move relevant samples into the correct directory (make_dirs.sh)
3) Concatenate all 'R1' and 'R2' files for each sample together (there are L001 and L002 files for R1 and R2 files, what does L001 and L002 mean-->Ask andy)(cat_files.sh)
4) Of the 'unmatached' reads (did not have 4 bp barcodes), match to mate pairs based on read names in fastq files 