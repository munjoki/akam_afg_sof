import inspect,os,csv,sys
from datetime import datetime

def fileyear(pyear,fin,ftype):

	frdir=os.getcwd()
	fwdir=os.getcwd()+"/Data/"

	print "      Loading file"
	fppi=open(frdir+"/"+fin+".csv","rU")
	frppi=csv.reader(fppi,delimiter=",")
	fdppi=list(frppi)
	print "      File loaded"

	fout=open(fwdir+"/"+ftype+"_Loans_"+pyear+".csv","wb")
	print "      Writing file to ",fwdir

	print "      Searching ",len(fdppi)-1," clients for those in year "+pyear

	csv.writer(fout).writerow(fdppi[0])

	nclients=0

	for row in range(1,len(fdppi)):
		if row%10000==0: print "         Searched ",row," of ",len(fdppi)-1," clients..."
		if ftype.lower()=="open":
			if datetime.strptime(fdppi[row][6],"%m/%d/%Y").year==datetime.strptime(pyear,"%Y").year:
				csv.writer(fout).writerow(fdppi[row])
				nclients+=1
		if ftype.lower()=="closed":
			if datetime.strptime(fdppi[row][7],"%m/%d/%Y").year==datetime.strptime(pyear,"%Y").year:
				csv.writer(fout).writerow(fdppi[row])
				nclients+=1

	print "      Finished finding ",fin," records from ",pyear," with ",nclients," clients found!"
	fout.close()
	fppi.close()
