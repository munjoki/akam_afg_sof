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
from fileyear import fileyear
from combineyear import combineyear
from loanquarterly import loanquarterly
from combineall import combineall

syear=ryear-1
tyear=ryear-2
fyear=ryear-3
ffyear=ryear-4
eyear=ryear-5

"Preparing open loan files across years from ",eyear,"-",syear
#fileyear(str(eyear),nopenloans,"Open")
#fileyear(str(ffyear),nopenloans,"Open")
#fileyear(str(fyear),nopenloans,"Open")
#fileyear(str(tyear),nopenloans,"Open")
#fileyear(str(syear),nopenloans,"Open")

"Preparing closed loan files across years from ",eyear,"-",syear
#fileyear(str(eyear),nclosedloans,"Closed")
#fileyear(str(ffyear),nclosedloans,"Closed")
#fileyear(str(fyear),nclosedloans,"Closed")
#fileyear(str(tyear),nclosedloans,"Closed")
#fileyear(str(syear),nclosedloans,"Closed")

"Combing open and closed loans within a year"
#combineyear(str(eyear))
#combineyear(str(ffyear))
#combineyear(str(fyear))
#combineyear(str(tyear))
#combineyear(str(syear))


"Preparing loans from ",ryear," for study of Q ",rquart

"First the open loans"
#fileyear(str(ryear),nopenloans,"Open")
"And skim open loans for Q ",rquart," only"
loanquarterly("Open",str(ryear),rquart)

"Now the closed loans"
#fileyear(str(ryear),nclosedloans,"Closed")
"And skim closed loans for Q ",rquart," only"
loanquarterly("Closed",str(ryear),rquart)

"Now combining without duplicates"
combineall(str(ryear),rquart)

"Side study looking only at clients in loan cycle 1 for Q ",rquart," of ",ryear
#combineyear(str(ryear))
print "Selecting only new clients in ",ryear

print "Please order your files by ascending (smallest to largest) customer number and then run loans2.py!\nGoodbye"
