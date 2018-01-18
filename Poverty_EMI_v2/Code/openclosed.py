import inspect,os,csv,sys
from productdecode import productnamepurpose,productname,productpurpose

def outopen(row,sow,fppi,fopen,fout):
    purp=productnamepurpose(fopen[sow][6])
    csv.writer(fout).writerow(fppi[row]+[fopen[sow][2],fopen[sow][3],fopen[sow][6],purp])

def outclosed(row,sow,fppi,fclosed,fout):
    prod=productname(float(fclosed[sow][0]),float(fclosed[sow][1]))
    purp=productpurpose(float(fclosed[sow][0]),float(fclosed[sow][1]))
    csv.writer(fout).writerow(fppi[row]+[fclosed[sow][6],fclosed[sow][5],prod,purp])
