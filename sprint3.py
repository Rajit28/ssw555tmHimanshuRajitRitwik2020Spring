import datetime
import main_parser

# US13 Sibling spacing
# Siblings should be born more than 8 months apart or less than 2 days apart (for twins)
# Author: Himanshu Tanwar

def US13():
	file_ = 'gedcomTests/main_test.ged'
	listPeople, listFam = main_parser.parse(file_)
	
	errorList = []

	for fam in listFam:
		if len(fam.children) > 0:
			for i in range(len(fam.children)):
				c1 = main_parser.findPerson(fam.children[i], listPeople)
				newYear = ( c1.birthday.month + 8 ) // 12
				newMonth = (c1.birthday.month + 8 ) % 12
				if newMonth == 0:
					newMonth = 12
				limit1 = datetime.date(c1.birthday.year + newYear, newMonth, c1.birthday.day)
				limit2 = c1.birthday + datetime.timedelta(days=2)
				for j in range(len(fam.children)):
					if i != j:
						c2 = main_parser.findPerson(fam.children[j], listPeople)
						if c2.birthday < limit1 and c2.birthday > limit2:
							errorList.append([c1,c2])
	return errorList


# US14 Multiple Births
# No more than 5 siblings should be born at the same time
# Author: Himanshu Tanwar

def US14():
	file_ = 'gedcomTests/main_test.ged'
	listPeople, listFam = main_parser.parse(file_)

	siblingCountError = []

	count = 0
	for fam in listFam:
		if len(fam.children) >= 5:
			for i in range(len(fam.children)):
				c1 = main_parser.findPerson(fam.children[i], listPeople)
				for j in range(len(fam.children)):
					if i != j:
						c2 = main_parser.findPerson(fam.children[j], listPeople)
						if c1.birthday == c2.birthday:
							count += 1
				if count >= 5:
					siblingCountError.append(fam)
					break;
				else:
					count = 0
					continue;
	return siblingCountError
			

#Author Rajit Gohel
#US15

def US15():
	file_ = 'gedcomTests/main_test.ged'
	listPeople, listFam = main_parser.parse(file_)
    
	siberror=[]
	for fam in listFam:
		if len(fam.children) >=15:
			siberror.append(fam)
	
	return siberror

#Author Rajit Gohel
#US16

def US16():
	file_ = 'gedcomTests/main_test.ged'
	listPeople, listFam = main_parser.parse(file_)

	lastnameerror=[]
	for fam in listFam:
		if fam.husbandId!='NA':
			husb = main_parser.findPerson(fam.husbandId, listPeople)
			list_name_husb=husb.name.split()
			if len(fam.children)>0:
				for child in fam.children:
					c = main_parser.findPerson(child, listPeople)
					if c.gender=="M":
						list_child_name=c.name.split()
						if list_name_husb[-1] != list_child_name[-1]:
							#f= main_parser.findfam(fam.id,listFam)
							lastnameerror.append(fam)
	return lastnameerror

#Author Ritvik Tiwari
#US17 

def US17():
	file_ = 'gedcomTests/main_test.ged'
	listPeople, listFam = main_parser.parse(file_)
	error =[]

	for fam in listFam:
		if fam.husbandId !='NA' and fam.wifeId != 'NA':
			husb = main_parser.findPerson(fam.husbandId, listPeople)
			wife=  main_parser.findPerson(fam.wifeId, listPeople)
			if len(husb.children) > 0:
				for child in husb.children:
					c = main_parser.findPerson(child, listPeople)
					if wife == c :
						error.append([husb,c])
			if len(wife.children) > 0:
				for child in wife.children:
					c = main_parser.findPerson(child, listPeople)
					if husb == c :
						error.append([wife,c])
	return error

#Author Ritvik Tiwari
#US 18 

def US18():
	file_ = 'gedcomTests/main_test.ged'
	listPeople, listFam = main_parser.parse(file_)
	error=[]

	for fam in listFam:
		if fam.husbandId !='NA':
			husb = main_parser.findPerson(fam.husbandId, listPeople)
			if len(husb.children) > 0:
				for child in husb.children:
					c = main_parser.findPerson(child, listPeople)
					c.father=husb
		if fam.wifeId!='NA':
			wife=  main_parser.findPerson(fam.wifeId, listPeople)
			if len(wife.children) > 0:
				for child in wife.children:
					c = main_parser.findPerson(child, listPeople)
					c.mother=wife

	for fam in listFam:
		if fam.husbandId !='NA' and fam.wifeId!='NA' :
			husb = main_parser.findPerson(fam.husbandId, listPeople)
			wife=  main_parser.findPerson(fam.wifeId, listPeople)
			if wife.mother != ""  and wife.father != "" and husb.mother != "" and husb.father != "":
				if husb.mother == wife.mother or husb.father==wife.father:
					error.append([husb,wife])
	return error

