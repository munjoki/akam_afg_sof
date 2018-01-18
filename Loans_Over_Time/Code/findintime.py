from datetime import datetime,timedelta

def findinrange(pdate,ldate,i):
    if ldate>=(pdate - timedelta(days=i)) and ldate<=(pdate + timedelta(days=i)): mtch=1
    else: mtch=0
    return mtch

def findinperiod(sdate,edate,cdate):
    if cdate>=sdate and cdate<=edate: mtch=1
    else: mtch=0
    return mtch

def findinperiodexclusive(sdate,edate,cdate):
    if cdate>=sdate and cdate<edate: mtch=1
    else: mtch=0
    return mtch