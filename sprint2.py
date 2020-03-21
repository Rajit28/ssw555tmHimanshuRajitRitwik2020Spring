import datetime
import main_parser

# US07 less than 150 years old
# Death should be less than 150 years after birth and todays date should be less than 150 years after birth for all living
# Author: Himanshu Tanwar

def US07():
	file_ = 'gedcomTests/sprint2_test.ged'
	listPeople, listFam = main_parser.parse(file_)
	t = datetime.datetime.today()
	today = datetime.date(t.year, t.month, t.day)

	deathError = []
	peopleError = []

	for person in listPeople:
		if person.alive == False:
			limit = person.birthday.year + 150
			if person.death.year > limit:
				deathError.append(person)
		if today.year > person.birthday.year + 150 and person.alive == True:
			peopleError.append(person)

	return deathError, peopleError


# US08 Birth before marriage of parents
# Children should be born after marriage of parents. And no more than 9 months after their divorce
# Author: Himanshu Tanwar

def US08():
	file_ = 'gedcomTests/sprint2_test.ged'
	listPeople, listFam = main_parser.parse(file_)
	t = datetime.datetime.today()
	today = datetime.date(t.year, t.month, t.day)

	marriageError = []
	divorceError = []

	for fam in listFam:
		if len(fam.children) > 0:
			if fam.divorced != "NA":
				newYear = ( fam.divorced.month + 9 ) // 12
				newMonth = (fam.divorced.month + 9 ) % 12
				if newMonth == 0:
					newMonth = 12
				limit = datetime.date(fam.divorced.year + newYear, newMonth, fam.divorced.day)
				for child in fam.children:
					c = main_parser.findPerson(child, listPeople)
					if c.birthday > limit:
						divorceError.append([c,fam.divorced,fam.id])
			elif fam.married != "NA":
				for child in fam.children:
					c = main_parser.findPerson(child, listPeople)
					if c.birthday < fam.married:
						marriageError.append([c,fam.married, fam.id])
	
	return marriageError, divorceError 

#Author Ritvik Tiwari

def US12():
	file_ = 'gedcomTests/sprint2_test.ged'
	listPeople, listFam = main_parser.parse(file_)
	error=[]
	for fam in listFam:
        	if len(fam.children) > 0:
            		if fam.husbandId !='NA':
				husb= main_parser.findPerson(fam.husbandId, listPeople)
				for child in fam.children:
				    c = main_parser.findPerson(child, listPeople)
				    limit = husb.birthday.year +80
				    if c.birthday.year > limit:
						error.append([c,husb])
            		if fam.wifeId !='NA':
				wife=  main_parser.findPerson(fam.wifeId, listPeople)
				for child in fam.children:
			    		c = main_parser.findPerson(child, listPeople)
			    		limit = wife.birthday.year +60
			    		if c.birthday.year > limit:
						error.append([c,wife])
    	return error 

#Author Ritvik Tiwari

def US17():
    	file_ = 'gedcomTests/sprint2_test.ged'
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


						
			
