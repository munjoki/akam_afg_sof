import inspect,os,csv

def afgbranch(bnum):
	if bnum==1: bname="Head Office"
	elif bnum==2: bname="Taimani"
	elif bnum==3: bname="Khairkhana"
	elif bnum==4: bname="Mandavi"
	elif bnum==5: bname="Kot-e-Sangi"
	elif bnum==6: bname="Pul-e-Khumry"
	elif bnum==7: bname="Mazar-e-Sharif I"
	elif bnum==8: bname="Mazar-e-Sharif II"
	elif bnum==9: bname="Kunduz"
	elif bnum==10: bname="Herat City I"
	elif bnum==11: bname="Herat City II"
	elif bnum==12: bname="Jalalabad"
	elif bnum==13: bname="Charikar"
	elif bnum==14: bname="Faizabad"
	elif bnum==15: bname="Shebergan"
	elif bnum==16: bname="Maimana"
	elif bnum==17: bname="Samangan"
	elif bnum==18: bname="Taloqan"
	elif bnum==19: bname="Balkh"
	elif bnum==20: bname="Sarepol"
	elif bnum==21: bname="Commercial"
	elif bnum==22: bname="Kishem"
	elif bnum==23: bname="Doshi"
	elif bnum==24: bname="Jirm"
	elif bnum==25: bname="Baharak"
	elif bnum==26: bname="Yamgan"
	elif bnum==27: bname="Bamyan City"
	elif bnum==28: bname="Yakawalang"
	elif bnum==29: bname="Panjab"
	elif bnum==30: bname="Waras"
	elif bnum==31: bname="Ishkashim"
	elif bnum==32: bname="Zebak"
	elif bnum==33: bname="Shugnan"
	elif bnum==34: bname="Darwaz"
	elif bnum==35: bname="Khulum"
	elif bnum==36: bname="Jabulsaraj"
	elif bnum==37: bname="Sholgara"
	elif bnum==38: bname="Aqcha"
	elif bnum==39: bname="Andkhoy"
	else: bname==""
	return bname 
