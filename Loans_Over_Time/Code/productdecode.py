import inspect,os,csv

def productname(pcode,pscheme):
	#Loan
	if pcode==1:	
		if pscheme==1: pname="Individual Loan - USD"
		elif pscheme==2: pname="Housing Loan(Tameer) - USD"
		elif pscheme==3: pname="Agriculture / Live stock Loan - USD"
		elif pscheme==4: pname="WPCO LOAN - USD"
		elif pscheme==5: pname="PERSONAL LOAN - USD"
		elif pscheme==6: pname="STAFF LOAN - USD"
		elif pscheme==7: pname="Agriculture/Live Stock Loan-Declining(USD)"
		elif pscheme==31: pname="Individual Loan - AFA"
		elif pscheme==32: pname="Housing Loan(Tameer) AFA"
		elif pscheme==33: pname="Agriculture / Live stock Loan - AFA"
		elif pscheme==34: pname="WPCO LOAN - AFA"
		elif pscheme==35: pname="PERSONAL LOAN - AFA"
		elif pscheme==36: pname="STAFF LOAN - AFA"
		elif pscheme==37: pname="Staff Loan Misc 1"
		elif pscheme==38: pname="Staff Loan Misc 2"
		elif pscheme==39: pname="Staff Loan Housing 1"
		elif pscheme==40: pname="Staff Loan Housing 2"
		elif pscheme==41: pname="Rural Housing Improvement Loan"
		elif pscheme==42: pname="Agriculture/Live Stock Loan-Declining(AFG)"
		elif pscheme==43: pname="Universal Loans-MF -AFA- Flat"
		elif pscheme==44: pname="Universal Loans-MF -AFA- Declining"
		elif pscheme==45: pname="Universal Loans-MF -USD- Flat"
		elif pscheme==46: pname="Universal Loans-MF -USD- Declining"
		elif pscheme==47: pname="Karobar Loan-AFN-Declining"
		elif pscheme==48: pname="Karobar Loan-USD-Declining"
		elif pscheme==49: pname="Housing Tameer-AFN-Flat"
		elif pscheme==50: pname="Housing Tameer Loan-USD-Flat"
		elif pscheme==51: pname="Personal Loan2-AFN-Flat"
		elif pscheme==52: pname="Personal Loan2-USD-Flat"
		else: pname=""
	elif pcode==2:	
		if pscheme==31: pname="Group Lending Loan - AFA"
		elif pscheme==32: pname="Group Lending Loan Agriculture"
		else: pname=""
	elif pcode==3:
		if pscheme==1: pname="SME Short Term Loans - USD"
		elif pscheme==2: pname="SME Medium Term Loan - USD"
		elif pscheme==31: pname="SME Short Term Loans - AFA"
		elif pscheme==32: pname="SME Medium Term Loan - AFA"
		else: pname=""
	#Depo
	elif pcode==21:
		if pscheme==1: pname="CURRENT ACCOUNT - USD"
		elif pscheme==21: pname="CURRENT ACCOUNT - EUR"
		elif pscheme==31: pname="CURRENT ACCOUNT - AFG"
		else: pname=""
	elif pcode==22:
		if pscheme==1: pname="SAVING ACCOUNT - USD"
		elif pscheme==21: pname="SAVING ACCOUNT - EUR"
		elif pscheme==31: pname="SAVING ACCOUNT - AFA"
		else: pname=""
	elif pcode==24:
		if pscheme==1: pname="CALL DEPOSIT - USD"
		elif pscheme==31: pname="CALL DEPOSIT - AFA"
		else: pname=""
	elif pcode==25:
		if pscheme==1: pname="DRAW DOWN ACCOUNT - USD"
		elif pscheme==21: pname="DRAW DOWN ACCOUNT - EUR"
		elif pscheme==31: pname="DRAW DOWN ACCOUNT - AFA"
		else: pname=""
	elif pcode==28:
		if pscheme==1: pname="BUSINESS SAVING DEPOSIT -USD"
		elif pscheme==21: pname="BUSINESS SAVING DEPOSIT - EUR"
		elif pscheme==31: pname="BUSINESS SAVING DEPOSIT - AFG"
		else: pname=""
	#Cert
	elif pcode==23:
		if pscheme==1: pname="FIXED DEPOSIT-USD"
		elif pscheme==31: pname="FIXED DEPOSIT-AFG"
		elif pscheme==32: pname="Term Deposit From Private Resident Banks"
		else: pname=""
	#Treasury
	elif pcode==26:
		if pscheme==1: pname="Term placements - Commerz Bank (USD)"
		elif pscheme==2: pname="Term placements - UBS (USD)"
		elif pscheme==3: pname="Term placements - HBL NY (USD)"
		elif pscheme==4: pname="Term placements - Habib Bank UK (USD)"
		elif pscheme==7: pname="TERM PLACEMENTS WITH KABUL (USD)"
		elif pscheme==8: pname="Term Placement with HBL-KBL (EUR)"
		elif pscheme==21: pname="Term placements - Commerz Bank (EUR)"
		elif pscheme==22: pname="Term placements - Habib Bank UK (EUR)"
		elif pscheme==23: pname="Term Placement UBS - EUR"
		elif pscheme==31: pname="PLACEMENT CAPITAL NOTE - AFG-28 DAYS"
		elif pscheme==32: pname="PLACEMENT CAPITAL NOTE - AFG-182 DAYS"
		elif pscheme==33: pname="Term Placement HBL-KBL (AFG)"
		elif pscheme==34: pname="PLACEMENT CAPITAL NOTE - AFG-364 DAYS"
		elif pscheme==35: pname="Term Placement - USD"
		elif pscheme==43: pname="Placement"
		elif pscheme==44: pname="PLACEMENT CAPITAL NOTE - AFG-91 DAYS"
		else: pname=""
	else: pname=""
	return pname
	
