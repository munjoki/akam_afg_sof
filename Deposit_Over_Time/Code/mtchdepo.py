import inspect,os,csv,sys
from datetime import datetime

def mtchdepo(nyear,oyear,nqrt):
	
	frdir=os.getcwd()
	fdir=os.getcwd()+"/Data/"
	print "   Loading file from ",nyear
	fnew=open(frdir+"/DepositInfo"+nqrt+nyear+".csv","rU")
	frnew=csv.reader(fnew,delimiter=",")
	fdnew=list(frnew)
	print "   File loaded"

	print "   Loading file from ",oyear
	fold=open(frdir+"/DepositInfo"+nqrt+nyear+".csv","rU")
	frold=csv.reader(fold,delimiter=",")
	fdold=list(frold)
	print "   File loaded"

	fout=open(fdir+"/Demand_Compare_"+nqrt+"_"+nyear+"_to_"+oyear+"_2.csv","wb")
	print "   Writing file to ",fdir

	#csv.writer(fout).writerow(fdnew[0])
	fout.write("CUST_CODE,PROD_CODE,PROD,OPEN_DATE,BRANCH,GEO_LOC,PROVINCE,GENDER,LAST_TRANS_DATE,"
		+"CURR_"+nyear+",BAL_AFN_"+nyear+",CURR_"+oyear+",BAL_AFN_"+oyear+",BAL_DIFF\n")

	nclients=0
	plce=0
	mtch=0
	
	for row in range(1,len(fdnew)):
		if row%1000==0: print "         Searched ",row," of ",len(fdnew)-1," clients..."
		
		if fdnew[row][2]!="Demand": continue
		
		for sow in range(plce,len(fdold)):
		
			if fdnew[row][0]==fdold[sow][0] and fdnew[row][2]==fdold[sow][2] and mtch!=1: 
				mtch=1
				plce=sow
				
				if "-" in fdnew[row][5] or fdnew[row][5]=="": balnew=0.0
				else: balnew=float(fdnew[row][5])
				
				if "-" in fdold[sow][5] or fdold[sow][5]=="": balold=0.0
				else: balold=float(fdold[sow][5])
				
				baldiff=balnew-balold
				
				fout.write(fdnew[row][0]+","+fdnew[row][1]+","+fdnew[row][2]+","+fdnew[row][3]+","
					+fdnew[row][6]+","+fdnew[row][11]+","+fdnew[row][12]+","+fdnew[row][10]+","
					+fdnew[row][9]+","+fdnew[row][4]+","+fdnew[row][5]+","
					+fdold[sow][4]+","+fdold[sow][5]+","+str(baldiff)+"\n")
					
		mtch=0
		
	fout.close()
	fnew.close()
	fold.close()
	