import sys

f=open(sys.argv[1],'r')
m=open(sys.argv[2],'w')

ll=f.readlines()

i=0

bins={}
for line in ll:
	line =line.split()
	if i %10000==0:
		print i,len(ll),float(i)/float(len(ll))*100
	i+=1
	#print line
	if len(line)>5 and line[0]!='@PG':
		if int(line[4])>=20:
			chr=line[2]
			pos=line[3]
			key=chr+'_'+pos
			if key not in bins.keys():
				bins[key]=1
			else:
				bins[key]+=1
				
				



for key in bins.keys():
	x=key+','+str(bins[key])+'\n'
	m.write(x)
	
	
	
f.close()
m.close()	