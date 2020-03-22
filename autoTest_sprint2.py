import unittest
import datetime
import main_parser
import sprint2
import autoTest_sprint1

# Unittest for US07
# Author: Himanshu Tanwar
class TestUS07(unittest.TestCase):

	def test_US07_individuals(self):
		deathError, peopleError = sprint2.US07()
		t = datetime.datetime.today()
		today = datetime.date(t.year, t.month, t.day)

		for person in deathError:
			print("ERROR: INDIVIDUAL: US07: " + person.id + " Name " + person.name + " DEATH "+ str(person.death) + " is greater than 150 years after birth: " + str(person.birthday))

		for person in peopleError:
			print("ERROR: INDIVIDUAL: US07: " + person.id + " Name " + person.name + " BIRTHDAY "+ str(person.birthday) + " is greater than 150 years")

		self.assertTrue(len(deathError) == 0 and len(peopleError) == 0, "US07: All DAYS are correct and are not greater than 150 years!")

# Unittest for US08
# Author: Himanshu Tanwar
class TestUS08(unittest.TestCase):

	def test_US08_individuals(self):
		marriageError, divorceError = sprint2.US08()

		for person in marriageError:
			print("ERROR: INDIVIDUAL: US08: " + person[0].id + " Name " + person[0].name + " born BEFORE marriage date of FAMILY: "+ person[2] + " : " + str(person[1]))

		for person in divorceError:
			print("ERROR: INDIVIDUAL: US08: " + person[0].id + " Name " + person[0].name + " born 9 months AFTER divorce date of FAMILY: " + person[2] + " : " + str(person[1]))

		self.assertTrue(len(marriageError) == 0 and len(divorceError) == 0, "US08: All BIRTHS are correct and occur correctly for parents Marriage/Divorce dates!")

# Unittest for US11
# Author: Ritvik Tiwari
class TestUS11(unittest.TestCase):
	def test_US11_individuals(self):
		bigamyError = sprint2.US11()
		for person in bigamyError:
			print("ERROR: INDIVIDUAL: US11: " + person.id + " Name " + person.name + " BIGAMY error, married to more than 1 person at the same time")
		self.assertTrue(len(bigamyError) == 0, "US11: Completed")

# Unittest for US12
# Author: Ritvik Tiwari
class TestUS12(unittest.TestCase):
	def test_US12_individuals(self):
		ageError = sprint2.US12()
		for person in ageError:
			if person[1].gender =="M":
				print("ERROR: INDIVIDUAL: US12: " + person[1].id + " Name " + person[1].name + " is more than 80 years older than the child " + person[0].id + ": Father's birthday "+ str(person[1].birthday)+", Child's birthday " +str(person[0].birthday))
			else:
				print("ERROR: INDIVIDUAL: US12: " + person[1].id + " Name " + person[1].name + " is more than 60 years older than the child " + person[0].id + ": Mother's birthday "+ str(person[1].birthday)+", Child's birthday " +str(person[0].birthday))
		self.assertTrue(len(ageError) == 0, "US12: Completed")


# Unittest for US17
# Author: Ritvik Tiwari
# class TestUS17(unittest.TestCase):

# 	def test_US17_individuals(self):
# 		Error = sprint2.US17()
# 		for person in ageError:
# 			if person[1].gender =="M":
# 				print("ERROR: INDIVIDUAL: US17: " + person[0].id + " Name " + person[0].name + "is married to his child " + person[1].id)
# 			else:
# 				print("ERROR: INDIVIDUAL: US17: " + person[0].id + " Name " + person[0].name + "is married to her child " + person[1].id)
# 		self.assertTrue(len(Error) == 0, "US17: Completed")
		
	
# Unittest for US09
# Author: Rajit Gohel
class TestUS09(unittest.TestCase):

	def test_US09_individuals(self):
		peopleError = sprint2.US09()

		for person in peopleError:
			print("ERROR: INDIVIDUAL: US09: " + person.id + " Name " + person.name + " is born on " + str(person.birthday)+ " which is after death of mother or after 9 months after death of father")

		self.assertTrue(len(peopleError) == 0, "US09: Completed")

# Unittest for US10
# Author: Rajit Gohel 
class TestUS10(unittest.TestCase):

	def test_US10_individuals(self):
		marriageError = sprint2.US10()

		for person in marriageError:
			print("ERROR: INDIVIDUAL: US10: " + person.id + " Name " + person.name + " is less than 14 years of age before marriage on  "+str(person.marriage))


		self.assertTrue(len(marriageError) == 0 , "US10: Completed")	

		
if __name__ == '__main__':
	main_parser.outputTable('gedcomTests/sprint1_test.ged')
	print("")
	unittest.main()
