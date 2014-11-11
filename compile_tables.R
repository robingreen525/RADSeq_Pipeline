setwd('Z:/shougroup/lab_users/Robin/Notebook/Partner Coevolution/Sequence_Analysis/JP/tmp/matched/euploid_panel/')


change_row_names<-function(table)
{
  #print(nrow(table))
  names<-c()
  for(i in 1:nrow(table))
  {
    key=paste(table[i,1],table[i,2],sep='_')
    #print(key)
    names<-append(names,key)
    
  }
  
  
  row.names(table)<-names
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
  for(i in 1:nrow(x))
  {
    if(x[i,1]<=450 && x[i,1]>=125)
    {
      temp<-x[i,]
      temp1<-temp
      temp<-temp[-1]
      #print(temp)
      s<-sd(temp)
      m<-mean(temp)
      cv<-s/m
      # print(cv)
      
      new<-append(temp1,m)
      new<-append(new,cv)
      new_table<-rbind(new_table,new)
      new_names<-append(new_names,rownames(x[i,]))
    }
    
    
  }
  
  rownames(new_table)<-new_names
  
  return(new_table)
  
}


a<-read.table("JR26/JR26.marker.complete",header=F)
b<-read.table("WY1335/WY1335.marker.complete",header=F)
c<-read.table('WY1341/WY1341.marker.complete',header=F)
d<-read.table('WY1342/WY1342.marker.complete',header=F)
e<-read.table('WY1347/WY1347.marker.complete',header=F)
f<-read.table('WY1430/WY1430.marker.complete',header=F)
g<-read.table('WY1521/WY1521.marker.complete',header=F)
h<-read.table('WY1580/WY1580.marker.complete',header=F)
i<-read.table('WY1626/WY1626.marker.complete',header=F)
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
k<-change_row_names(k)

ab<-RJG_cbind(a,b)
abc<-RJG_cbind(ab,c)
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
all<-RJG_cbind(abcdefghij,k)
z<-RJG_getCV(all)
z
save.image('2014-07-12.RData')
