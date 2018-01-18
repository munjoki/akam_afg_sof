import inspect,os,csv

def natpl(score):
	if score>=0 and score<=4: llhd=100.0
	elif score>=5 and score<=9: llhd=68.8
	elif score>=10 and score<=14: llhd=66.1
	elif score>=15 and score<=19: llhd=59.5
	elif score>=20 and score<=24: llhd=51.3
	elif score>=25 and score<=29: llhd=43.5
	elif score>=30 and score<=34: llhd=31.9
	elif score>=35 and score<=39: llhd=24.6
	elif score>=40 and score<=44: llhd=15.2
	elif score>=45 and score<=49: llhd=11.4
	elif score>=50 and score<=54: llhd=6.0
	elif score>=55 and score<=59: llhd=2.7
	elif score>=60 and score<=64: llhd=0.9
	elif score>=65 and score<=69: llhd=0.0
	elif score>=70 and score<=74: llhd=3.0
	elif score>=75 and score<=79: llhd=0.0
	elif score>=80 and score<=84: llhd=0.0
	elif score>=85 and score<=89: llhd=0.0
	elif score>=90 and score<=94: llhd=0.0
	elif score>=95 and score<=100: llhd=0.0
	else: llhd=-1.0
	return llhd


def natpl150(score):
	if score>=0 and score<=4: llhd=100.0
	elif score>=5 and score<=9: llhd=90.2
	elif score>=10 and score<=14: llhd=89.5
	elif score>=15 and score<=19: llhd=89.1
	elif score>=20 and score<=24: llhd=85.5
	elif score>=25 and score<=29: llhd=81.1
	elif score>=30 and score<=34: llhd=74.5
	elif score>=35 and score<=39: llhd=66.9
	elif score>=40 and score<=44: llhd=58.0
	elif score>=45 and score<=49: llhd=47.9
	elif score>=50 and score<=54: llhd=37.2
	elif score>=55 and score<=59: llhd=26.1
	elif score>=60 and score<=64: llhd=21.0
	elif score>=65 and score<=69: llhd=14.3
	elif score>=70 and score<=74: llhd=14.3
	elif score>=75 and score<=79: llhd=1.4
	elif score>=80 and score<=84: llhd=0.0
	elif score>=85 and score<=89: llhd=0.0
	elif score>=90 and score<=94: llhd=0.0
	elif score>=95 and score<=100: llhd=0.0
	else: llhd=-1.0
	return llhd
	

def natpl200(score):
	if score>=0 and score<=4: llhd=100.0
	elif score>=5 and score<=9: llhd=96.7
	elif score>=10 and score<=14: llhd=96.5
	elif score>=15 and score<=19: llhd=97.2
	elif score>=20 and score<=24: llhd=96.4
	elif score>=25 and score<=29: llhd=93.2
	elif score>=30 and score<=34: llhd=90.4
	elif score>=35 and score<=39: llhd=87.3
	elif score>=40 and score<=44: llhd=82.8
	elif score>=45 and score<=49: llhd=73.4
	elif score>=50 and score<=54: llhd=68.4
	elif score>=55 and score<=59: llhd=61.3
	elif score>=60 and score<=64: llhd=50.4
	elif score>=65 and score<=69: llhd=37.1
	elif score>=70 and score<=74: llhd=29.2
	elif score>=75 and score<=79: llhd=5.1
	elif score>=80 and score<=84: llhd=9.5
	elif score>=85 and score<=89: llhd=15.2
	elif score>=90 and score<=94: llhd=0.0
	elif score>=95 and score<=100: llhd=0.0
	else: llhd=-1.0
	return llhd
	
	
def usaidxtrm(score):
	if score>=0 and score<=4: llhd=100.0
	elif score>=5 and score<=9: llhd=44.4
	elif score>=10 and score<=14: llhd=39.2
	elif score>=15 and score<=19: llhd=35.2
	elif score>=20 and score<=24: llhd=28.8
	elif score>=25 and score<=29: llhd=20.0
	elif score>=30 and score<=34: llhd=13.6
	elif score>=35 and score<=39: llhd=7.9
	elif score>=40 and score<=44: llhd=4.5
	elif score>=45 and score<=49: llhd=4.2
	elif score>=50 and score<=54: llhd=2.6
	elif score>=55 and score<=59: llhd=0.5
	elif score>=60 and score<=64: llhd=0.5
	elif score>=65 and score<=69: llhd=0.0
	elif score>=70 and score<=74: llhd=0.0
	elif score>=75 and score<=79: llhd=0.0
	elif score>=80 and score<=84: llhd=0.0
	elif score>=85 and score<=89: llhd=0.0
	elif score>=90 and score<=94: llhd=0.0
	elif score>=95 and score<=100: llhd=0.0
	else: llhd=-1.0
	return llhd
	

def usaid125(score):
	if score>=0 and score<=4: llhd=100.0
	elif score>=5 and score<=9: llhd=22.2
	elif score>=10 and score<=14: llhd=19.5
	elif score>=15 and score<=19: llhd=13.6
	elif score>=20 and score<=24: llhd=10.7
	elif score>=25 and score<=29: llhd=6.8
	elif score>=30 and score<=34: llhd=3.6
	elif score>=35 and score<=39: llhd=1.8
	elif score>=40 and score<=44: llhd=0.5
	elif score>=45 and score<=49: llhd=0.5
	elif score>=50 and score<=54: llhd=0.9
	elif score>=55 and score<=59: llhd=0.0
	elif score>=60 and score<=64: llhd=0.0
	elif score>=65 and score<=69: llhd=0.0
	elif score>=70 and score<=74: llhd=0.0
	elif score>=75 and score<=79: llhd=0.0
	elif score>=80 and score<=84: llhd=0.0
	elif score>=85 and score<=89: llhd=0.0
	elif score>=90 and score<=94: llhd=0.0
	elif score>=95 and score<=100: llhd=0.0
	else: llhd=-1.0
	return llhd


def usaid250(score):
	if score>=0 and score<=4: llhd=100.0
	elif score>=5 and score<=9: llhd=79.0
	elif score>=10 and score<=14: llhd=82.8
	elif score>=15 and score<=19: llhd=79.9
	elif score>=20 and score<=24: llhd=72.5
	elif score>=25 and score<=29: llhd=68.6
	elif score>=30 and score<=34: llhd=57.3
	elif score>=35 and score<=39: llhd=46.9
	elif score>=40 and score<=44: llhd=35.8
	elif score>=45 and score<=49: llhd=26.2
	elif score>=50 and score<=54: llhd=19.3
	elif score>=55 and score<=59: llhd=12.9
	elif score>=60 and score<=64: llhd=7.1
	elif score>=65 and score<=69: llhd=6.0
	elif score>=70 and score<=74: llhd=6.7
	elif score>=75 and score<=79: llhd=1.4
	elif score>=80 and score<=84: llhd=0.0
	elif score>=85 and score<=89: llhd=0.0
	elif score>=90 and score<=94: llhd=0.0
	elif score>=95 and score<=100: llhd=0.0
	else: llhd=-1.0
	return llhd