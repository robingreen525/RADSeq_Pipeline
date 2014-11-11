
RJG_logFoldDifference<-function(x,y)
{
  names.x<-rownames(x)
  names.y<-rownames(y)
  
  new_table=c()
  new_names<-c()
  
  #print('good')
  count=0
  for(i in 1:length(names.y))
  {
    num.x=i
    #print(i)
    a<-which(names.x==names.y[i])
    #print(a)
    if(length(a)!=0)
    {
      euploid=x[a,11]
      test<-y[i,2]
      fold<-test/euploid
      #if(log(fold,2)>.75)
      # print(fold) #seems to be working
      nam<-names.y[i]
      #print(nam)
      nam<-strsplit(nam,split='_')
      #whiwprint(nam[[1]])
      
      temp<-data.frame(paste(nam[[1]][1],nam[[1]][2],sep='_'),as.integer(nam[[1]][3]),log(fold,2))
      new_table<-rbind(new_table,temp)
      
      
    }
  }
  
  return(new_table)
}



RJG_RomanNumeralSort<-function(x)
{
  
  #rom_num<-c('Supercontig_1.1','Supercontig_1.2','Supercontig_1.3','Supercontig_1.4','Supercontig_1.5','Supercontig_1.6','Supercontig_1.7','Supercontig_1.8','Supercontig_1.9','Supercontig_1.10',
             #'Supercontig_1.11','Supercontig_1.12','Supercontig_1.13','Supercontig_1.14','Supercontig_1.15','Supercontig_1.16','Supercontig_1.17')
  
  rom_num<-c('Supercontig_1.17','Supercontig_1.6','Supercontig_1.15','Supercontig_1.1','Supercontig_1.11'
             ,'Supercontig_1.16','Supercontig_1.2','Supercontig_1.12','Supercontig_1.14'
             ,'Supercontig_1.8','Supercontig_1.9','Supercontig_1.10','Supercontig_1.5'
             ,'Supercontig_1.7','Supercontig_1.3','Supercontig_1.4')
  new_table<-c()
  i=0
  for(i in 1:length(rom_num))
  {
    nam<-rom_num[i]
    print(nam)
    temp<-x[which(x[,1]==nam),]
    
    #new_temp<-c()
    
    
    new_table<-rbind(new_table,temp)
    
    
    
  }
  
  add<-c()
  for(j in 1:nrow(new_table))
  {
    add<-append(add,j)
    
    
  }
  
  print(add)
  new_table<-cbind(new_table,add)
  return(new_table)
  
}

categorize_plot<-function(x)
{
  x<-x[,1]
  print(length(x))
  cats<-c()
  for(i in 1:length(x))
  {
    if(i==1)
    {
      contig=x[i]
      category<-1 
      cats<-append(cats,category)
    }
    else
    {
      new_contig=x[i]
      if(new_contig!=contig)
      {
        contig=new_contig
        if(category==1)
        {
          category=2
          cats<-append(cats,category)
        }
        else 
        {
          
          category=1
          cats<-append(cats,category)
        }
      }
      else
      {
        cats<-append(cats,category)
        
        
        
      }
      
      
      
    }
    
    
    
    
  }
  
  
  
  return(cats)
  
  
}

library(ggplot2)
#load('2014-07-12.RData')
#setwd('')
load('../reads/matched/euploid_panel/euploid_panel.RData')
z<-euploid_model



w<-read.table('../reads/matched/38RL1/38RL1.marker.complete',header=F)
w<-change_row_names(w)
s<-RJG_logFoldDifference(z,w)
s<-RJG_RomanNumeralSort(s)
q<-s
v<-categorize_plot(q)
q<-cbind(q,v)

#a<-ggplot(q,aes(x=q[,4],y=q[,3]))+geom_point(shape=1,aes(color=factor(q[,1])),size=3)+scale_color_discrete(direction=1,h=0:600)+xlab("Ignore_Abritrary Postitions for Plotting")+ylab('Log2-Fold Difference Compared to Euploud Panel')+opts(title='JR30')+ylim(-1,2)
a<-ggplot(q,aes(x=q[,4],y=q[,3]))+geom_point(shape=1,aes(color=factor(q[,5])),size=3)+xlab("Chromosome")+ylab('Log2-Fold Difference Compared to Euploud Panel')+opts(title='38RL1X15211C')+ylim(-1,2)+scale_colour_manual(values = c( "#0072B2","#D55E00"))+guides(fill=FALSE)
print(a)