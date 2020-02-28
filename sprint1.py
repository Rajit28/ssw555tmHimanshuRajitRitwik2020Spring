import datetime
import main_parser

# US01 dates before current date
# make sure dates are before current date
# Author: Himanshu Tanwar
def US01():
	file_ = 'gedcomTests/us01_test.ged'
	listPeople, listFam = main_parser.parse(file_)
	t = datetime.datetime.today()
	today = datetime.date(t.year, t.month, t.day)
	peopleErrors = []
	famErrors = []
	for person in listPeople:
		if person.birthday > today:
			peopleErrors.append(person)
		elif person.death != 'NA' and person.death > today:
			peopleErrors.append(person)

	for fam in listFam:
		if fam.married != 'NA' and fam.married > today:
			famErrors.append(fam)
		elif fam.divorced != 'NA' and fam.divorced > today:
			famErrors.append(fam)

	return peopleErrors, famErrors

# US02 birth before marriage 
# make sure the each birthday is before marriage of an individual 
# Author: Himanshu Tanwar
def US02():
	file_ = 'gedcomTests/us02_test.ged'
	listPeople, listFam = main_parser.parse(file_)
	peopleErrors = []

	for fam in listFam:
		if fam.husbandId != 'NA':
			husb = main_parser.findPerson(fam.husbandId, listPeople)
			if fam.married != 'NA' and husb.birthday > fam.married:
				husb.marriage = fam.married
				peopleErrors.append(husb)
		if fam.wifeId != 'NA':
			wife = main_parser.findPerson(fam.wifeId, listPeople)
			if fam.married != 'NA' and wife.birthday > fam.married:
				wife.marriage = fam.married
				peopleErrors.append(wife)
	return peopleErrors