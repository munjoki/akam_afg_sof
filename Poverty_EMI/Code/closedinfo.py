import inspect,os,csv,sys
from afgbranch import afgbranch
from productdecode import *

def closedinfo(nfile):

	fdir=os.getcwd()+"/Data/"
	
	print "   Loading file"
	fin=open(fdir+"/"+nfile+".csv","rU")
	frin=csv.reader(fin,delimiter=",")
	fdin=list(frin)
	print "   File loaded"

	fout=open(fdir+"/Poverty_EMI_closed.csv","wb")
	print "   Writing file to ",fdir


	fout.write("CUSTOMER_CODE,BRANCH_CODE,BRANCH,GENDER,AGE,"
			   +"LOAN_APPROVE_1,LOAN_CLOSED_1,PROD_1,PURP_1,CYCLE_1,DURATION_1,CURR_1,AMOUNT_1,INST_AFA_1,"
			   +"LOAN_APPROVE_2,LOAN_CLOSED_2,PROD_2,PURP_2,CYCLE_2,DURATION_2,CURR_2,AMOUNT_2,INST_AFA_2,"
			   +"LOAN_APPROVE_3,LOAN_CLOSED_3,PROD_3,PURP_2,CYCLE_2,DURATION_2,CURR_2,AMOUNT_2,INST_AFA_2,"
			   +"NET_USD,GROSS_USD,NET_PER_DIEM_USD,GROSS_PER_DIEM_USD\n")

	mtch=0
	for row in range(1,len(fdin)):
	
		if row%1000==0: print "      Searched ",row," of ",len(fdppi)-1," clients..."
		
		#skip second entry for client as already written out
		if mtch==1:
			mtch=0
			continue
		#filter out SME clients
		if int(fdin[row][4])==3: continue 
		
		if float(fdin[row][3])!="": branch=afgbranch(float(fdin[row][3]))
		else: branch=""
		prod1=productname(float(fdin[row][4]),float(fdin[row][5]))
		purp1=productpurpose(float(fdin[row][4]),float(fdin[row][5]))
		
		fout.write(fdin[row][0]+","+fdin[row][3]+","+branch+","+fdin[row][1]+","+fdin[row][2]+","
			+fdin[row][6]+","+fdin[row][7]+","+prod1+","+purp1+","+fdin[row][20]+","+fdin[row][8]+","+fdin[row][9]+","+fdin[row][10]+","+fdin[row][12]+",")
			
		if len(fdin)>row+1 and fdin[row][0]==fdin[row+1][0]: 
			totnet=float(fdin[row][15])+float(fdin[row+1][15])
			totgross=float(fdin[row][16])+float(fdin[row+1][16])
			pdnet=float(fdin[row][17])+float(fdin[row+1][17])
			pdgross=float(fdin[row][18])+float(fdin[row+1][18])
			
			prod2=productname(float(fdin[row+1][4]),float(fdin[row+1][5]))
			purp2=productpurpose(float(fdin[row+1][4]),float(fdin[row+1][5]))
			fout.write(fdin[row+1][6]+","+fdin[row+1][7]+","+prod2+","+purp2+","+fdin[row][20]+","+fdin[row+1][8]+","+fdin[row+1][9]+","+fdin[row+1][10]+","+fdin[row+1][12]+","
				+totnet+","+totgross+","+pdnet+","+pdgross+"\n")
			mtch=1
		else:
			fout.write(",,,,,,,,,"
				+fdin[row][15]+","+fdin[row][16]+","+fdin[row][17]+","+fdin[row][18]+"\n")
		
		  
	
	print "   Finished calculating poverty levels for records from ",nyear," for ",len(fdin)-1," clients!"
	fout.close()
	fin.close()