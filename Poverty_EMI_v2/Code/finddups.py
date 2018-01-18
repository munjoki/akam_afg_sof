import inspect,os,csv,sys,time
from ppiscore import ppiscore
from compcust import compcust


def olddups(row,ffile):
    nskip=row
    lskip=0
    bdevnt=0
    
    if len(ffile)>row+1:
        if ffile[row][3]==ffile[row+1][3]:
            lskip=1
            if len(ffile)>row+2:
                if ffile[row][3]==ffile[row+2][3]:
                    lskip=2
                    date1 = time.strptime(ffile[row][4],"%m/%d/%y")
                    date2 = time.strptime(ffile[row+1][4],"%m/%d/%y")
                    date3 = time.strptime(ffile[row+2][4],"%m/%d/%y")

                    if date1<=date2 and date1<=date3:
                        nskip=row
                        if date1==date2:
                            if ppiscore(ffile[row][39],ffile[row][40],ffile[row][41],ffile[row][42],ffile[row][43],ffile[row][44],ffile[row][45],ffile[row][46],ffile[row][47],ffile[row][48])!=ppiscore(ffile[row+1][39],ffile[row+1][40],ffile[row+1][41],ffile[row+1][42],ffile[row+1][43],ffile[row+1][44],ffile[row+1][45],ffile[row+1][46],ffile[row+1][47],ffile[row+1][48]): bdevnt=1
                        if date1==date3:
                            if ppiscore(ffile[row][39],ffile[row][40],ffile[row][41],ffile[row][42],ffile[row][43],ffile[row][44],ffile[row][45],ffile[row][46],ffile[row][47],ffile[row][48])!=ppiscore(ffile[row+2][39],ffile[row+2][40],ffile[row+2][41],ffile[row+2][42],ffile[row+2][43],ffile[row+2][44],ffile[row+2][45],ffile[row+2][46],ffile[row+2][47],ffile[row+2][48]): bdevnt=1
                        
                    elif date2<date1 and date2<=date3:
                        nskip=row+1
                        if date2==date3:
                            if ppiscore(ffile[row+1][39],ffile[row+1][40],ffile[row+1][41],ffile[row+1][42],ffile[row+1][43],ffile[row+1][44],ffile[row+1][45],ffile[row+1][46],ffile[row+1][47],ffile[row+1][48])!=ppiscore(ffile[row+2][39],ffile[row+2][40],ffile[row+2][41],ffile[row+2][42],ffile[row+2][43],ffile[row+2][44],ffile[row+2][45],ffile[row+2][46],ffile[row+2][47],ffile[row+2][48]): bdevnt=1
                            
                    else: nskip=row+2
                    
                else:
                   date1 = time.strptime(ffile[row][4],"%m/%d/%y")
                   date2 = time.strptime(ffile[row+1][4],"%m/%d/%y")
                   if date1<=date2:
                       nskip=row
                       if date1==date2:
                           if ppiscore(ffile[row][39],ffile[row][40],ffile[row][41],ffile[row][42],ffile[row][43],ffile[row][44],ffile[row][45],ffile[row][46],ffile[row][47],ffile[row][48])!=ppiscore(ffile[row+1][39],ffile[row+1][40],ffile[row+1][41],ffile[row+1][42],ffile[row+1][43],ffile[row+1][44],ffile[row+1][45],ffile[row+1][46],ffile[row+1][47],ffile[row+1][48]): bdevnt=1
                   else: nskip=row+1
            else:
                date1 = time.strptime(ffile[row][4],"%m/%d/%y")
                date2 = time.strptime(ffile[row+1][4],"%m/%d/%y")
                if date1<=date2:
                    nskip=row
                    if date1==date2:
                        if ppiscore(ffile[row][39],ffile[row][40],ffile[row][41],ffile[row][42],ffile[row][43],ffile[row][44],ffile[row][45],ffile[row][46],ffile[row][47],ffile[row][48])!=ppiscore(ffile[row+1][39],ffile[row+1][40],ffile[row+1][41],ffile[row+1][42],ffile[row+1][43],ffile[row+1][44],ffile[row+1][45],ffile[row+1][46],ffile[row+1][47],ffile[row+1][48]): bdevnt=1
                else: nskip=row+1
        
    return nskip,lskip,bdevnt