def productpurpose(pcode,pscheme):
	if pcode==1:
		if pscheme==2 or pscheme==32 or pscheme==41 or pscheme==49 or pscheme==50:  ppurpose="Housing"
		elif pscheme==3 or pscheme==7 or pscheme==33 or pscheme==42: ppurpose="Agriculture"
		elif pscheme==5 or pscheme==35 or pscheme==51 or pscheme==52: ppurpose="Consumer"
		elif pscheme==1 or pscheme==31 or pscheme==43 or pscheme==44 or pscheme==45 or pscheme==46 or pscheme==47 or pscheme==48: ppurpose="Enterprise"
		elif pscheme==4 or pscheme==34: ppurpose="WPCO"
		elif pscheme==6 or pscheme==36 or pscheme==37 or pscheme==38 or pscheme==39 or pscheme==40: ppurpose="Staff"
		else: ppurpose=""
	elif pcode==2:
		if pscheme==31 or pscheme==32: ppurpose="Group"
		else: ppurpose=""
	elif pcode==3:
		if pscheme==1 or pscheme==2 or pscheme==31 or pscheme==32: ppurpose="SME"
		else: ppurpose=""
	else: ppurpose=""
	return ppurpose



def productnamepurpose(pname):
	if "staff" not in pname.lower():
		if "group" not in pname.lower():
			if "wpco" not in pname.lower(): 
				if "housing" in pname.lower(): pnpurpose="Housing"
				elif "agriculture" in pname.lower(): pnpurpose="Agriculture"
				elif "sme" in pname.lower(): pnpurpose="SME"
				elif "personal" in pname.lower(): pnpurpose="Consumer"
				elif "individual" in pname.lower() or "universal" in pname.lower() or "karobar" in pname.lower(): pnpurpose="Enterprise"
				else: pnpurpose="" 
			else: pnpurpose="WPCO"
		else: pnpurpose="Group"
	else: pnpurpose="Staff"
	return pnpurpose



