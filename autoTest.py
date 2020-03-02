import unittest
import datetime
import main_parser
import sprint1

# Unittest for US01
# Author: Himanshu Tanwar
class TestUS01(unittest.TestCase):

	def test_US01_individuals(self):
		indDateErrors, famDateErrors = sprint1.US01()
		
		t = datetime.datetime.today()
		today = datetime.date(t.year, t.month, t.day)

		for person in indDateErrors:
			if person.birthday > today:
				print("ERROR: INDIVIDUAL: US01: " + person.id + " Name " + person.name + " BIRTHDAY is after today: "+ str(person.birthday))
			elif person.death != 'NA' and person.death > today:
				print("ERROR: INDIVIDUAL: US01: " + person.id + " Name " + person.name + " DEATHDAY is after today: "+ str(person.death))
		self.assertTrue(len(indDateErrors) == 0, "All individual dates are correct and do not happen after today!")

	def test_US01_families(self):
		indDateErrors, famDateErrors = sprint1.US01()
		t = datetime.datetime.today()
		today = datetime.date(t.year, t.month, t.day)

		for fam in famDateErrors:
			if fam.married != 'NA' and fam.married > today:
				print("ERROR: FAMILY: US01: " + fam.id + " MARRIAGE DATE is after today: "+ str(fam.married))
			elif fam.divorced != 'NA' and fam.divorced > today:
				print("ERROR: FAMILY: US01: " + fam.id + " DIVORCE DATE is after today: "+ str(fam.divorced))
		self.assertTrue(len(famDateErrors) == 0, "All families dates are correct and do not happen after today!")
	
# Unittest for US02
# Author: Himanshu Tanwar

class TestUS02(unittest.TestCase):
	
	def test_US02_individuals(self):
		indDateErrors = sprint1.US02()

		for person in indDateErrors:
			print("ERROR: INDIVIDUAL: US02: " + person.id + " Name " + person.name + " BIRTHDAY "+ str(person.birthday) + " is after MARRIAGE Date " + str(person.marriage))

		self.assertTrue(len(indDateErrors) == 0, "All BIRTHDAYS are correct and do not occur after MARRIAGE DATE!")

#Author : Ritvik Tiwari

class TestUS05(unittest.TestCase):
	
	def test_US05_individuals(self):
		indDateErrors = sprint1.US05()

		for person in indDateErrors:
			print("ERROR: INDIVIDUAL: US05: " + person.id + " Name " + person.name + " Death DAY "+ str(person.death) + " is before MARRIAGE Date " + str(person.marriage))

		self.assertTrue(len(indDateErrors) == 0, "All dates are correct and do not occur before MARRIAGE DATE!")

#Author: Ritvik Tiwari

class TestUS06(unittest.TestCase):
	
	def test_US06_individuals(self):
		indDateErrors = sprint1.US06()

		for person in indDateErrors:
			print("ERROR: INDIVIDUAL: US06: " + person.id + " Name " + person.name + " Divorce Day "+ str(person.divorce) + " is after death Date " + str(person.death))

		self.assertTrue(len(indDateErrors) == 0, "All dates are correct and do not occur before MARRIAGE DATE!")
#Author : Rajit Gohel

class TestUS04(unittest.TestCase):
    
    def test_US04_families(self):
        famDateErrors = sprint1.US04()

        for fam in famDateErrors:
            print("ERROR: FAMILY: US04: " + fam.id + " Divorce date: " + str(fam.divorced) + " occurs before Marriage date: " + str(fam.married))

        self.assertTrue(len(famDateErrors) == 0, "All dates are correct and do not occur before MARRIAGE DATE!")

#Author : Rajit Gohel
class TestUS03(unittest.TestCase):
    
    def test_US03_individuals(self):
        indDateErrors = sprint1.US03()

        for person in indDateErrors:
            print("ERROR: INDIVIDUAL: US03: " + person.id + " Name " + person.name + " BIRTHDAY "+ str(person.birthday) + " is after death Date " + str(person.death))

        self.assertTrue(len(indDateErrors) == 0, "All dates are correct and do not occur before MARRIAGE DATE!")

if __name__ == '__main__':
	main_parser.outputTable('gedcomTests/sprint1_test.ged')
	print("")
	unittest.main()
