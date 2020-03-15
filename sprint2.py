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
						
			