import inspect,os,csv,sys
from findintime import findinperiod
from datetime import datetime

def povertyquarterly(nyear,nqrt):

	fdir=os.getcwd()+"/Data/"
	
	fin=open(fdir+"/Poverty_Likelihood_"+nyear+"_Match_Loan.csv","rU")
	frin=csv.reader(fin,delimiter=",")
	fdin=list(frin)
	
	fout=open(fdir+"/Poverty_Likelihood_"+nyear+"_Match_Loan_Q"+str(nqrt)+".csv","wb")
	
	csv.writer(fout).writerow(fdin[0])
	
	print "      Searching ",len(fdin)-1," clients for records in Q",nqrt," of ",nyear
	
	if nqrt==1:
		bqrt="1/1/"+nyear
		eqrt="3/31/"+nyear
		sdate=datetime.strptime(bqrt,"%m/%d/%Y")
		edate=datetime.strptime(eqrt,"%m/%d/%Y")
	elif nqrt==2:
		bqrt="4/1/"+nyear
		eqrt="6/30/"+nyear
		sdate=datetime.strptime(bqrt,"%m/%d/%Y")
		edate=datetime.strptime(eqrt,"%m/%d/%Y")
	elif nqrt==3:
		bqrt="7/1/"+nyear
		eqrt="9/30/"+nyear
		sdate=datetime.strptime(bqrt,"%m/%d/%Y")
		edate=datetime.strptime(eqrt,"%m/%d/%Y")
	elif nqrt==4:
		bqrt="10/1/"+nyear
		eqrt="12/31/"+nyear
		sdate=datetime.strptime(bqrt,"%m/%d/%Y")
		edate=datetime.strptime(eqrt,"%m/%d/%Y")
	else: 
		print "No quarter selected, so using default of first quarter"
		bqrt="1/1/"+nyear
		eqrt="3/31/"+nyear
		sdate=datetime.strptime(bqrt,"%m/%d/%Y")
		edate=datetime.strptime(eqrt,"%m/%d/%Y")
	
	nclients=0
	
	for row in range(1,len(fdin)):
	
		if row%1000==0: print "      Searched ",row," of ",len(fdin)-1," clients..."
		
		pdate=datetime.strptime(fdin[row][10],"%m/%d/%Y")
		intime=findinperiod(sdate,edate,pdate)
		
		if intime!=1: continue
		
		csv.writer(fout).writerow(fdin[row])
		nclients+=1
	
	print "   Finished finding ",nclients," out of ",len(fdin)-1," clients with records in Q",nqrt," of ",nyear
	fin.close()
	fout.close()