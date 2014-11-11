import sys



sam=open(sys.argv[3],'r')
sam=sam.readlines()

reads=0
reads=len(sam)


#read_count=float(sys.argv[3])
f=open(sys.argv[1],'r')

ll=f.readlines()




chrs={}


count=0
full=0
#reads=0
for line in ll:
	line=line.split()
	#print line
	if line[0] not in chrs.keys():
		chrs[line[0]]=[]
		chrs[line[0]].append(int(line[1]))
	else:
		chrs[line[0]].append(int(line[1]))
		

f=open(sys.argv[2],'r')

ll=f.readlines()

reads=len(sam)-18


for line in ll:
	line=line.split()
	key=line[0].split('_')
	#print key
	chr=key[0]+'_'+key[1]
	pos=int(key[2].split(',')[0])
	total=int(key[2].split(',')[1])
	key=chr
	#print key, pos
	dist=10000000
	for entry in chrs[key]:
		if (entry>pos):
			num=abs(entry-pos) #Mbo1 sites occurs after 5' Mfe1 site
			if num < dist:
				dist=num
		
	print key, pos, dist, total,float(total)/float(reads)
	if dist >=100 and dist <=450:
		count+=1
	full+=1

#print reads

