import inspect,os,csv,sys
from findintime import findinrange
from openclosed import *
from datetime import datetime
from compcust import compcust

def loanmatch(fyear,oyear,fadd,fopen,fclosed,fswitch,frange):

    fdir=os.getcwd()+"/Data/"

    if fswitch.lower()=="open":
        fother="closed"
        fone=fopen
        ftwo=fclosed
    elif fswitch.lower()=="closed":
        fother="open"
        fone=fclosed
        ftwo=fopen
    else:
        print "   No preference selected; using default of searching open loans first..."
        fswitch="open"
        fother="closed"
        fone=fopen
        ftwo=fclosed


    print "      Loading PPI file with scores from ",fyear," matched to those of ",oyear
    if float(fyear)>float(oyear): fppi=open(fdir+"/"+"/PPI_Compare_"+fyear+"_to_"+oyear+fadd+".csv","rU")
    else: fppi=open(fdir+"/"+"/PPI_Compare_"+oyear+"_to_"+fyear+fadd+".csv","rU")
    frppi=csv.reader(fppi,delimiter=",")
    fdppi=list(frppi)
    print "      File loaded"

    print "      Loading preferred ",fswitch, " loan records from ",fyear," to match"
    fnone=open(fdir+"/"+fone+"_"+fyear+".csv","rU")
    frone=csv.reader(fnone,delimiter=",")
    fdone=list(frone)
    print "      File loaded"

    print "      Loading other ",fother," loan records from ",fyear," to also match"
    fntwo=open(fdir+"/"+ftwo+"_"+fyear+".csv","rU")
    frtwo=csv.reader(fntwo,delimiter=",")
    fdtwo=list(frtwo)
    print "      File loaded"

    if float(fyear)>float(oyear): fout=open(fdir+"/PPI_Compare_"+fyear+"_to_"+oyear+fadd+"_Match_Loan.csv","wb")
    else: fout=open(fdir+"/PPI_Compare_"+fyear+"_to_"+oyear+fadd+"_Match_Loan.csv","wb")
    print "      Writing file to ",fdir


    csv.writer(fout).writerow(fdppi[0]+["PPI_LOAN_DISB_"+fyear,"PPI_LOAN_CLOSED_"+fyear,"PPI_PROD_"+fyear,"PPI_PURP_"+fyear])
    
    print "      Searching ",len(fdppi)-1," clients for "+fyear+" loans"

    nclients=0
    mtch=0
    for row in range(1,len(fdppi)):
        if row%1000==0: print "         Searched ",row," of ",len(fdppi)-1," clients..."

        for sow in range(1,len(fdone)):
            if mtch!=1:
                if fswitch.lower()=="open": mtch=compcust(float(fdppi[row][0]),float(fdone[sow][0]))
                if fswitch.lower()=="closed": mtch=compcust(float(fdppi[row][0]),float(fdone[sow][3]))
                
                if mtch==1:

                    if fswitch.lower()=="open": ldate=datetime.strptime(fdone[sow][2],"%m/%d/%y")
                    if fswitch.lower()=="closed": ldate=datetime.strptime(fdone[sow][6],"%m/%d/%y")
                    if float(fyear)>float(oyear): pdate=datetime.strptime(fdppi[row][10],"%m/%d/%y")
                    if float(fyear)<float(oyear): pdate=datetime.strptime(fdppi[row][12],"%m/%d/%y")
                    
                    intime=findinrange(pdate,ldate,frange)

                    if intime==1:
                        if fswitch.lower()=="open": outopen(row,sow,fdppi,fdone,fout)
                        if fswitch.lower()=="closed": outclosed(row,sow,fdppi,fdone,fout)
                        nclients+=1
                    else: mtch=0


        if mtch!=1:
            
            for now in range(1,len(fdtwo)):
                if mtch!=1:
                    if fother.lower()=="open": mtch=compcust(float(fdppi[row][0]),float(fdtwo[now][0]))
                    if fother.lower()=="closed": mtch=compcust(float(fdppi[row][0]),float(fdtwo[now][3]))
                
                    if mtch==1:

                        if fother.lower()=="open": ldate=datetime.strptime(fdtwo[now][2],"%m/%d/%y")
                        if fother.lower()=="closed": ldate=datetime.strptime(fdtwo[now][6],"%m/%d/%y")
                        if float(fyear)>float(oyear): pdate=datetime.strptime(fdppi[row][10],"%m/%d/%y")
                        if float(fyear)<float(oyear): pdate=datetime.strptime(fdppi[row][12],"%m/%d/%y")

                        intime=findinrange(pdate,ldate,frange)

                        if intime==1:
                            if fother.lower()=="open": outopen(row,now,fdppi,fdtwo,fout)
                            if fother.lower()=="closed": outclosed(row,now,fdppi,fdtwo,fout)
                            nclients+=1
                        else: mtch=0
        if mtch!=1:
            csv.writer(fout).writerow(fdppi[row]+["","","",""])

        mtch=0

    print "   Finished finding matches from loan records from ",fyear," with ",nclients," out of ",len(fdppi)-1," clients with PPI records"
    fppi.close()
    fnone.close()
    fntwo.close()
    fout.close()
    
