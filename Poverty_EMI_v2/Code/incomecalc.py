import inspect,os,csv,sys
from datetime import datetime
from findintime import *
from afgbranch import afgbranch
from productdecode import *

def incomecalc(nyear,nopen,nclosed,nqrt):

	if str(nqrt)!="": quart="_Q"+str(nqrt)
	else: quart=""

	frdir=os.getcwd()
	fdir=os.getcwd()+"/Data/"
	print "   Loading file from ",nyear
	fin=open(fdir+"/All_Loans_"+nyear+quart+".csv","rU")
	frin=csv.reader(fin,delimiter=",")
	fdin=list(frin)
	print "   File loaded"
	
	print "      Loading file of open loans"
	fop=open(frdir+"/"+nopen+".csv","rU")
	frop=csv.reader(fop,delimiter=",")
	fdop=list(frop)
	print "      File loaded"
	
	print "      Loading file of closed loans"
	fcl=open(frdir+"/"+nclosed+".csv","rU")
	frcl=csv.reader(fcl,delimiter=",")
	fdcl=list(frcl)
	print "      File loaded"

	fout=open(fdir+"/All_Income_"+nyear+quart+".csv","wb")
	print "   Writing file to ",fdir

	fout.write("Cust_Code,Gender,Age,Branch_Code,Branch,"
		+"Product_1_"+nyear+",Purpose_1_"+nyear+",Loan_Cycle_1_"+nyear+",Approve_Date_1_"+nyear+",Maturity_Date_1_"+nyear+",Closed_Date_1_"+nyear+",Duration_1_"+nyear+","
		+"Currency_1_"+nyear+",Amount_1_"+nyear+",Markup_1_"+nyear+",Installment_AFA_1_"+nyear+",Net_Income_USD_1_"+nyear+",Gross_Income_USD_1_"+nyear+","
		+"Product_2_"+nyear+",Purpose_2_"+nyear+",Loan_Cycle_2_"+nyear+",Approve_Date_2_"+nyear+",Maturity_Date_2_"+nyear+",Closed_Date_2_"+nyear+",Duration_2_"+nyear+","
		+"Currency_2_"+nyear+",Amount_2_"+nyear+",Markup_2_"+nyear+",Installment_AFA_2_"+nyear+",Net_Income_USD_2_"+nyear+",Gross_Income_USD_2_"+nyear+","
		+"Product_3_"+nyear+",Purpose_3_"+nyear+",Loan_Cycle_3_"+nyear+",Approve_Date_3_"+nyear+",Maturity_Date_3_"+nyear+",Closed_Date_3_"+nyear+",Duration_3_"+nyear+","
		+"Currency_3_"+nyear+",Amount_3_"+nyear+",Markup_3_"+nyear+",Installment_AFA_3_"+nyear+",Net_Income_USD_3_"+nyear+",Gross_Income_USD_3_"+nyear+"\n")
		
	
	
	print "   Searching ",len(fdin)-1," clients from ",nyear," for concurrent loans"

	dup=0
	plce=1
	mtch=0
	nmtchs=0
	otcon=0
	tthcon=0
	othcon=0
	pos=0
	shft=0

	for row in range(1,len(fdin)):

		if row%100==0: print "      Searched ",row," of ",len(fdin)-1," clients..."

		if dup!=0:
			dup-=1
			continue
	
		fout.write(fdin[row][0]+","+fdin[row][1]+","+fdin[row][2]+","+fdin[row][3]+","+fdin[row][4]+",")
		
		if fdin[row][10]=="": nl1=datetime.strptime(fdin[row][9],"%m/%d/%Y")
		else: nl1=datetime.strptime(fdin[row][10],"%m/%d/%Y")
		
		if len(fdin)>row+1 and fdin[row][0]==fdin[row+1][0]:
			dup=1
			
			if fdin[row+1][10]=="": nl2=datetime.strptime(fdin[row+1][9],"%m/%d/%Y")
			else: nl2=datetime.strptime(fdin[row+1][10],"%m/%d/%Y")
			
			otcon=findinperiodexclusive(datetime.strptime(fdin[row][8],"%m/%d/%Y"),nl1,datetime.strptime(fdin[row+1][8],"%m/%d/%Y"))
			
			if len(fdin)>row+2 and fdin[row][0]==fdin[row+2][0]:
				dup=2
				
				if fdin[row+2][10]=="": nl3=datetime.strptime(fdin[row+2][9],"%m/%d/%Y")
				else: nl3=datetime.strptime(fdin[row+2][10],"%m/%d/%Y")
				
				tthcon=findinperiodexclusive(datetime.strptime(fdin[row+1][8],"%m/%d/%Y"),nl2,datetime.strptime(fdin[row+2][8],"%m/%d/%Y"))
				othcon=findinperiodexclusive(datetime.strptime(fdin[row][8],"%m/%d/%Y"),nl1,datetime.strptime(fdin[row+2][8],"%m/%d/%Y"))
		if dup==1:
			if otcon==1: 
				fout.write(fdin[row][5]+","+fdin[row][6]+","+fdin[row][7]+","+fdin[row][8]+","+fdin[row][9]+","+fdin[row][10]+","
							+fdin[row][11]+","+fdin[row][12]+","+fdin[row][13]+","+fdin[row][14]+","+fdin[row][15]+","+fdin[row][16]+","+fdin[row][17]+","
							+fdin[row+1][5]+","+fdin[row+1][6]+","+fdin[row+1][7]+","+fdin[row+1][8]+","+fdin[row+1][9]+","+fdin[row+1][10]+","
							+fdin[row+1][11]+","+fdin[row+1][12]+","+fdin[row+1][13]+","+fdin[row+1][14]+","+fdin[row+1][15]+","+fdin[row+1][16]+","+fdin[row+1][17])
				pos=2
			else: 
				pos=1
				if fdin[row+1][16]>fdin[row][16]:
					fout.write(fdin[row+1][5]+","+fdin[row+1][6]+","+fdin[row+1][7]+","+fdin[row+1][8]+","+fdin[row+1][9]+","+fdin[row+1][10]+","
							+fdin[row+1][11]+","+fdin[row+1][12]+","+fdin[row+1][13]+","+fdin[row+1][14]+","+fdin[row+1][15]+","+fdin[row+1][16]+","+fdin[row+1][17])
					shft=1
				else:
					fout.write(fdin[row][5]+","+fdin[row][6]+","+fdin[row][7]+","+fdin[row][8]+","+fdin[row][9]+","+fdin[row][10]+","
								+fdin[row][11]+","+fdin[row][12]+","+fdin[row][13]+","+fdin[row][14]+","+fdin[row][15]+","+fdin[row][16]+","+fdin[row][17])
		elif dup==2:
			if otcon==0 and tthcon==0 and othcon==0:
				pos=1
				if fdin[row+1][16]>fdin[row][16] or fdin[row+2][16]>fdin[row][16]: 
					if fdin[row+1][16]>=fdin[row+2][16]: 
						fout.write(fdin[row+1][5]+","+fdin[row+1][6]+","+fdin[row+1][7]+","+fdin[row+1][8]+","+fdin[row+1][9]+","+fdin[row+1][10]+","
							+fdin[row+1][11]+","+fdin[row+1][12]+","+fdin[row+1][13]+","+fdin[row+1][14]+","+fdin[row+1][15]+","+fdin[row+1][16]+","+fdin[row+1][17])
						shft=1
					else: 
						fout.write(fdin[row+2][5]+","+fdin[row+2][6]+","+fdin[row+2][7]+","+fdin[row+2][8]+","+fdin[row+2][9]+","+fdin[row+2][10]+","
							+fdin[row+2][11]+","+fdin[row+2][12]+","+fdin[row+2][13]+","+fdin[row+2][14]+","+fdin[row+2][15]+","+fdin[row+2][16]+","+fdin[row+2][17])
						shft=2
				else: 
					fout.write(fdin[row][5]+","+fdin[row][6]+","+fdin[row][7]+","+fdin[row][8]+","+fdin[row][9]+","+fdin[row][10]+","
								+fdin[row][11]+","+fdin[row][12]+","+fdin[row][13]+","+fdin[row][14]+","+fdin[row][15]+","+fdin[row][16]+","+fdin[row][17])
								
			if otcon==1 and tthcon==0 and othcon==0:
				fout.write(fdin[row][5]+","+fdin[row][6]+","+fdin[row][7]+","+fdin[row][8]+","+fdin[row][9]+","+fdin[row][10]+","
							+fdin[row][11]+","+fdin[row][12]+","+fdin[row][13]+","+fdin[row][14]+","+fdin[row][15]+","+fdin[row][16]+","+fdin[row][17]+","
							+fdin[row+1][5]+","+fdin[row+1][6]+","+fdin[row+1][7]+","+fdin[row+1][8]+","+fdin[row+1][9]+","+fdin[row+1][10]+","
							+fdin[row+1][11]+","+fdin[row+1][12]+","+fdin[row+1][13]+","+fdin[row+1][14]+","+fdin[row+1][15]+","+fdin[row+1][16]+","+fdin[row+1][17])
				pos=2
			if otcon==0 and tthcon==1 and othcon==0:
				fout.write(fdin[row+1][5]+","+fdin[row+1][6]+","+fdin[row+1][7]+","+fdin[row+1][8]+","+fdin[row+1][9]+","+fdin[row+1][10]+","
							+fdin[row+1][11]+","+fdin[row+1][12]+","+fdin[row+1][13]+","+fdin[row+1][14]+","+fdin[row+1][15]+","+fdin[row+1][16]+","+fdin[row+1][17]+","
							+fdin[row+2][5]+","+fdin[row+2][6]+","+fdin[row+2][7]+","+fdin[row+2][8]+","+fdin[row+2][9]+","+fdin[row+2][10]+","
							+fdin[row+2][11]+","+fdin[row+2][12]+","+fdin[row+2][13]+","+fdin[row+2][14]+","+fdin[row+2][15]+","+fdin[row+2][16]+","+fdin[row+2][17])
				shft=1
				pos=2
			if otcon==0 and tthcon==0 and othcon==1:
				fout.write(fdin[row][5]+","+fdin[row][6]+","+fdin[row][7]+","+fdin[row][8]+","+fdin[row][9]+","+fdin[row][10]+","
							+fdin[row][11]+","+fdin[row][12]+","+fdin[row][13]+","+fdin[row][14]+","+fdin[row][15]+","+fdin[row][16]+","+fdin[row][17]+","
							+fdin[row+2][5]+","+fdin[row+2][6]+","+fdin[row+2][7]+","+fdin[row+2][8]+","+fdin[row+2][9]+","+fdin[row+2][10]+","
							+fdin[row+2][11]+","+fdin[row+2][12]+","+fdin[row+2][13]+","+fdin[row+2][14]+","+fdin[row+2][15]+","+fdin[row+2][16]+","+fdin[row+2][17])
				pos=2
			if otcon==1 and tthcon==1 and othcon==0:
				otnet=float(fdin[row+1][16])+float(fdin[row][16])
				tthnet=float(fdin[row+1][16])+float(fdin[row+2][16])
				if otnet>tthnet:
					fout.write(fdin[row][5]+","+fdin[row][6]+","+fdin[row][7]+","+fdin[row][8]+","+fdin[row][9]+","+fdin[row][10]+","
								+fdin[row][11]+","+fdin[row][12]+","+fdin[row][13]+","+fdin[row][14]+","+fdin[row][15]+","+fdin[row][16]+","+fdin[row][17]+","
								+fdin[row+1][5]+","+fdin[row+1][6]+","+fdin[row+1][7]+","+fdin[row+1][8]+","+fdin[row+1][9]+","+fdin[row+1][10]+","
								+fdin[row+1][11]+","+fdin[row+1][12]+","+fdin[row+1][13]+","+fdin[row+1][14]+","+fdin[row+1][15]+","+fdin[row+1][16]+","+fdin[row+1][17])
					pos=2
				else: 
					fout.write(fdin[row+1][5]+","+fdin[row+1][6]+","+fdin[row+1][7]+","+fdin[row+1][8]+","+fdin[row+1][9]+","+fdin[row+1][10]+","
								+fdin[row+1][11]+","+fdin[row+1][12]+","+fdin[row+1][13]+","+fdin[row+1][14]+","+fdin[row+1][15]+","+fdin[row+1][16]+","+fdin[row+1][17]+","
								+fdin[row+2][5]+","+fdin[row+2][6]+","+fdin[row+2][7]+","+fdin[row+2][8]+","+fdin[row+2][9]+","+fdin[row+2][10]+","
								+fdin[row+2][11]+","+fdin[row+2][12]+","+fdin[row+2][13]+","+fdin[row+2][14]+","+fdin[row+2][15]+","+fdin[row+2][16]+","+fdin[row+2][17])
					pos=2
					shft=1
			if otcon==1 and tthcon==0 and othcon==1:
				otnet=float(fdin[row+1][16])+float(fdin[row][16])
				othnet=float(fdin[row][16])+float(fdin[row+2][16])
				if otnet>othnet:
					fout.write(fdin[row][5]+","+fdin[row][6]+","+fdin[row][7]+","+fdin[row][8]+","+fdin[row][9]+","+fdin[row][10]+","
								+fdin[row][11]+","+fdin[row][12]+","+fdin[row][13]+","+fdin[row][14]+","+fdin[row][15]+","+fdin[row][16]+","+fdin[row][17]+","
								+fdin[row+1][5]+","+fdin[row+1][6]+","+fdin[row+1][7]+","+fdin[row+1][8]+","+fdin[row+1][9]+","+fdin[row+1][10]+","
								+fdin[row+1][11]+","+fdin[row+1][12]+","+fdin[row+1][13]+","+fdin[row+1][14]+","+fdin[row+1][15]+","+fdin[row+1][16]+","+fdin[row+1][17])
					pos=2
				else: 
					fout.write(fdin[row][5]+","+fdin[row][6]+","+fdin[row][7]+","+fdin[row][8]+","+fdin[row][9]+","+fdin[row][10]+","
								+fdin[row][11]+","+fdin[row][12]+","+fdin[row][13]+","+fdin[row][14]+","+fdin[row][15]+","+fdin[row][16]+","+fdin[row][17]+","
								+fdin[row+2][5]+","+fdin[row+2][6]+","+fdin[row+2][7]+","+fdin[row+2][8]+","+fdin[row+2][9]+","+fdin[row+2][10]+","
								+fdin[row+2][11]+","+fdin[row+2][12]+","+fdin[row+2][13]+","+fdin[row+2][14]+","+fdin[row+2][15]+","+fdin[row+2][16]+","+fdin[row+2][17])
					pos=2
			if otcon==0 and tthcon==1 and othcon==1:
				othnet=float(fdin[row][16])+float(fdin[row+2][16])
				tthnet=float(fdin[row+1][16])+float(fdin[row+2][16])
				if othnet>tthnet:
					fout.write(fdin[row][5]+","+fdin[row][6]+","+fdin[row][7]+","+fdin[row][8]+","+fdin[row][9]+","+fdin[row][10]+","
								+fdin[row][11]+","+fdin[row][12]+","+fdin[row][13]+","+fdin[row][14]+","+fdin[row][15]+","+fdin[row][16]+","+fdin[row][17]+","
								+fdin[row+2][5]+","+fdin[row+2][6]+","+fdin[row+2][7]+","+fdin[row+2][8]+","+fdin[row+2][9]+","+fdin[row+2][10]+","
								+fdin[row+2][11]+","+fdin[row+2][12]+","+fdin[row+2][13]+","+fdin[row+2][14]+","+fdin[row+2][15]+","+fdin[row+2][16]+","+fdin[row+2][17])
					pos=2
				else: 
					fout.write(fdin[row+1][5]+","+fdin[row+1][6]+","+fdin[row+1][7]+","+fdin[row+1][8]+","+fdin[row+1][9]+","+fdin[row+1][10]+","
								+fdin[row+1][11]+","+fdin[row+1][12]+","+fdin[row+1][13]+","+fdin[row+1][14]+","+fdin[row+1][15]+","+fdin[row+1][16]+","+fdin[row+1][17]+","
								+fdin[row+2][5]+","+fdin[row+2][6]+","+fdin[row+2][7]+","+fdin[row+2][8]+","+fdin[row+2][9]+","+fdin[row+2][10]+","
								+fdin[row+2][11]+","+fdin[row+2][12]+","+fdin[row+2][13]+","+fdin[row+2][14]+","+fdin[row+2][15]+","+fdin[row+2][16]+","+fdin[row+2][17])
					pos=2
					shft=1
		else:
			pos=1
			fout.write(fdin[row][5]+","+fdin[row][6]+","+fdin[row][7]+","+fdin[row][8]+","+fdin[row][9]+","+fdin[row][10]+","
								+fdin[row][11]+","+fdin[row][12]+","+fdin[row][13]+","+fdin[row][14]+","+fdin[row][15]+","+fdin[row][16]+","+fdin[row][17])
		
		
		otcon=0
		tthcon=0
		othcon=0
		
		if row%100==0: print "      Searching in closed loans for concurrent matches..."
		for sow in range(plce,len(fdcl)):
			
			if fdin[row+shft][0]==fdcl[sow][0]:
				plce=sow
				if datetime.strptime(fdcl[sow][7],"%m/%d/%Y").year>datetime.strptime(nyear,"%Y").year: continue
				if fdin[row+shft][8]==fdcl[sow][7] and fdin[row+shft][13]==fdcl[sow][12] and fdin[row+shft][7]==fdcl[sow][23]: continue 
				
				if shft==0: edtm=nl1 
				if shft==1: edtm=nl2
				if shft==2: edtm=nl3
				
				if pos>1 and dup==1: 
					if fdin[row+1][8]==fdcl[sow][7] and fdin[row+1][13]==fdcl[sow][12] and fdin[row+1][7]==fdcl[sow][23]: continue
				if pos>1 and dup==2: 
					if fdin[row+2][8]==fdcl[sow][7] and fdin[row+2][13]==fdcl[sow][12] and fdin[row+2][7]==fdcl[sow][23]: continue
					if fdin[row+1][8]==fdcl[sow][7] and fdin[row+1][13]==fdcl[sow][12] and fdin[row+1][7]==fdcl[sow][23]: continue

					
				if findinclosingperiod(datetime.strptime(fdin[row+shft][8],"%m/%d/%Y"),edtm,datetime.strptime(fdcl[sow][9],"%m/%d/%Y"))==1:
					pos+=1
					if fdcl[sow][6]!="": purpc=productnamepurpose(fdcl[sow][6])
					else: purpc=""
					fout.write(","+fdcl[sow][6]+","+purpc+","+fdcl[sow][23]+","+fdcl[sow][7]+","+fdcl[sow][8]+","+fdcl[sow][9]+","+fdcl[sow][10]+","+fdcl[sow][11]+","
							+fdcl[sow][12]+","+fdcl[sow][13]+","+fdcl[sow][15]+","+fdcl[sow][18]+","+fdcl[sow][19])
							
		if row%100==0: print "      Searching in open loans for concurrent matches..."
		for pow in range(plce,len(fdop)):
			
			if fdin[row+shft][0]==fdop[pow][0]:
				plce=pow
				if datetime.strptime(fdop[pow][6],"%m/%d/%Y").year>datetime.strptime(nyear,"%Y").year: continue
				if fdin[row+shft][8]==fdop[pow][6] and fdin[row+shft][13]==fdop[pow][10] and fdin[row+shft][7]==fdop[pow][20]: continue 
				
				if shft==0: edtm=nl1 
				if shft==1: edtm=nl2
				if shft==2: edtm=nl3
				
				if pos>1 and dup==1: 
					if fdin[row+1][8]==fdop[pow][7] and fdin[row+1][13]==fdop[pow][12] and fdin[row+1][7]==fdop[pow][23]: continue
				if pos>1 and dup==2: 
					if fdin[row+2][8]==fdop[pow][7] and fdin[row+2][13]==fdop[pow][12] and fdin[row+2][7]==fdop[pow][23]: continue
					if fdin[row+1][8]==fdop[pow][7] and fdin[row+1][13]==fdop[pow][12] and fdin[row+1][7]==fdop[pow][23]: continue
				
				if findinperiodexclusive(datetime.strptime(fdin[row+shft][8],"%m/%d/%Y"),edtm,datetime.strptime(fdop[pow][6],"%m/%d/%Y"))==1:
					pos+=1
					
					if fdop[row][4]!="" and fdop[row][5]!="": 
						prod=productname(float(fdop[row][4]),float(fdop[row][5]))
						purp=productpurpose(float(fdop[row][4]),float(fdop[row][5]))
					else: 
						prod=""
						purp=""
					
					fout.write(","+prod+","+purp+","+fdop[row][20]+","+fdop[row][6]+","+fdop[row][7]+",,"+fdop[row][8]+","+fdop[row][9]+","
						+fdop[row][10]+",,"+fdop[row][12]+","+fdop[row][15]+","+fdop[row][16])
		
		if pos==1: 
			fout.write(",,,,,,,,,,,,,"
				+",,,,,,,,,,,,,\n")
		if pos==2: fout.write(",,,,,,,,,,,,,\n")
		if pos>=3: 
			print "Error, "+str(pos)+" concurrent loans"
			fout.write("\n")
		
		pos=0
		shft=0
		
	"YAYAYAYAY we are done!!!!!!!!"

	fin.close()
	fout.close()
	fcl.close()
	fop.close()