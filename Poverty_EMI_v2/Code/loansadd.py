import inspect,os,csv,sys
from findintime import findinperiod
from openclosed import *
from datetime import datetime
from compcust import compcust
from finddups import loandups

def loansadd(nyear,oyear,fname,fadd,ftype):

	fdir=os.getcwd()+"/Data/"

	print "      Loading PPI file with scores from ",nyear," matched to those of ",oyear," already matched to loans"
	fin=open(fdir+"/PPI_Compare_"+oyear+"_to_"+nyear+"_Match_Loan_Match_Loan"+fadd+".csv","rU")
	frin=csv.reader(fin,delimiter=",")
	fdin=list(frin)

	print "      Loading file with all ",ftype," loans on record"
	floan=open(os.getcwd()+"/"+fname+".csv","rU")
	frloan=csv.reader(floan,delimiter=",")
	fdloan=list(frloan)

	fout=open(fdir+"/PPI_Compare_"+oyear+"_to_"+nyear+"_Match_Loan_Match_Loan"+fadd+"_Final.csv","wb")

	if ftype.lower()=="open": csv.writer(fout).writerow(fdin[0]+["LOAN_DISB_1","LOAN_CLOSED_1","PROD_1","PURP_1","LOAN_DISB_2","LOAN_CLOSED_2","PROD_2","PURP_2","LOAN_DISB_3","LOAN_CLOSED_3","PROD_3","PURP_3"])
	if ftype.lower()=="closed": csv.writer(fout).writerow(fdin[0]+["LOAN_DISB_4","LOAN_CLOSED_4","PROD_4","PURP_4","LOAN_DISB_5","LOAN_CLOSED_5","PROD_5","PURP_5","LOAN_DISB_6","LOAN_CLOSED_6","PROD_6","PURP_6"])
	plce=1
	mtch=0
	nclients=0
    
	print "      Searching ",len(fdin)-1," clients for any additional ",ftype," loans"

	for row in range(1,len(fdin)):
		if row%1000==0: print "         Searched ",row," of ",len(fdin)-1," clients..."
		for sow in range(plce,len(fdloan)):
			if mtch!=1:
				if ftype.lower()=="open": mtch=compcust(fdin[row][0],fdloan[sow][0])
				if ftype.lower()=="closed": mtch=compcust(fdin[row][0],fdloan[sow][3])
				
				if mtch==1:
					plce=sow
					nwrit=0
					if ftype.lower()=="open": ldate=datetime.strptime(fdloan[sow][2],"%m/%d/%y")
					if ftype.lower()=="closed": ldate=datetime.strptime(fdloan[sow][5],"%m/%d/%y")
					sdate=datetime.strptime(fdin[row][12],"%m/%d/%y")
					edate=datetime.strptime(fdin[row][10],"%m/%d/%y")
					
					intime=findinperiod(sdate,edate,ldate)
					
					if ftype.lower()=="open": nlpurp=productnamepurpose(fdloan[sow][6])
					if ftype.lower()=="closed": nlpurp=productpurpose(float(fdloan[sow][0]),float(fdloan[sow][1]))
					if compcust(sdate,ldate)==1 and compcust(fdin[row][22],nlpurp)==1: 
						mtch=0
						continue
					if compcust(edate,ldate)==1 and compcust(fdin[row][18],nlpurp)==1: 
						mtch=0
						continue

					if intime==1:
						if ftype.lower()=="open": ndups=loandups(sow,0,fdloan,2)
						if ftype.lower()=="closed": ndups=loandups(sow,3,fdloan,2)

						wrt1=0
						wrt2=0
						wrt3=0
						
						if ftype.lower()=="open":
							nldate1=datetime.strptime(fdloan[sow][2],"%m/%d/%y")
							purp1=productnamepurpose(fdloan[sow][6])
							if findinperiod(sdate,edate,nldate1)!=1: wrt1=1
							if compcust(edate,nldate1)==1 and compcust(fdin[row][18],purp1)==1: wrt1=1
							if ndups==0: 
								if wrt1!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][2],fdloan[sow][3],fdloan[sow][6],purp1,"","","","","","","",""])
								else: csv.writer(fout).writerow(fdin[row]+["","","","","","","","","","","","","","","","","","","",""])
							if ndups==1:
								nldate2=datetime.strptime(fdloan[sow+1][2],"%m/%d/%y")
								purp2=productnamepurpose(fdloan[sow+1][6])
								if findinperiod(sdate,edate,nldate2)!=1: wrt2=1
								if compcust(edate,nldate2)==1 and compcust(fdin[row][18],purp2)==1: wrt2=1
								if wrt1!=1 and wrt2!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][2],fdloan[sow][3],fdloan[sow][6],purp1,fdloan[sow+1][2],fdloan[sow+1][3],fdloan[sow+1][6],purp2,"","","",""])
								elif wrt1!=1 and wrt2==1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][2],fdloan[sow][3],fdloan[sow][6],purp1,"","","","","","","",""])
								elif wrt1==1 and wrt2!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow+1][2],fdloan[sow+1][3],fdloan[sow+1][6],purp2,"","","","","","","",""])
								else: csv.writer(fout).writerow(fdin[row]+["","","","","","","","","","","","","","","","","","","",""])
								plce=sow+1
							if ndups==2:
								nldate2=datetime.strptime(fdloan[sow+1][2],"%m/%d/%y")
								purp2=productnamepurpose(fdloan[sow+1][6])
								nldate3=datetime.strptime(fdloan[sow+2][2],"%m/%d/%y")
								purp3=productnamepurpose(fdloan[sow+2][6])
								if findinperiod(sdate,edate,nldate2)!=1: wrt2=1
								if compcust(edate,nldate2)==1 and compcust(fdin[row][18],purp2)==1: wrt2=1
								if findinperiod(sdate,edate,nldate3)!=1: wrt3=1
								if compcust(edate,nldate3)==1 and compcust(fdin[row][18],purp3)==1: wrt3=1
								if wrt1!=1 and wrt2!=1 and wrt3!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][2],fdloan[sow][3],fdloan[sow][6],purp1,fdloan[sow+1][2],fdloan[sow+1][3],fdloan[sow+1][6],purp2,fdloan[sow+2][2],fdloan[sow+2][3],fdloan[sow+2][6],purp3])
								elif wrt1!=1 and wrt2!=1 and wrt3==1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][2],fdloan[sow][3],fdloan[sow][6],purp1,fdloan[sow+1][2],fdloan[sow+1][3],fdloan[sow+1][6],purp2,"","","",""])
								elif wrt1!=1 and wrt2==1 and wrt3!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][2],fdloan[sow][3],fdloan[sow][6],purp1,fdloan[sow+2][2],fdloan[sow+2][3],fdloan[sow+2][6],purp3,"","","",""])
								elif wrt1==1 and wrt2!=1 and wrt3!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow+1][2],fdloan[sow+1][3],fdloan[sow+1][6],purp2,fdloan[sow+2][2],fdloan[sow+2][3],fdloan[sow+2][6],purp3,"","","",""])
								elif wrt1!=1 and wrt2==1 and wrt3==1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][2],fdloan[sow][3],fdloan[sow][6],purp1,"","","","","","","",""])
								elif wrt1==1 and wrt2!=1 and wrt3==1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow+1][2],fdloan[sow+1][3],fdloan[sow+1][6],purp2,"","","","","","","",""])
								elif wrt1==1 and wrt2==1 and wrt3!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow+2][2],fdloan[sow+2][3],fdloan[sow+2][6],purp3,"","","","","","","",""])
								else: csv.writer(fout).writerow(fdin[row]+["","","","","","","","","","","","","","","","","","","",""])
								plce=sow+2
						if ftype.lower()=="closed":
							nldate1=datetime.strptime(fdloan[sow][5],"%m/%d/%y")
							prod1=productname(float(fdloan[sow][0]),float(fdloan[sow][1]))
							purp1=productpurpose(float(fdloan[sow][0]),float(fdloan[sow][1]))
							if findinperiod(sdate,edate,nldate1)!=1: wrt1=1
							if compcust(edate,nldate1)==1 and compcust(fdin[row][18],purp1)==1: wrt1=1
							if ndups==0: 
								if wrt1!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][6],fdloan[sow][5],prod1,purp1,"","","","","","","",""])
								else: csv.writer(fout).writerow(fdin[row]+["","","","","","","","","","","","","","","","","","","",""])
							if ndups==1:
								nldate2=datetime.strptime(fdloan[sow+1][5],"%m/%d/%y")
								prod2=productname(float(fdloan[sow+1][0]),float(fdloan[sow+1][1]))
								purp2=productpurpose(float(fdloan[sow+1][0]),float(fdloan[sow+1][1]))
								if findinperiod(sdate,edate,nldate2)!=1: wrt2=1
								if compcust(edate,nldate2)==1 and compcust(fdin[row][18],purp2)==1: wrt2=1
								if wrt1!=1 and wrt2!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][6],fdloan[sow][5],prod1,purp1,fdloan[sow+1][6],fdloan[sow+1][5],prod2,purp2,"","","",""])
								elif wrt1!=1 and wrt2==1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][6],fdloan[sow][5],prod1,purp1,"","","","","","","",""])
								elif wrt1==1 and wrt2!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow+1][6],fdloan[sow+1][5],prod1,purp1,"","","","","","","",""])
								else: csv.writer(fout).writerow(fdin[row]+["","","","","","","","","","","","","","","","","","","",""])
								plce=sow+1
							if ndups==2:
								nldate2=datetime.strptime(fdloan[sow+1][5],"%m/%d/%y")
								prod2=productname(float(fdloan[sow+1][0]),float(fdloan[sow+1][1]))
								purp2=productpurpose(float(fdloan[sow+1][0]),float(fdloan[sow+1][1]))
								nldate3=datetime.strptime(fdloan[sow+2][5],"%m/%d/%y")
								prod3=productname(float(fdloan[sow+2][0]),float(fdloan[sow+2][1]))
								purp3=productpurpose(float(fdloan[sow+2][0]),float(fdloan[sow+2][1]))
								if findinperiod(sdate,edate,nldate2)!=1: wrt2=1
								if compcust(edate,nldate2)==1 and compcust(fdin[row][18],purp2)==1: wrt2=1
								if findinperiod(sdate,edate,nldate3)!=1: wrt3=1
								if compcust(edate,nldate3)==1 and compcust(fdin[row][18],purp3)==1: wrt3=1
								if wrt1!=1 and wrt2!=1 and wrt3!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][6],fdloan[sow][5],prod1,purp1,fdloan[sow+1][6],fdloan[sow+1][5],prod2,purp2,fdloan[sow+2][6],fdloan[sow+2][5],prod3,purp3])
								elif wrt1!=1 and wrt2!=1 and wrt3==1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][6],fdloan[sow][5],prod1,purp1,fdloan[sow+1][6],fdloan[sow+1][5],prod2,purp2,"","","",""])
								elif wrt1!=1 and wrt2==1 and wrt3!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][6],fdloan[sow][5],prod1,purp1,fdloan[sow+2][6],fdloan[sow+2][5],prod3,purp3,"","","",""])
								elif wrt1==1 and wrt2!=1 and wrt3!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow+1][6],fdloan[sow+1][5],prod2,purp2,fdloan[sow+2][6],fdloan[sow+2][5],prod3,purp3,"","","",""])
								elif wrt1!=1 and wrt2==1 and wrt3==1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow][6],fdloan[sow][5],prod1,purp1,"","","","","","","",""])
								elif wrt1==1 and wrt2!=1 and wrt3==1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow+1][6],fdloan[sow+1][5],prod2,purp2,"","","","","","","",""])
								elif wrt1==1 and wrt2==1 and wrt3!=1: csv.writer(fout).writerow(fdin[row]+[fdloan[sow+2][6],fdloan[sow+2][5],prod3,purp3,"","","","","","","",""])
								else: csv.writer(fout).writerow(fdin[row]+["","","","","","","","","","","","","","","","","","","",""])
								plce=sow+2
					else: 
						mtch=0
						
		if mtch==1: nclients+=1
		if mtch!=1:
			csv.writer(fout).writerow(fdin[row]+["","","","","","","","","","","",""])

		mtch=0     
	print "   Finished finding all other loan records from ",oyear," to ",nyear," with ",nclients," out of ",len(fdin)-1," clients with PPI records"
	fin.close()
	floan.close()
	fout.close()