def newdups(row,ffile):

    nskip=row
    lskip=0
    bdevnt=0
    
    if len(ffile)>row+1:
        if ffile[row][3]==ffile[row+1][3]:
            lskip=1
            if len(ffile)>row+2:
                if ffile[row][3]==ffile[row+2][3]:
                    lskip=2
                    date1 = time.strptime(ffile[row][4],"%m/%d/%y")
                    date2 = time.strptime(ffile[row+1][4],"%m/%d/%y")
                    date3 = time.strptime(ffile[row+2][4],"%m/%d/%y")                    
                    if date1>=date2 and date1>=date3:
                        nskip=row
                        if date1==date2:
                            if ppiscore(ffile[row][39],ffile[row][40],ffile[row][41],ffile[row][42],ffile[row][43],ffile[row][44],ffile[row][45],ffile[row][46],ffile[row][47],ffile[row][48])!=ppiscore(ffile[row+1][39],ffile[row+1][40],ffile[row+1][41],ffile[row+1][42],ffile[row+1][43],ffile[row+1][44],ffile[row+1][45],ffile[row+1][46],ffile[row+1][47],ffile[row+1][48]): bdevnt=1
                        if date1==date3:
                            if ppiscore(ffile[row][39],ffile[row][40],ffile[row][41],ffile[row][42],ffile[row][43],ffile[row][44],ffile[row][45],ffile[row][46],ffile[row][47],ffile[row][48])!=ppiscore(ffile[row+2][39],ffile[row+2][40],ffile[row+2][41],ffile[row+2][42],ffile[row+2][43],ffile[row+2][44],ffile[row+2][45],ffile[row+2][46],ffile[row+2][47],ffile[row+2][48]): bdevnt=1
                    elif date2>date1 and date2>=date3:
                        nskip=row+1
                        if date2==date3:
                            if ppiscore(ffile[row+1][39],ffile[row+1][40],ffile[row+1][41],ffile[row+1][42],ffile[row+1][43],ffile[row+1][44],ffile[row+1][45],ffile[row+1][46],ffile[row+1][47],ffile[row+1][48])!=ppiscore(ffile[row+2][39],ffile[row+2][40],ffile[row+2][41],ffile[row+2][42],ffile[row+2][43],ffile[row+2][44],ffile[row+2][45],ffile[row+2][46],ffile[row+2][47],ffile[row+2][48]): bdevnt=1
                    else: nskip=row+2
                    
                else:
                   date1 = time.strptime(ffile[row][4],"%m/%d/%y")
                   date2 = time.strptime(ffile[row+1][4],"%m/%d/%y")       
                   if date1>=date2:
                       nskip=row
                       if date1==date2:
                           if ppiscore(ffile[row][39],ffile[row][40],ffile[row][41],ffile[row][42],ffile[row][43],ffile[row][44],ffile[row][45],ffile[row][46],ffile[row][47],ffile[row][48])!=ppiscore(ffile[row+1][39],ffile[row+1][40],ffile[row+1][41],ffile[row+1][42],ffile[row+1][43],ffile[row+1][44],ffile[row+1][45],ffile[row+1][46],ffile[row+1][47],ffile[row+1][48]): bdevnt=1
                   else: nskip=row+1
            else:
                date1 = time.strptime(ffile[row][4],"%m/%d/%y")
                date2 = time.strptime(ffile[row+1][4],"%m/%d/%y")
                if date1>=date2:
                    nskip=row
                    if date1==date2:
                        if ppiscore(ffile[row][39],ffile[row][40],ffile[row][41],ffile[row][42],ffile[row][43],ffile[row][44],ffile[row][45],ffile[row][46],ffile[row][47],ffile[row][48])!=ppiscore(ffile[row+1][39],ffile[row+1][40],ffile[row+1][41],ffile[row+1][42],ffile[row+1][43],ffile[row+1][44],ffile[row+1][45],ffile[row+1][46],ffile[row+1][47],ffile[row+1][48]): bdevnt=1
                else: nskip=row+1
        
    return nskip,lskip,bdevnt

def loandups(sow,i,ffile,ntimes):
    nmtch=0
    for itr in range(0,ntimes):
        if len(ffile)>sow+itr:
            if compcust(float(ffile[sow][i]),float(ffile[sow+itr+1][i]))==1: nmtch+=1
            else: break
    return nmtch

