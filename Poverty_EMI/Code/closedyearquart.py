import inspect,os,csv,sys
from afgbranch import afgbranch
from datetime import datetime
from findintime import findinperiod
from productdecode import *

def closedyearquart(nyear,nqrt,fname):

	fdir=os.getcwd()+"/Data/"
	
	print "   Loading file"
	fin=open(fdir+"/"+fname+".csv","rU")
	frin=csv.reader(fin,delimiter=",")
	fdin=list(frin)
	print "   File loaded"

	fout=open(fdir+"/Closed_Q"+str(nqrt)+"_"+nyear+".csv","wb")
	print "   Writing file to ",fdir

	if nqrt==0:
		bqrt="1/1/"+nyear
		eqrt="12/31/"+nyear
		sdate=datetime.strptime(bqrt,"%m/%d/%Y")
		edate=datetime.strptime(eqrt,"%m/%d/%Y")
	elif nqrt==1:
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
		print "No quarter selected, so using default of all year"
		bqrt="1/1/"+nyear
		eqrt="12/31/"+nyear
		sdate=datetime.strptime(bqrt,"%m/%d/%Y")
		edate=datetime.strptime(eqrt,"%m/%d/%Y")
	
	csv.writer(fout).writerow(fdin[0])

	nclients=0
	for row in range(1,len(fdin)):
	
		if row%1000==0: print "      Searched ",row," of ",len(fdin)-1," clients..."
		
		pdate=datetime.strptime(fdin[row][7],"%m/%d/%Y")
		cdate=datetime.strptime(fdin[row][23],"%m/%d/%Y")
		intime=findinperiod(sdate,edate,pdate)
		outtime=findinperiod(sdate,edate,cdate)
		
		if intime!=1 or cdate<sdate: continue
		
		csv.writer(fout).writerow(fdin[row])
		nclients+=1
	
	print "   Finished finding ",nclients," out of ",len(fdin)-1," clients with records in Q",nqrt," of ",nyear
	fin.close()
	fout.close()