import inspect,os,csv,sys
from datetime import datetime,timedelta
from findintime import findinrange

def fileyear(pyear,fin,fout,ftype,frange):

    if fout=="": fout=fin

    frdir=os.getcwd()
    fwdir=os.getcwd()+"/Data/"

    print "      Loading file"
    fppi=open(frdir+"/"+fin+".csv","rU")
    frppi=csv.reader(fppi,delimiter=",")
    fdppi=list(frppi)
    print "      File loaded"

    fout=open(fwdir+"/"+fout+"_"+pyear+".csv","wb")
    print "      Writing file to ",fwdir
    
    print "      Searching ",len(fdppi)-1," clients for those in year "+pyear

    csv.writer(fout).writerow(fdppi[0])

    nclients=0
    
    for row in range(1,len(fdppi)):
        if row%1000==0: print "         Searched ",row," of ",len(fdppi)-1," clients..."
        if ftype=="ppi":
            if fdppi[row][5]==pyear:
                csv.writer(fout).writerow(fdppi[row])
                nclients+=1
        if ftype=="open":
            nyear=int(pyear)+1
            mtch1=findinrange(datetime.strptime(fdppi[row][2],"%m/%d/%y"),datetime.strptime(pyear,"%Y"),frange)
            mtch2=findinrange(datetime.strptime(fdppi[row][2],"%m/%d/%y"),datetime.strptime(str(nyear),"%Y"),frange)
            if datetime.strptime(fdppi[row][2],"%m/%d/%y").year==datetime.strptime(pyear,"%Y").year or mtch1==1 or mtch2==1:
                csv.writer(fout).writerow(fdppi[row])
                nclients+=1
        if ftype=="closed":
            nyear=int(pyear)+1
            mtch1=findinrange(datetime.strptime(fdppi[row][6],"%m/%d/%y"),datetime.strptime(pyear,"%Y"),frange)
            mtch2=findinrange(datetime.strptime(fdppi[row][6],"%m/%d/%y"),datetime.strptime(str(nyear),"%Y"),frange)
            if datetime.strptime(fdppi[row][6],"%m/%d/%y").year==datetime.strptime(pyear,"%Y").year or mtch1==1 or mtch2==1:
                csv.writer(fout).writerow(fdppi[row])
                nclients+=1

    print "      Finished finding ",fin," records from ",pyear," with ",nclients," clients found!"
    fout.close()
