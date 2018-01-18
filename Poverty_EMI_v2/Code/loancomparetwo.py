import inspect,os,csv,sys
from datetime import datetime
from findintime import *

def loancomparetwo(nyear,oyear,nqrt):

	fdir=os.getcwd()+"/Data/"
	print "   Loading file from ",nyear
	fnew=open(fdir+"/All_Loans_"+nyear+"_Q"+str(nqrt)+".csv","rU")
	frnew=csv.reader(fnew,delimiter=",")
	fdnew=list(frnew)
	print "   File loaded"

	print "   Loading file from ",oyear
	fold=open(fdir+"/All_Loans_"+oyear+".csv","rU")
	frold=csv.reader(fold,delimiter=",")
	fdold=list(frold)
	print "   File loaded"

	fout=open(fdir+"/Loans_Compare_"+nyear+"_Q"+str(nqrt)+"_to_"+oyear+".csv","wb")
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
		
		
		
		

	print "   Searching ",len(fdnew)-1," clients from ",nyear," for matches in ",oyear

	dup=0
	plce=1
	mtch=0
	nmtchs=0
	
	for row in range(1,len(fdnew)):

		if row%1000==0: print "      Searched ",row," of ",len(fdnew)-1," clients..."

		if dup!=0:
			dup-=1
			continue
		
		for sow in range(plce,len(fdold)):
			
			if mtch!=1 and fdnew[row][0]==fdold[sow][0]:
			
				fout.write(fdnew[row][0]+","+fdnew[row][1]+","+fdnew[row][2]+","+fdnew[row][3]+","+fdnew[row][4]+",")
				
				nnet=float(fdnew[row][16])
				ngross=float(fdnew[row][17])

				if len(fdnew)>row+1 and fdnew[row][0]==fdnew[row+1][0]:
					dup=1
					
					if len(fdnew)>row+2 and fdnew[row][0]==fdnew[row+2][0]:
						dup=2
						if fdnew[row][10]=="": nl1=datetime.strptime(fdnew[row][9],"%m/%d/%Y")
						else: nl1=datetime.strptime(fdnew[row][10],"%m/%d/%Y")
						
						if fdnew[row+1][10]=="": nl2=datetime.strptime(fdnew[row+1][9],"%m/%d/%Y")
						else: nl2=datetime.strptime(fdnew[row+1][10],"%m/%d/%Y")
						
						if fdnew[row+2][10]=="": nl3=datetime.strptime(fdnew[row+2][9],"%m/%d/%Y")
						else: nl3=datetime.strptime(fdnew[row+2][10],"%m/%d/%Y")
						
						otcon=findinperiodexclusive(datetime.strptime(fdnew[row][8],"%m/%d/%Y"),nl1,datetime.strptime(fdnew[row+1][8],"%m/%d/%Y"))
						tthcon=findinperiodexclusive(datetime.strptime(fdnew[row+1][8],"%m/%d/%Y"),nl2,datetime.strptime(fdnew[row+2][8],"%m/%d/%Y"))
						othcon=findinperiodexclusive(datetime.strptime(fdnew[row][8],"%m/%d/%Y"),nl1,datetime.strptime(fdnew[row+2][8],"%m/%d/%Y"))
						
						if otcon==0 and tthcon==0 and othcon==0:
							if fdnew[row+1][16]>fdnew[row][16] or fdnew[row+2][16]>fdnew[row][16]: 
								if fdnew[row+1][16]>=fdnew[row+2][16]: 
									nnet=float(fdnew[row+1][16])
									ngross=float(fdnew[row+1][17])
								else: 
									nnet=float(fdnew[row+2][16])
									ngross=float(fdnew[row+2][17])
						if otcon==1 and tthcon==0 and othcon==0:
							nnet+=float(fdnew[row+1][16])
							ngross+=float(fdnew[row+1][17])
						if otcon==0 and tthcon==1 and othcon==0:
							nnet=float(fdnew[row+1][16])+float(fdnew[row+2][16])
							ngross=float(fdnew[row+1][17])+float(fdnew[row+2][17])
						if otcon==0 and tthcon==0 and othcon==1:
							nnet+=float(fdnew[row+2][16])
							ngross+=float(fdnew[row+2][17])
						if otcon==1 and tthcon==1 and othcon==0:
							otnet=float(fdnew[row+1][16])+float(fdnew[row][16])
							tthnet=float(fdnew[row+1][16])+float(fdnew[row+2][16])
							if otnet>tthnet:
								nnet=otnet
								ngross=float(fdnew[row+1][17])+float(fdnew[row][17])
							else: 
								nnet=tthnet
								ngross=float(fdnew[row+1][17])+float(fdnew[row+2][17])
						if otcon==1 and tthcon==0 and othcon==1:
							otnet=float(fdnew[row+1][16])+float(fdnew[row][16])
							othnet=float(fdnew[row][16])+float(fdnew[row+2][16])
							if otnet>othnet:
								nnet=otnet
								ngross=float(fdnew[row+1][17])+float(fdnew[row][17])
							else: 
								nnet=othnet
								ngross=float(fdnew[row][17])+float(fdnew[row+2][17])
						if otcon==0 and tthcon==1 and othcon==1:
							othnet=float(fdnew[row][16])+float(fdnew[row+2][16])
							tthnet=float(fdnew[row+1][16])+float(fdnew[row+2][16])
							if othnet>tthnet:
								nnet=othnet
								ngross=float(fdnew[row+2][17])+float(fdnew[row][17])
							else: 
								nnet=tthnet
								ngross=float(fdnew[row+1][17])+float(fdnew[row+2][17])
						fout.write(fdnew[row][5]+","+fdnew[row][6]+","+fdnew[row][7]+","+fdnew[row][8]+","+fdnew[row][9]+","+fdnew[row][10]+","
							+fdnew[row][11]+","+fdnew[row][12]+","+fdnew[row][13]+","+fdnew[row][14]+","+fdnew[row][15]+","
							+fdnew[row+1][5]+","+fdnew[row+1][6]+","+fdnew[row+1][7]+","+fdnew[row+1][8]+","+fdnew[row+1][9]+","+fdnew[row+1][10]+","
							+fdnew[row+1][11]+","+fdnew[row+1][12]+","+fdnew[row+1][13]+","+fdnew[row+1][14]+","+fdnew[row+1][15]+","
							+fdnew[row+2][5]+","+fdnew[row+2][6]+","+fdnew[row+2][7]+","+fdnew[row+2][8]+","+fdnew[row+2][9]+","+fdnew[row+2][10]+","
							+fdnew[row+2][11]+","+fdnew[row+2][12]+","+fdnew[row+2][13]+","+fdnew[row+2][14]+","+fdnew[row+2][15]+","+str(nnet)+","+str(ngross)+",")
					else:
						if fdnew[row][10]=="":
							if datetime.strptime(fdnew[row+1][8],"%m/%d/%Y")>=datetime.strptime(fdnew[row][8],"%m/%d/%Y"):
								nnet+=float(fdnew[row+1][16])
								ngross+=float(fdnew[row+1][17])
							else: 
								if float(fdnew[row+1][16])>nnet and float(fdnew[row+1][17])>ngross:
									nnet=float(fdnew[row+1][16])
									ngross=float(fdnew[row+1][17])
						else: 
							if findinperiodexclusive(datetime.strptime(fdnew[row][8],"%m/%d/%Y"),datetime.strptime(fdnew[row][10],"%m/%d/%Y"),datetime.strptime(fdnew[row+1][8],"%m/%d/%Y"))==1:
								nnet+=float(fdnew[row+1][16])
								ngross+=float(fdnew[row+1][17])
							else: 
								if float(fdnew[row+1][16])>nnet and float(fdnew[row+1][17])>ngross: 
									nnet=float(fdnew[row+1][16])
									ngross=float(fdnew[row+1][17])
						
						fout.write(fdnew[row][5]+","+fdnew[row][6]+","+fdnew[row][7]+","+fdnew[row][8]+","+fdnew[row][9]+","+fdnew[row][10]+","
							+fdnew[row][11]+","+fdnew[row][12]+","+fdnew[row][13]+","+fdnew[row][14]+","+fdnew[row][15]+","
							+fdnew[row+1][5]+","+fdnew[row+1][6]+","+fdnew[row+1][7]+","+fdnew[row+1][8]+","+fdnew[row+1][9]+","+fdnew[row+1][10]+","
							+fdnew[row+1][11]+","+fdnew[row+1][12]+","+fdnew[row+1][13]+","+fdnew[row+1][14]+","+fdnew[row+1][15]+","
							+",,,,,,,,,,,"+str(nnet)+","+str(ngross)+",")
							
				else: 
					fout.write(fdnew[row][5]+","+fdnew[row][6]+","+fdnew[row][7]+","+fdnew[row][8]+","+fdnew[row][9]+","+fdnew[row][10]+","
						+fdnew[row][11]+","+fdnew[row][12]+","+fdnew[row][13]+","+fdnew[row][14]+","+fdnew[row][15]+","
						+",,,,,,,,,,,,,,,,,,,,,,"+str(nnet)+","+str(ngross)+",")
				
				mtch=1
				onet=float(fdold[sow][16])
				ogross=float(fdold[sow][17])
				nmtchs+=1
				ocase=0
				
				if len(fdold)>sow+1 and fdold[sow][0]==fdold[sow+1][0]:
					plce=sow+1
					
					if len(fdold)>sow+2 and fdold[sow][0]==fdold[sow+2][0]:
						plce=sow+2
						
						if fdold[sow][10]=="": nl1=datetime.strptime(fdold[sow][9],"%m/%d/%Y")
						else: nl1=datetime.strptime(fdold[sow][10],"%m/%d/%Y")
						
						if fdold[sow+1][10]=="": nl2=datetime.strptime(fdold[sow+1][9],"%m/%d/%Y")
						else: nl2=datetime.strptime(fdold[sow+1][10],"%m/%d/%Y")
						
						if fdold[sow+2][10]=="": nl3=datetime.strptime(fdold[sow+2][9],"%m/%d/%Y")
						else: nl3=datetime.strptime(fdold[sow+2][10],"%m/%d/%Y")
						
						otcon=findinperiodexclusive(datetime.strptime(fdold[sow][8],"%m/%d/%Y"),nl1,datetime.strptime(fdold[sow+1][8],"%m/%d/%Y"))
						tthcon=findinperiodexclusive(datetime.strptime(fdold[sow+1][8],"%m/%d/%Y"),nl2,datetime.strptime(fdold[sow+2][8],"%m/%d/%Y"))
						othcon=findinperiodexclusive(datetime.strptime(fdold[sow][8],"%m/%d/%Y"),nl1,datetime.strptime(fdold[sow+2][8],"%m/%d/%Y"))
						
						if otcon==0 and tthcon==0 and othcon==0:
							if fdold[sow+1][16]>fdold[sow][16] or fdold[sow+2][16]>fdold[sow][16]: 
								if fdold[sow+1][16]>=fdold[sow+2][16]: 
									onet=float(fdold[sow+1][16])
									ogross=float(fdold[sow+1][17])
								else: 
									onet=float(fdold[sow+2][16])
									ogross=float(fdold[sow+2][17])
						if otcon==1 and tthcon==0 and othcon==0:
							onet+=float(fdold[sow+1][16])
							ogross+=float(fdold[sow+1][17])
						if otcon==0 and tthcon==1 and othcon==0:
							onet=float(fdold[sow+1][16])+float(fdold[sow+2][16])
							ogross=float(fdold[sow+1][17])+float(fdold[sow+2][17])
						if otcon==0 and tthcon==0 and othcon==1:
							onet+=float(fdold[sow+2][16])
							ogross+=float(fdold[sow+2][17])
						if otcon==1 and tthcon==1 and othcon==0:
							otnet=float(fdold[sow+1][16])+float(fdold[sow][16])
							tthnet=float(fdold[sow+1][16])+float(fdold[sow+2][16])
							if otnet>tthnet:
								onet=otnet
								ogross=float(fdold[sow+1][17])+float(fdold[sow][17])
							else: 
								onet=tthnet
								ogross=float(fdold[sow+1][17])+float(fdold[sow+2][17])
						if otcon==1 and tthcon==0 and othcon==1:
							otnet=float(fdold[sow+1][16])+float(fdold[sow][16])
							othnet=float(fdold[sow][16])+float(fdold[sow+2][16])
							if otnet>othnet:
								onet=otnet
								ogross=float(fdold[sow+1][17])+float(fdold[sow][17])
							else: 
								onet=othnet
								ogross=float(fdold[sow][17])+float(fdold[sow+2][17])
						if otcon==0 and tthcon==1 and othcon==1:
							othnet=float(fdold[sow][16])+float(fdold[sow+2][16])
							tthnet=float(fdold[sow+1][16])+float(fdold[sow+2][16])
							if othnet>tthnet:
								onet=othnet
								ogross=float(fdold[sow+2][17])+float(fdold[sow][17])
							else: 
								onet=tthnet
								ogross=float(fdold[sow+1][17])+float(fdold[sow+2][17])
						
						fout.write(fdold[sow][5]+","+fdold[sow][6]+","+fdold[sow][7]+","+fdold[sow][8]+","+fdold[sow][9]+","+fdold[sow][10]+","
							+fdold[sow][11]+","+fdold[sow][12]+","+fdold[sow][13]+","+fdold[sow][14]+","+fdold[sow][15]+","
							+fdold[sow+1][5]+","+fdold[sow+1][6]+","+fdold[sow+1][7]+","+fdold[sow+1][8]+","+fdold[sow+1][9]+","+fdold[sow+1][10]+","
							+fdold[sow+1][11]+","+fdold[sow+1][12]+","+fdold[sow+1][13]+","+fdold[sow+1][14]+","+fdold[sow+1][15]+","
							+fdold[sow+2][5]+","+fdold[sow+2][6]+","+fdold[sow+2][7]+","+fdold[sow+2][8]+","+fdold[sow+2][9]+","+fdold[sow+2][10]+","
							+fdold[sow+2][11]+","+fdold[sow+2][12]+","+fdold[sow+2][13]+","+fdold[sow+2][14]+","+fdold[sow+2][15]+","+str(onet)+","+str(ogross)+",")
							
					else:
						if fdold[sow][10]=="":
							if datetime.strptime(fdold[sow+1][8],"%m/%d/%Y")>=datetime.strptime(fdold[sow][8],"%m/%d/%Y"):
								onet+=float(fdold[sow+1][16])
								ogross+=float(fdold[sow+1][17])
							else: 
								if float(fdold[sow+1][16])>onet and float(fdold[sow+1][17])>ogross:
									onet=float(fdold[sow+1][16])
									ogross=float(fdold[sow+1][17])
						else: 
							if findinperiodexclusive(datetime.strptime(fdold[sow][8],"%m/%d/%Y"),datetime.strptime(fdold[sow][10],"%m/%d/%Y"),datetime.strptime(fdold[sow+1][8],"%m/%d/%Y"))==1:
								onet+=float(fdold[sow+1][16])
								ogross+=float(fdold[sow+1][17])
							else: 
								if float(fdold[sow+1][16])>onet and float(fdold[sow+1][17])>ogross: 
									onet=float(fdold[sow+1][16])
									ogross=float(fdold[sow+1][17])

						fout.write(fdold[sow][5]+","+fdold[sow][6]+","+fdold[sow][7]+","+fdold[sow][8]+","+fdold[sow][9]+","+fdold[sow][10]+","
							+fdold[sow][11]+","+fdold[sow][12]+","+fdold[sow][13]+","+fdold[sow][14]+","+fdold[sow][15]+","
							+fdold[sow+1][5]+","+fdold[sow+1][6]+","+fdold[sow+1][7]+","+fdold[sow+1][8]+","+fdold[sow+1][9]+","+fdold[sow+1][10]+","
							+fdold[sow+1][11]+","+fdold[sow+1][12]+","+fdold[sow+1][13]+","+fdold[sow+1][14]+","+fdold[sow+1][15]+","
							+",,,,,,,,,,,"+str(onet)+","+str(ogross)+",")
							
				else:
					plce=sow
					fout.write(fdold[sow][5]+","+fdold[sow][6]+","+fdold[sow][7]+","+fdold[sow][8]+","+fdold[sow][9]+","+fdold[sow][10]+","
						+fdold[sow][11]+","+fdold[sow][12]+","+fdold[sow][13]+","+fdold[sow][14]+","+fdold[sow][15]+","
						+",,,,,,,,,,,,,,,,,,,,,,"+str(onet)+","+str(ogross)+",")
				
				dnet=nnet-onet
				dgross=ngross-ogross
				fout.write(str(dnet)+","+str(dgross)+"\n")
				
		mtch=0
		
	print "   Finished finding matches between records from ",nyear," and ",oyear," with ",nmtchs," clients with records in both years!"
	fout.close()
	fnew.close()
	fold.close()