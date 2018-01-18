import inspect,os,csv

def ppione(pansw):
	if pansw=="SEVEN_PLUS": ppi=0
	elif pansw=="FVE_SIX": ppi=4
	elif pansw=="FOUR": ppi=9
	elif pansw=="THREE": ppi=12
	elif pansw=="TWO": ppi=17
	elif pansw=="ONE": ppi=23
	elif pansw=="NONE": ppi=29
	else: ppi=-1
	return ppi
		
def ppitwo(pansw):
	if pansw=="NO_MALE_HEAD": ppi=0
	elif pansw=="NO_FEMALE_HEAD": ppi=5
	elif pansw=="NO": ppi=5
	elif pansw=="YES": ppi=11
	else: ppi=-1
	return ppi

def ppithree(pansw):
	if pansw=="TEMPORARY": ppi=0
	elif pansw=="HOUSE_SINGLE_FAMILY": ppi=3
	else: ppi=-1
	return ppi
	
def ppifour(pansw):
	if pansw=="ONE_TO_FOUR": ppi=0
	elif pansw=="FOVE_PLUS": ppi=4
	else: ppi=-1
	return ppi
	
def ppifive(pansw):
	if pansw=="NONE": ppi=0
	elif pansw=="OPEN_PIT": ppi=5
	elif pansw=="TRADITIONAL": ppi=6
	elif pansw=="IMPROVED": ppi=11
	else: ppi=-1
	return ppi
	
def ppisix(pansw):
	if pansw=="ANIMAL_DUNG": ppi=0
	elif pansw=="CROP_RESIDUE": ppi=4
	else: ppi=-1
	return ppi	
	
def ppiseven(pansw):
	if pansw=="NONE": ppi=0
	elif pansw=="ONE": ppi=1
	elif pansw=="TWO_PLUS": ppi=9
	else: ppi=-1
	return ppi
	
def ppieight(pansw):
	if pansw=="NO": ppi=0
	elif pansw=="YES": ppi=3
	else: ppi=-1
	return ppi
	
def ppinine(pansw):
	if pansw=="NO": ppi=0
	elif pansw=="MOTORCYCLE": ppi=12
	elif pansw=="CAR": ppi=22
	else: ppi=-1
	return ppi
	
def ppiten(pansw):
	if pansw=="NO": ppi=0
	elif pansw=="YES": ppi=4
	else: ppi=-1
	return ppi

def ppiscore(pone,ptwo,pthree,pfour,pfive,psix,pseven,peight,pnine,pten):
	score=ppione(pone)+ppitwo(ptwo)+ppithree(pthree)+ppifour(pfour)+ppifive(pfive)+ppisix(psix)+ppiseven(pseven)+ppieight(peight)+ppinine(pnine)+ppiten(pten)
	return score
