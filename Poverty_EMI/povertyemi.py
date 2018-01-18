import inspect,os,csv,sys

##############################################
######Set Parameters for Your Analysis!!######
##############################################

#1. Year for the study
ryear="2017"
#2. Quarter for further analysis (0 means the whole year)
rquart=2
#3. The directory where you saved the PPI_Score_Analysis folder
mydir="C:\Data\julia.gray\Documents\SPI_Tool_Afg\SPI_Analysis\Poverty_EMI"
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
from openinfo import openinfo
from emiyearquart import emiyearquart
from closedyearquart import closedyearquart
from closedate import closedate

print "Hello!\nWelcome to your PPI Score analysis!\nWe will first separate out the different years of PPI score collection" 

print "    All open loans"
openinfo(nopenloans)

print "    from Q"+str(rquart)+" in "+ryear
emiyearquart(ryear,rquart)

print "    Matching closed loans close date"
closedate(nclosedloans)

print "    Closed loans from Q"+str(rquart)+" in "+ryear
closedyearquart(ryear,rquart,nclosedloans)

print "Your study is now ready for analysis!\nGoodbye"
