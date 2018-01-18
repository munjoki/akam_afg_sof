import inspect,os,csv,sys
from findintime import findinperiod
from datetime import datetime

def loanquarterly(tloan,nyear,nqrt):

	fdir=os.getcwd()+"/Data/"
	
	fin=open(fdir+"/"+tloan+"_Loans_"+nyear+".csv","rU")
	frin=csv.reader(fin,delimiter=",")
	fdin=list(frin)
	
	fout=open(fdir+"/"+tloan+"_Loans_"+nyear+"_Q"+str(nqrt)+".csv","wb")
	
	fout.write("Cust_Code,Gender,Age,Branch_Code,Branch,Product,Purpose,Loan_Cycle,Approve_Date,Maturity_Date,Closed_Date,"
		"Duration,Currency,Amount,Markup,Installment_AFA,Net_Income_USD,Gross_Income_USD\n")
	
	print "      Searching ",len(fdin)-1," clients for PPI records in Q",nqrt," of ",nyear
	
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
		
		if tloan.lower()=="open": pdate=datetime.strptime(fdin[row][6],"%m/%d/%Y")
		if tloan.lower()=="closed": pdate=datetime.strptime(fdin[row][7],"%m/%d/%Y")
		intime=findinperiod(sdate,edate,pdate)
		
		if intime!=1: continue
		
		csv.writer(fout).writerow(fdin[row])
		nclients+=1
	
	print "   Finished finding ",nclients," out of ",len(fdin)-1," clients with PPI records in Q",nqrt," of ",nyear
	fin.close()
	fout.close()