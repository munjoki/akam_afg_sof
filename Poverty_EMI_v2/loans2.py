import inspect,os,csv,sys

##############################################
######Set Parameters for Your Analysis!!######
##############################################

#1. Year for the study
ryear=2017
#2. Quarter for further analysis (0 means the whole year)
rquart=1
#3. The directory where you saved the Loans folder
mydir="C:\Data\julia.gray\Documents\SPI_Tool_Afg\SPI_Analysis\Loans"
#4. Name of the file with the open loan records including loan cycle
nopenloans="Open_Loans_as_of_Jun_2017_clean"
#5. Name of the file with the closed loan records including loan cycle
nclosedloans="Closed_Loans_Closed_Date_as_of_Jun_2017"

##############################################
##############################################
##############################################

os.chdir(mydir)
sdir=os.getcwd()+"/Code/"
sys.path.append(sdir)
from loannew import loannew
from incomecalc import incomecalc
from incomecomp import incomecomp

syear=ryear-1
tyear=ryear-2
fyear=ryear-3
ffyear=ryear-4
eyear=ryear-5

# print "Selecting only new clients in ",ryear
# #loannew(str(ryear),rquart)

"Finding concurrent loans for  ",ryear," in Q",rquart
incomecalc(str(ryear),nopenloans,nclosedloans,rquart)

# "Finding concurrent loans for  ",eyear
# incomecalc(str(eyear),nopenloans,nclosedloans,"")

# "Finding concurrent loans for  ",fyear
# incomecalc(str(fyear),nopenloans,nclosedloans,"")

# "Finding concurrent loans for  ",ffyear
# incomecalc(str(ffyear),nopenloans,nclosedloans,"")

# "Finding concurrent loans for  ",tyear
# incomecalc(str(tyear),nopenloans,nclosedloans,"")

# "Finding concurrent loans for  ",syear
# incomecalc(str(syear),nopenloans,nclosedloans,"")


"Loans from ",ryear," matched to ",eyear
incomecomp(str(ryear),str(eyear),rquart)

"Loans from ",ryear," matched to ",fyear
incomecomp(str(ryear),str(fyear),rquart)

"Loans from ",ryear," matched to ",ffyear
incomecomp(str(ryear),str(ffyear),rquart)

"Loans from ",ryear," matched to ",tyear
incomecomp(str(ryear),str(tyear),rquart)

"Loans from ",ryear," matched to ",syear
incomecomp(str(ryear),str(syear),rquart)


