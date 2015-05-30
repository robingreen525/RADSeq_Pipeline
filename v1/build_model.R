
load('euploid_panel.RData')
cv<-function(x) sd(x)/mean(x)
euploid<-euploid[,-1] # remove column with length of reads (already filtered based on size)
m<-apply(euploid,1,mean)
c<-apply(euploid,1,cv)


euploid_model<-cbind(euploid,m,c)
euploid_model<-euploid_model[which(euploid_model[,12]<0.15),]
save.image('euploid_panel.RData')