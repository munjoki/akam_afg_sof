import inspect,os,csv,sys

##############################################
######Set Parameters for Your Analysis!!######
##############################################

#1. Year for the study
ryear=2017
#2. The directory where you saved the PPI_Score_Analysis folder
mydir="C:\Data\julia.gray\Documents\SPI_Tool_Afg\SPI_Analysis\Loans_Over_Time"
#3. Name of the file with the open loan records including loan cycle
nopenloans="Open_Loans_as_of_Jun_2017_clean"
#4. Name of the file with the closed loan records including loan cycle
nclosedloans="Closed_Loans_Closed_Date_as_of_Jun_2017"

##############################################
##############################################
##############################################


os.chdir(mydir)
sdir=os.getcwd()+"/Code/"
sys.path.append(sdir)
from fileyear import fileyear
from combineyear import combineyear
from loancomparetwo import loancomparetwo

syear=ryear-1
tyear=ryear-2
fyear=ryear-3
ffyear=ryear-4
eyear=ryear-5

"Preparing open loan files across years from ",eyear,"-",ryear
fileyear(str(eyear),nopenloans,"Open")
fileyear(str(ffyear),nopenloans,"Open")
fileyear(str(fyear),nopenloans,"Open")
fileyear(str(tyear),nopenloans,"Open")
fileyear(str(syear),nopenloans,"Open")
fileyear(str(ryear),nopenloans,"Open")

"Preparing closed loan files across years from ",eyear,"-",ryear
fileyear(str(eyear),nclosedloans,"Closed")
fileyear(str(ffyear),nclosedloans,"Closed")
fileyear(str(fyear),nclosedloans,"Closed")
fileyear(str(tyear),nclosedloans,"Closed")
fileyear(str(syear),nclosedloans,"Closed")
fileyear(str(ryear),nclosedloans,"Closed")

"Combing open and closed loans within a year"
combineyear(str(eyear))
combineyear(str(ffyear))
combineyear(str(fyear))
combineyear(str(tyear))
combineyear(str(syear))
combineyear(str(ryear))

"Compare two years ",ryear," to ",eyear
loancomparetwo(str(ryear),str(eyear))

"Compare two years ",ryear," to ",fyear
loancomparetwo(str(ryear),str(fyear))

"Compare two years ",ryear," to ",ffyear
loancomparetwo(str(ryear),str(ffyear))

"Compare two years ",ryear," to ",tyear
loancomparetwo(str(ryear),str(tyear))

"Compare two years ",ryear," to ",syear
loancomparetwo(str(ryear),str(syear))

print "Your study is now ready for analysis!\nGoodbye"
