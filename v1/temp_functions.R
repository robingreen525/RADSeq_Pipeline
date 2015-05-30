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