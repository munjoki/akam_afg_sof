import inspect,os,csv,sys

mydir="C:\Data\julia.gray\Documents\SPI_Tool_Afg\PPI_Score_Analysis"
os.chdir(mydir)
fdir=os.getcwd()+"/Data/"
sdir=os.getcwd()+"/Code/"
sys.path.append(sdir)

from compcust import compcust 

fother="2017"

#fin=open(fdir+"/missingguys1.csv","rU")
fin=open(fdir+"/PPI_Compare_2016_to_2017_Match_Loan_Match_Loan_Final_Final_31days.csv","rU")
frin=csv.reader(fin,delimiter=",")
fdin=list(frin)

#if fother.lower()=="open": flf=open(os.getcwd()+"/Loan_Portfolio_as_of_Jun_2017.csv","rU")
#if fother.lower()=="closed": flf=open(os.getcwd()+"/Closed_Loans_Since_2010.csv","rU")
flf=open(fdir+"/Poverty_Likelihood_2017_Match_Loan.csv","rU")
frlf=csv.reader(flf,delimiter=",")
fdlf=list(frlf)

fout=open(fdir+"/Pov2017_Loans_Check_"+fother+".csv","wb")

csv.writer(fout).writerow(fdin[0]+fdlf[0])

mtch=0
plce=1
print "Hello, I'm starting"
for row in range(1,len(fdin)):
	
	if row%100==0: print "         Searched ",row," of ",len(fdin)-1," clients..."

	mtch=0
	
	for sow in range(plce,len(fdlf)):
		#if fother.lower()=="open": mtch=compcust(float(fdin[row][0]),float(fdlf[sow][0]))
		#if fother.lower()=="closed": mtch=compcust(float(fdin[row][0]),float(fdlf[sow][3]))
		mtch=compcust(float(fdin[row][0]),float(fdlf[sow][0]))
		if mtch==1: 
			csv.writer(fout).writerow(fdin[row]+fdlf[sow])
			plce=sow
	
fin.close()
flf.close()
fout.close()