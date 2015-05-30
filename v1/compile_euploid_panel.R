

setwd('../reads/matched/euploid_panel/')
#setwd('/Volumes/homes/shougroup/lab_users/Robin/Notebook/Partner Coevolution/Sequence_Analysis/JP/tmp/matched/euploid_panel/')

change_row_names<-function(table)
{
  i=0
  #print(nrow(table))
  nam<-c()
  for(i in 1:nrow(table))
  {
    keynam=paste(table[i,1],table[i,2],sep='_')

	if(keynam %in% nam){i=i+1}
	#print(nam)
	#print(i)
	#print(which(nam[i]==keynam))
    nam<-append(nam,keynam)
    #print(which(nam[i]==keynam))
  }
  
 # print(which(duplicated(nam)==TRUE)) //have about 20 duplciated markers in JR26.
  bad<-which(duplicated(nam)==TRUE)
  
   table<-table[-bad,]
  
  
  
  
    nam<-c()
  for(i in 1:nrow(table))
  {
    keynam=paste(table[i,1],table[i,2],sep='_')

	if(keynam %in% nam){i=i+1}
	#print(keynam)
	#print(i)
	#print(which(nam[i]==keynam))
    nam<-append(nam,keynam)
    #print(which(nam[i]==keynam))
  }
  
  
  table<-table
  row.names(table)<-nam
  table<-table[,-1]
  table<-table[,-1]
  table<-table[-2]
  colnames(table)<-c('Size','Prop')
  return(table)
  
}




RJG_cbind<-function(x,y)
{
  names.x<-rownames(x)
  names.y<-rownames(y)
  
  new_table=c()
  new_names<-c()
  
  #print('good')
  
  for(i in 1:length(names.y))
  {
    num.y=i
    #print(i)
    a<-which(names.x==names.y[i]) # in y, not x
    #print(a)
    if(length(a)==0)
    {
      t=c(y[i,1],rep(0,ncol(x)-1),y[i,-1])
      #print(t)
      #print(y[i,-1])
      #print('herp')
      new_table<-rbind(new_table,t)
      new_names<-append(new_names,names.y[i])
      
      
      
    }
    else
    {
      
      t=c(y[i,1],x[a,-1],y[i,-1])
      # print(t)
      new_table<-rbind(new_table,t)
      new_names<-append(new_names,names.y[i])
      
      
    }
    
  }
  
  for(i in 1:length(names.y))
  {
    num.x=i
    a<-which(names.y==names.x[i])
    if(length(a)==0)
    {
      t=c(y[i,1],y[i,-1],rep(0,ncol(y-1)))
      #print(t)
      new_table<-rbind(new_table,t)
      new_names<-append(new_names,names.x[i])
      
      
    }
    
    
  }
  
  
  rownames(new_table)<-new_names
  return(new_table)
  
  
}


RJG_getCV<-function(x)
{
  
  new_table<-c()
  new_names<-c()
  print(x)
  for(i in 1:nrow(x))
  {
    if(x[i,1]<=450 && x[i,1]>=125)
    {
      temp<-x[i,]
      print(temp)
      temp1<-temp
      temp<-temp[-1]
      #print(temp)
      s<-sd(temp)
      m<-mean(temp)
      cv<-s/m
      #print(cv)
      
      
      new<-append(temp1,m)
      new<-append(new,cv)
      new_table<-rbind(new_table,new)
      new_names<-append(new_names,rownames(x[i,]))
    }
    
    
  }
  
  rownames(new_table)<-new_names
  print(new_names)
  return(new_table)
  
}

getwd()
a<-read.table("JR26/JR26.marker.complete",header=F)
print('a')
print(head(a))
b<-read.table("WY1335/WY1335.marker.complete",header=F)
print('b')
c<-read.table('WY1341/WY1341.marker.complete',header=F)
print('c')
d<-read.table('WY1342/WY1342.marker.complete',header=F)
print('d')
e<-read.table('WY1347/WY1347.marker.complete',header=F)
print('e')
f<-read.table('WY1430/WY1430.marker.complete',header=F)
print('f')
g<-read.table('WY1521/WY1521.marker.complete',header=F)
print('g')
h<-read.table('WY1580/WY1580.marker.complete',header=F)
print('h')
i<-read.table('WY1626/WY1626.marker.complete',header=F)
print('i')
j<-read.table('WY1657/WY1657.marker.complete',header=F)
#k<-read.table('YO979/YO979.marker.complete',header=F)

print(1)
a<-change_row_names(a)
b<-change_row_names(b)
c<-change_row_names(c)
d<-change_row_names(d)
e<-change_row_names(e)
f<-change_row_names(f)
g<-change_row_names(g)
h<-change_row_names(h)
i<-change_row_names(i)
j<-change_row_names(j)
#k<-change_row_names(k)
print(2)
ab<-RJG_cbind(a,b)
print(3)
abc<-RJG_cbind(ab,c)
print(4)
abcd<-RJG_cbind(abc,d)
print(1)
abcde<-RJG_cbind(abcd,e)
print(2)
abcdef<-RJG_cbind(abcde,f)
print(3)
abcdefg<-RJG_cbind(abcdef,g)
print(4)
abcdefgh<-RJG_cbind(abcdefg,h)
print(5)
abcdefghi<-RJG_cbind(abcdefgh,i)
print(6)
abcdefghij<-RJG_cbind(abcdefghi,j)
print(7)
all<-abcdefghij

#z<-RJG_getCV(all)

euploid<-all




save.image('euploid_panel.RData')

#use apply to get cv for each row
setwd('../../../scripts/')


