import inspect,os,csv,sys

##############################################
######Set Parameters for Your Analysis!!######
##############################################


#1. The directory where you saved the Deposit folder
mydir="C:\Data\julia.gray\Documents\SPI_Tool_Afg\SPI_Analysis\Deposit_Over_Time"

#2. Choose the quarter for the study
nqrt="Jun"
#Q1=Mar Q2=Jun Q3=Sept Q4=Dec

#3. Choose Year for the study
nyear=17

##############################################
##############################################
##############################################

os.chdir(mydir)
sdir=os.getcwd()+"/Code/"
sys.path.append(sdir)
from mtchdepo import mtchdepo

oyear=nyear-3

mtchdepo(str(nyear),str(oyear),nqrt)