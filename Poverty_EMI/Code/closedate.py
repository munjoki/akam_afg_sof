import inspect,os,csv,sys
from datetime import datetime
from findintime import findinrange

def closedate(fname):

	fdir=os.getcwd()+"/Data/"
	
	print "   Loading file without closed date"
	fin=open(os.getcwd()+"/missing_check_find.csv","rU")
	frin=csv.reader(fin,delimiter=",")
	fdin=list(frin)
	print "   File loaded"

	print "   Loading file with closed date"
	fdat=open(os.getcwd()+"/Closed_Loans_Since_2010.csv","rU")
	frdat=csv.reader(fdat,delimiter=",")
	fddat=list(frdat)
	print "   File loaded"
	
	fout=open(fdir+"/Closed_Loans_Closed_Date_missing.csv","wb")
	print "   Writing file to ",fdir
	
	csv.writer(fout).writerow(fdin[0]+["Closed_Date"])
	
	plce=1
	mtch=0
	nclients=0
	for row in range(1,len(fdin)):
	
		if row%1000==0: print "      Searched ",row," of ",len(fdin)-1," clients..."
		
		for sow in range(plce,len(fddat)):
		
			if float(fdin[row][0])<float(fddat[sow][3]): break
			if mtch!=1:
				cloan=datetime.strptime(fdin[row][7],"%m/%d/%Y")
				dloan=datetime.strptime(fddat[sow][6],"%m/%d/%Y")
				if float(fdin[row][0])==float(fddat[sow][3]) and findinrange(cloan,dloan,31)==1:
					mtch=1
					plce=sow 
					nclients+=1
					csv.writer(fout).writerow(fdin[row]+[fddat[sow][5]])
		
		if mtch!=1: csv.writer(fout).writerow(fdin[row]+[""])
		mtch=0
	print nclients," out of ",len(fdin)-1