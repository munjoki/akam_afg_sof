import inspect,os,csv,sys
from datetime import datetime
from findintime import *
from afgbranch import afgbranch
from productdecode import *

def incomecomp(nyear,oyear,nqrt):

	fdir=os.getcwd()+"/Data/"
	
	print "   Loading file from ",nyear
	fnew=open(fdir+"/All_Income_"+nyear+"_Q"+str(nqrt)+".csv","rU")
	frnew=csv.reader(fnew,delimiter=",")
	fdnew=list(frnew)
	print "   File loaded"
	
	print "   Loading file from ",oyear
	fold=open(fdir+"/All_Income_"+oyear+".csv","rU")
	frold=csv.reader(fold,delimiter=",")
	fdold=list(frold)
	print "   File loaded"
	
	fout=open(fdir+"/All_Income_Compare_"+oyear+"_to_"+nyear+"_Q"+str(nqrt)+".csv","wb")
	print "   Writing file to ",fdir

	fout.write("Cust_Code,Gender,Age,Branch_Code,Branch,"
		+"Product_1_"+nyear+",Purpose_1_"+nyear+",Loan_Cycle_1_"+nyear+",Approve_Date_1_"+nyear+",Maturity_Date_1_"+nyear+",Closed_Date_1_"+nyear+",Duration_1_"+nyear+","
		+"Currency_1_"+nyear+",Amount_1_"+nyear+",Markup_1_"+nyear+",Installment_AFA_1_"+nyear+","
		+"Product_2_"+nyear+",Purpose_2_"+nyear+",Loan_Cycle_2_"+nyear+",Approve_Date_2_"+nyear+",Maturity_Date_2_"+nyear+",Closed_Date_2_"+nyear+",Duration_2_"+nyear+","
		+"Currency_2_"+nyear+",Amount_2_"+nyear+",Markup_2_"+nyear+",Installment_AFA_2_"+nyear+","
		+"Product_3_"+nyear+",Purpose_3_"+nyear+",Loan_Cycle_3_"+nyear+",Approve_Date_3_"+nyear+",Maturity_Date_3_"+nyear+",Closed_Date_3_"+nyear+",Duration_3_"+nyear+","
		+"Currency_3_"+nyear+",Amount_3_"+nyear+",Markup_3_"+nyear+",Installment_AFA_3_"+nyear+","
		+"Net_Income_USD_"+nyear+",Gross_Income_USD_"+nyear+","
		+"Product_1_"+oyear+",Purpose_1_"+oyear+",Loan_Cycle_1_"+oyear+",Approve_Date_1_"+oyear+",Maturity_Date_1_"+oyear+",Closed_Date_1_"+oyear+",Duration_1_"+oyear+","
		+"Currency_1_"+oyear+",Amount_1_"+oyear+",Markup_1_"+oyear+",Installment_AFA_1_"+oyear+","
		+"Product_2_"+oyear+",Purpose_2_"+oyear+",Loan_Cycle_2_"+oyear+",Approve_Date_2_"+oyear+",Maturity_Date_2_"+oyear+",Closed_Date_2_"+oyear+",Duration_2_"+oyear+","
		+"Currency_2_"+oyear+",Amount_2_"+oyear+",Markup_2_"+oyear+",Installment_AFA_2_"+oyear+","
		+"Product_3_"+oyear+",Purpose_3_"+oyear+",Loan_Cycle_3_"+oyear+",Approve_Date_3_"+oyear+",Maturity_Date_3_"+oyear+",Closed_Date_3_"+oyear+",Duration_3_"+oyear+","
		+"Currency_3_"+oyear+",Amount_3_"+oyear+",Markup_3_"+oyear+",Installment_AFA_3_"+oyear+","
		+"Net_Income_USD_"+oyear+",Gross_Income_USD_"+oyear+","
		+"Change_Net_Income_USD,Change_Gross_Income_USD"
		+"\n")
	plce=1
	mtch=0
	nmtchs=0
	for row in range(1,len(fdnew)):

		if row%1000==0: print "      Searched ",row," of ",len(fdnew)-1," clients..."

		for sow in range(plce,len(fdold)):
		
			if mtch!=1 and fdnew[row][0]==fdold[sow][0]:
				
				mtch=1
				nmtchs+=1
				plce=sow
				
				#final income for newer year
				if fdnew[row][34]!="":
					if int(fdnew[row][33])<int(fdnew[row][20]):
						if fdnew[row][36]!="": led1=fdnew[row][36]
						else: led1=fdnew[row][35]
						if findinperiodexclusive(datetime.strptime(fdnew[row][34],"%m/%d/%Y"),datetime.strptime(led1,"%m/%d/%Y"),datetime.strptime(fdnew[row][21],"%m/%d/%Y"))==0:
							if float(fdnew[row][29])>=float(fdnew[row][42]): nwmtch=1
							else: nwmtch=2
						else: 
							print "WHAT?!? Three concurrent new loans for real!!"
							nwmtch=3
					else: 
						if fdnew[row][23]!="": led2=fdnew[row][23]
						else: led=fdnew[row][22]
						if findinperiodexclusive(datetime.strptime(fdnew[row][21],"%m/%d/%Y"),datetime.strptime(led2,"%m/%d/%Y"),datetime.strptime(fdnew[row][34],"%m/%d/%Y"))==0:
							if float(fdnew[row][29])>=float(fdnew[row][42]): nwmtch=1
							else: nwmtch=2
						else: 
							print "WHAT?!? Three concurrent new loans for real!!"
							nwmtch=3
				elif fdnew[row][31]!="": nwmtch=1
				else: nwmtch=0
				
				if nwmtch==0:
					netincome1=float(fdnew[row][16])
					grossincome1=float(fdnew[row][17])
					fout.write(fdnew[row][0]+","+fdnew[row][1]+","+fdnew[row][2]+","+fdnew[row][3]+","+fdnew[row][4]+","
						+fdnew[row][5]+","+fdnew[row][6]+","+fdnew[row][7]+","+fdnew[row][8]+","+fdnew[row][9]+","+fdnew[row][10]+","
						+fdnew[row][11]+","+fdnew[row][12]+","+fdnew[row][13]+","+fdnew[row][14]+","+fdnew[row][15]+","
						+",,,,,,,,,,,"
						+",,,,,,,,,,,"
						+str(netincome1)+","+str(grossincome1)
						+",")
				elif nwmtch==1:
					netincome1=float(fdnew[row][16])+float(fdnew[row][29])
					grossincome1=float(fdnew[row][17])+float(fdnew[row][30])
					fout.write(fdnew[row][0]+","+fdnew[row][1]+","+fdnew[row][2]+","+fdnew[row][3]+","+fdnew[row][4]+","
						+fdnew[row][5]+","+fdnew[row][6]+","+fdnew[row][7]+","+fdnew[row][8]+","+fdnew[row][9]+","+fdnew[row][10]+","
						+fdnew[row][11]+","+fdnew[row][12]+","+fdnew[row][13]+","+fdnew[row][14]+","+fdnew[row][15]+","
						+fdnew[row][18]+","+fdnew[row][19]+","+fdnew[row][20]+","+fdnew[row][21]+","+fdnew[row][22]+","+fdnew[row][23]+","
						+fdnew[row][24]+","+fdnew[row][25]+","+fdnew[row][26]+","+fdnew[row][27]+","+fdnew[row][28]+","
						+",,,,,,,,,,,"
						+str(netincome1)+","+str(grossincome1)
						+",")
				elif nwmtch==2:
					netincome1=float(fdnew[row][16])+float(fdnew[row][42])
					grossincome1=float(fdnew[row][17])+float(fdnew[row][43])
					fout.write(fdnew[row][0]+","+fdnew[row][1]+","+fdnew[row][2]+","+fdnew[row][3]+","+fdnew[row][4]+","
						+fdnew[row][5]+","+fdnew[row][6]+","+fdnew[row][7]+","+fdnew[row][8]+","+fdnew[row][9]+","+fdnew[row][10]+","
						+fdnew[row][11]+","+fdnew[row][12]+","+fdnew[row][13]+","+fdnew[row][14]+","+fdnew[row][15]+","
						+fdnew[row][31]+","+fdnew[row][32]+","+fdnew[row][33]+","+fdnew[row][34]+","+fdnew[row][35]+","+fdnew[row][36]+","
						+fdnew[row][37]+","+fdnew[row][38]+","+fdnew[row][39]+","+fdnew[row][40]+","+fdnew[row][41]+","
						+",,,,,,,,,,,"
						+str(netincome1)+","+str(grossincome1)
						+",")
				elif nwmtch==3:
					netincome1=float(fdnew[row][16])+float(fdnew[row][29])+float(fdnew[row][42])
					grossincome1=float(fdnew[row][17])+float(fdnew[row][30])+float(fdnew[row][43])
					fout.write(fdnew[row][0]+","+fdnew[row][1]+","+fdnew[row][2]+","+fdnew[row][3]+","+fdnew[row][4]+","
						+fdnew[row][5]+","+fdnew[row][6]+","+fdnew[row][7]+","+fdnew[row][8]+","+fdnew[row][9]+","+fdnew[row][10]+","
						+fdnew[row][11]+","+fdnew[row][12]+","+fdnew[row][13]+","+fdnew[row][14]+","+fdnew[row][15]+","
						+fdnew[row][18]+","+fdnew[row][19]+","+fdnew[row][20]+","+fdnew[row][21]+","+fdnew[row][22]+","+fdnew[row][23]+","
						+fdnew[row][24]+","+fdnew[row][25]+","+fdnew[row][26]+","+fdnew[row][27]+","+fdnew[row][28]+","
						+fdnew[row][31]+","+fdnew[row][32]+","+fdnew[row][33]+","+fdnew[row][34]+","+fdnew[row][35]+","+fdnew[row][36]+","
						+fdnew[row][37]+","+fdnew[row][38]+","+fdnew[row][39]+","+fdnew[row][40]+","+fdnew[row][41]+","
						+str(netincome1)+","+str(grossincome1)
						+",")
				else: print "ERROR!! I can't compute this Dave"
				
				#final income for older year
				if fdold[sow][34]!="":
					if int(fdold[sow][33])<int(fdold[sow][20]):
						if fdold[sow][36]!="": led1=fdold[sow][36]
						else: led1=fdold[sow][35]
						if findinperiodexclusive(datetime.strptime(fdold[sow][34],"%m/%d/%Y"),datetime.strptime(led1,"%m/%d/%Y"),datetime.strptime(fdold[sow][21],"%m/%d/%Y"))==0:
							if float(fdold[sow][29])>=float(fdold[sow][42]): oldmtch=1
							else: oldmtch=2
						else: 
							print "WHAT?!? Three concurrent old loans for real!!"
							oldmtch=3
					else: 
						if fdold[sow][23]!="": led2=fdold[sow][23]
						else: led=fdold[sow][22]
						if findinperiodexclusive(datetime.strptime(fdold[sow][21],"%m/%d/%Y"),datetime.strptime(led2,"%m/%d/%Y"),datetime.strptime(fdold[sow][34],"%m/%d/%Y"))==0:
							if float(fdold[sow][29])>=float(fdold[sow][42]): oldmtch=1
							else: oldmtch=2
						else: 
							print "WHAT?!? Three concurrent old loans for real!!"
							oldmtch=3
				elif fdold[sow][31]!="": oldmtch=1
				else: oldmtch=0
				
				if oldmtch==0:
					netincome2=float(fdold[sow][16])
					grossincome2=float(fdold[sow][17])
					fout.write(fdold[sow][0]+","+fdold[sow][1]+","+fdold[sow][2]+","+fdold[sow][3]+","+fdold[sow][4]+","
						+fdold[sow][5]+","+fdold[sow][6]+","+fdold[sow][7]+","+fdold[sow][8]+","+fdold[sow][9]+","+fdold[sow][10]+","
						+fdold[sow][11]+","+fdold[sow][12]+","+fdold[sow][13]+","+fdold[sow][14]+","+fdold[sow][15]+","
						+",,,,,,,,,,,"
						+",,,,,,,,,,,"
						+str(netincome2)+","+str(grossincome2)
						+",")
				elif oldmtch==1:
					netincome2=float(fdold[sow][16])+float(fdold[sow][29])
					grossincome2=float(fdold[sow][17])+float(fdold[sow][30])
					fout.write(fdold[sow][0]+","+fdold[sow][1]+","+fdold[sow][2]+","+fdold[sow][3]+","+fdold[sow][4]+","
						+fdold[sow][5]+","+fdold[sow][6]+","+fdold[sow][7]+","+fdold[sow][8]+","+fdold[sow][9]+","+fdold[sow][10]+","
						+fdold[sow][11]+","+fdold[sow][12]+","+fdold[sow][13]+","+fdold[sow][14]+","+fdold[sow][15]+","
						+fdold[sow][18]+","+fdold[sow][19]+","+fdold[sow][20]+","+fdold[sow][21]+","+fdold[sow][22]+","+fdold[sow][23]+","
						+fdold[sow][24]+","+fdold[sow][25]+","+fdold[sow][26]+","+fdold[sow][27]+","+fdold[sow][28]+","
						+",,,,,,,,,,,"
						+str(netincome2)+","+str(grossincome2)
						+",")
				elif oldmtch==2:
					netincome2=float(fdold[sow][16])+float(fdold[sow][42])
					grossincome2=float(fdold[sow][17])+float(fdold[sow][43])
					fout.write(fdold[sow][0]+","+fdold[sow][1]+","+fdold[sow][2]+","+fdold[sow][3]+","+fdold[sow][4]+","
						+fdold[sow][5]+","+fdold[sow][6]+","+fdold[sow][7]+","+fdold[sow][8]+","+fdold[sow][9]+","+fdold[sow][10]+","
						+fdold[sow][11]+","+fdold[sow][12]+","+fdold[sow][13]+","+fdold[sow][14]+","+fdold[sow][15]+","
						+fdold[sow][31]+","+fdold[sow][32]+","+fdold[sow][33]+","+fdold[sow][34]+","+fdold[sow][35]+","+fdold[sow][36]+","
						+fdold[sow][37]+","+fdold[sow][38]+","+fdold[sow][39]+","+fdold[sow][40]+","+fdold[sow][41]+","
						+",,,,,,,,,,,"
						+str(netincome2)+","+str(grossincome2)
						+",")
				elif oldmtch==3:
					netincome2=float(fdold[sow][16])+float(fdold[sow][29])+float(fdold[sow][42])
					grossincome2=float(fdold[sow][17])+float(fdold[sow][30])+float(fdold[sow][43])
					fout.write(fdold[sow][0]+","+fdold[sow][1]+","+fdold[sow][2]+","+fdold[sow][3]+","+fdold[sow][4]+","
						+fdold[sow][5]+","+fdold[sow][6]+","+fdold[sow][7]+","+fdold[sow][8]+","+fdold[sow][9]+","+fdold[sow][10]+","
						+fdold[sow][11]+","+fdold[sow][12]+","+fdold[sow][13]+","+fdold[sow][14]+","+fdold[sow][15]+","
						+fdold[sow][18]+","+fdold[sow][19]+","+fdold[sow][20]+","+fdold[sow][21]+","+fdold[sow][22]+","+fdold[sow][23]+","
						+fdold[sow][24]+","+fdold[sow][25]+","+fdold[sow][26]+","+fdold[sow][27]+","+fdold[sow][28]+","
						+fdold[sow][31]+","+fdold[sow][32]+","+fdold[sow][33]+","+fdold[sow][34]+","+fdold[sow][35]+","+fdold[sow][36]+","
						+fdold[sow][37]+","+fdold[sow][38]+","+fdold[sow][39]+","+fdold[sow][40]+","+fdold[sow][41]+","
						+str(netincome2)+","+str(grossincome2)
						+",")
				else: print "ERROR!! I can't compute this Dave"
				
				dnetincome=netincome1-netincome2
				dgrossincome=grossincome1-grossincome2
				
				fout.write(str(dnetincome)+","+str(dgrossincome)+"\n")
				
				continue 
				
		mtch=0

	print "   Finished finding matches between records from ",nyear," and ",oyear," with ",nmtchs," clients with records in both years!"
	fout.close()
	fnew.close()
	fold.close()
