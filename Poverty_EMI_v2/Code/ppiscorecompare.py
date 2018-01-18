import inspect,os,csv,sys
from ppiscore import ppiscore
from finddups import newdups,olddups
from afgbranch import afgbranch

def ppiscorecompare(nyear,oyear):

    fdir=os.getcwd()+"/Data/"
    print "   Loading file from ",nyear
    fnew=open(fdir+"/PPI_Data_"+nyear+".csv","rU")
    frnew=csv.reader(fnew,delimiter=",")
    fdnew=list(frnew)
    print "   File loaded"

    print "   Loading file from ",oyear
    fold=open(fdir+"/PPI_Data_"+oyear+".csv","rU")
    frold=csv.reader(fold,delimiter=",")
    fdold=list(frold)
    print "   File loaded"

    fout=open(fdir+"/PPI_Compare_"+nyear+"_to_"+oyear+".csv","wb")
    print "   Writing file to ",fdir

    fout.write("CUSTOMER_CODE,BRANCH_CODE,BRANCH,GENDER,DOB,CLIENT_INCOME_SOURCE_1,CLIENT_INCOME_SOURCE_2,"
               +"JOB_SUPPORTED_BY_CLIENT_BUSINESS,SEASONAL_WORKERS_CLIENT_BUSINESS,HOME_GEOGRAPHIC_LOCATION,"
               +"INPUT_DATE_"+nyear+",PPI_SCORE_"+nyear+",INPUT_DATE_"+oyear+",PPI_SCORE_"+oyear+",PPI_SCORE_DIFF\n")

    print "   Searching ",len(fdnew)," clients from ",nyear," for matches in ",oyear

    lskip17=0
    plc16=1
    mtch17=0
    nmtchs=0
    
    for row in range(1,len(fdnew)):

        if row%100==0: print "      Searched ",row," of ",len(fdnew)-1," clients..."

            
        if lskip17>0:
            lskip17-=1
            continue
            
        out17,lskip17,bdevnt17=newdups(row,fdnew)
        if bdevnt17!=0:
            bdevnt17=0
            continue
        
        for sow in range(plc16,len(fdold)):

            if float(fdnew[out17][3])==float(fdold[sow][3]) and mtch17!=1:
                mtch17=1
               
                out16,lskip16,bdevnt16=olddups(sow,fdold)
                plc16=out16+lskip16
                if bdevnt16!=0:
                    bdevnt16=0
                    continue
                 
                if fdnew[out17][49]!="": pscore17=float(fdnew[out17][49])
                else: pscore17=ppiscore(fdnew[out17][39],fdnew[out17][40],fdnew[out17][41],fdnew[out17][42],fdnew[out17][43],fdnew[out17][44],fdnew[out17][45],fdnew[out17][46],fdnew[out17][47],fdnew[out17][48])

                if fdold[out16][49]!="": pscore16=float(fdold[out16][49])
                else: pscore16=ppiscore(fdold[out16][39],fdold[out16][40],fdold[out16][41],fdold[out16][42],fdold[out16][43],fdold[out16][44],fdold[out16][45],fdold[out16][46],fdold[out16][47],fdold[out16][48])

                if pscore17<0 or pscore16<0: continue
                nmtchs+=1
                scorediff=pscore17-pscore16

                branch=afgbranch(float(fdnew[out17][1]))

                fout.write(fdnew[out17][3]+","+fdnew[out17][1]+","+branch+","+fdnew[out17][12]+","+fdnew[out17][15]+","+fdnew[out17][21]+","
                          +fdnew[out17][22]+","+fdnew[out17][23]+","+fdnew[out17][24]+","+fdnew[out17][28]+","
                          +fdnew[out17][4]+","+str(pscore17)+","+fdold[out16][4]+","+str(pscore16)+","+str(scorediff)+"\n")
        
        mtch17=0
    print "   Finished finding matches between records from ",nyear," and ",oyear," with ",nmtchs," clients with records in both years!"
    fout.close()
    fnew.close()
    fold.close()
    
