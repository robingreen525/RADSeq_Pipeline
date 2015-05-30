

#the purpose of this script is to generate RADSeq plots for each sample. For each marker, proporition of coverage will be
# compared against the euploid panel. The euploid panel markers will be filtered by CV of proprotion across all 10 strains in 
# the panel

# take strain from command line and use it to make RADSeq plot
args <- commandArgs(TRUE)
strain<-args[1]
print(strain)
path<-args[2]

dir=paste(path,strain,sep='/') # where the strain of interest is
print(dir)
file=paste(strain,'markers.complete',sep='.') # the strain.markers.complete file
print(file)
full=paste(dir,file,sep='/')
print(full)
final=paste(strain,'RADSeq.pdf',sep='_')
full_final<-paste(dir,final,sep='/') # the final PDF file of the saved plots

require(ggplot2)

# get euploid panel data
load('/fh/fast/shou_w/NextGenSeq/RadSeq/Euploid_Panel/reads/20150528_euploid.RData')

# get markers below desired CV threshold (15% is ~5000 markers, 10% is ~1300)
panel<-euploid_pass[which(euploid_pass$cv<=15),]

#get data of strain being compared to euploid panel
r<-read.table(full,header=F)






colnames(r)<-c('Supercontig','Pos','length','reads','prop')
site<-paste(r$Supercontig,r$Pos,sep='_')
r<-cbind(r,site)

#only focus on the sites in your sample that have been filtered by CV from the euploid panel
a<-r[which(r$site %in% panel$site),]

# get the relative increase/decrease in proportion of coverage for the sample vs. the euploid panel for each site

panel_prop<-data.frame()
for(i in 1:nrow(a)) # for each marker in sample
{
	marker<-as.character(a$site[i])
	j<-which(panel$site==marker)
	#print(marker)
	temp<-panel[j,] # get the corresponding information from the euploid panel
	#print(temp$avg)
	panel_prop<-rbind(panel_prop,as.numeric(temp$avg)) #save the proportion of coverage from the euploid panel for that marker

}

colnames(panel_prop)<-c('panel_prop')
a<-cbind(a,panel_prop)
log_fold<-log((a$prop/a$panel_prop),2)
a<-cbind(a,log_fold)

# sort the information by chromosome and position for plotting
chrom_conv<-list('Supercontig_1.1'=4,'Supercontig_1.2'=7,'Supercontig_1.3'=15,
                 'Supercontig_1.4'=16,'Supercontig_1.5'=8,'Supercontig_1.6'=2,
                 'Supercontig_1.7'=14,'Supercontig_1.8'=10,'Supercontig_1.9'=11,
                 'Supercontig_1.10'=12.1,'Supercontig_1.11'=5,'Supercontig_1.12'=8,
               'Supercontig_1.13'=12.2,'Supercontig_1.14'=9,'Supercontig_1.15'=3,
                 'Supercontig_1.16'=6,'Supercontig_1.17'=1,
                 'XII'='XII')

loss=0
chr<-data.frame()
for(i in 1:nrow(a))
{
	contig=as.character(a$Supercontig[i])
	ch=as.numeric((chrom_conv[contig]))
	chr<-rbind(chr,ch)
	



}       

colnames(chr)<-c('chr')
# sort the markers first by chromosome, then by position along each chromosome
a<-cbind(a,chr)
a<-a[order(chr,a$Pos),]

#add an arbitrary column for making plotting order
plot_x<-data.frame()
for(i in 1:nrow(a))
{
	plot_x<-rbind(plot_x,i)

}


colnames(plot_x)<-c('plot_x')
a<-cbind(a,plot_x)


b<-ggplot(a,aes(x=plot_x,y=log_fold))+geom_point(shape=1,aes(color=factor(chr)),size=3)+xlab("Chromosome")+ylab('Log2-Fold Difference Compared to Euploud Panel')+ylim(-1,2)+scale_colour_manual(values = c( "#0072B2","#D55E00","#0072B2","#D55E00","#0072B2","#D55E00","#0072B2","#D55E00","#0072B2","#D55E00","#0072B2","#D55E00","#0072B2","#D55E00","#0072B2","#D55E00"))+guides(fill=FALSE)
ggsave(b,file=full_final)
