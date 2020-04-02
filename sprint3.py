import datetime
import main_parser

# US13 Sibling spacing
# Siblings should be born more than 8 months apart or less than 2 days apart (for twins)
# Author: Himanshu Tanwar

def US13():
	file_ = 'gedcomTests/sprint1_test.ged'
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
	file_ = 'gedcomTests/sprint1_test.ged'
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
			


				


print(US13)
