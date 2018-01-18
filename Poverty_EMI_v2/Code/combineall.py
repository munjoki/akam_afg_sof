import inspect,os,csv,sys
from afgbranch import afgbranch
from datetime import datetime
from findintime import findinperiod
from productdecode import *

def combineall(nyear,nqrt):

	fdir=os.getcwd()+"/Data/"
	
	print "   Loading file"
	fop=open(fdir+"/Open_Loans_"+nyear+"_Q"+str(nqrt)+".csv","rU")
	frop=csv.reader(fop,delimiter=",")
	fdop=list(frop)
	print "   File loaded"
	
	print "   Loading file"
	fcl=open(fdir+"/Closed_Loans_"+nyear+"_Q"+str(nqrt)+".csv","rU")
	frcl=csv.reader(fcl,delimiter=",")
	fdcl=list(frcl)
	print "   File loaded"
	
	fout=open(fdir+"/All_Loans_"+nyear+"_Q"+str(nqrt)+".csv","wb")
	print "   Writing file to ",fdir

	csv.writer(fout).writerow(fdop[0])
	
	nclients=0
	for row in range(1,len(fdop)):
		if row%10000==0: print "         Searched ",row," of ",len(fdop)-1," clients..."
		
		if fdop[row][3]!="": branch=afgbranch(float(fdop[row][3]))
		else: branch=""
		
		if fdop[row][4]!="" and fdop[row][5]!="": 
			prod=productname(float(fdop[row][4]),float(fdop[row][5]))
			purp=productpurpose(float(fdop[row][4]),float(fdop[row][5]))
		else: 
			prod=""
			purp=""
		
		fout.write(fdop[row][0]+","+fdop[row][1]+","+fdop[row][2]+","+fdop[row][3]+","+branch+","+prod+","+purp+","
			+fdop[row][20]+","+fdop[row][6]+","+fdop[row][7]+",,"+fdop[row][8]+","+fdop[row][9]+","
			+fdop[row][10]+",,"+fdop[row][12]+","+fdop[row][15]+","+fdop[row][16]+"\n")
		
	print "      Finished finding records from ",nyear," for open loans!"
	
	print "      Now the closed loans"
	

	for sow in range(1,len(fdcl)):
		if sow%1000==0: print "         Searched ",sow," of ",len(fdcl)-1," clients..."
	
		if fdcl[sow][6]!="": purpc=productnamepurpose(fdcl[sow][6])
		else: purpc=""
		
		fout.write(fdcl[sow][0]+","+fdcl[sow][1]+",,"+fdcl[sow][3]+","+fdcl[sow][2]+","+fdcl[sow][6]+","+purpc+","
			+fdcl[sow][23]+","+fdcl[sow][7]+","+fdcl[sow][8]+","+fdcl[sow][9]+","+fdcl[sow][10]+","+fdcl[sow][11]+","
			+fdcl[sow][12]+","+fdcl[sow][13]+","+fdcl[sow][15]+","+fdcl[sow][18]+","+fdcl[sow][19]+"\n")

	print "      Finished finding records from ",nyear," for open loans!"