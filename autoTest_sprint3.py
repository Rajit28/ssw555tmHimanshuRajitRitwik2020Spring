import unittest
import datetime
import main_parser
import sprint3

# Unittest for US13
# Author: Himanshu Tanwar
class TestUS13(unittest.TestCase):

	def test_US13_individuals(self):
		errorList = sprint3.US13()
		
		for sib in errorList:
			print("ERROR: INDIVIDUAL: US13: "+ sib[0].name + " Birthday " +  str(sib[0].birthday) + " is within incorrect spacing with " + sib[1].name + " Birthday " + str(sib[1].birthday) )

		self.assertTrue(len(errorList) == 0 , "US13: All siblings birthday are correctly spaced!")

# Unittest for US14
# Author: Himanshu Tanwar		
class TestUS14(unittest.TestCase):

	def test_US14_individuals(self):
		siblingErrorList = sprint3.US14()

		for fam in siblingErrorList:
			print("ERROR: FAMILY: US14: "+ fam.id + " has 5 or more children with the same birthday!")
		
		self.assertTrue(len(siblingErrorList) == 0 , "US14: Number of children with same birthday is less than 5!")

# Unittest for US15
# Author: Rajit Gohel
		
class TestUS15(unittest.TestCase):

	def test_US15_individuals(self):
		Error = sprint3.US15()

		for family in Error:
			print("ERROR: FAMILY: US15: " + family.id + " has more than 15 sibilings")
		
		self.assertTrue(len(Error) == 0, "US15: Completed")	
			      
# Unittest for US16
# Author: Rajit Gohel			      
			      
class TestUS16(unittest.TestCase):

	def test_US16_individuals(self):
		Error = sprint3.US16()

		for family in Error:
			print("ERROR: FAMILY: US16: " + family.id + " has last name mismatch in males")
		
		self.assertTrue(len(Error) == 0, "US16: Completed")			      
		

		
# Unittest for US17
# Author: Ritvik Tiwari
class TestUS17(unittest.TestCase):

	def test_US17_individuals(self):
		Error = sprint3.US17()
		for person in Error:
			if person[1].gender =="M":
				print("ERROR: INDIVIDUAL: US17: " + person[0].id + " Name " + person[0].name + " is married to his child " + person[1].id)
			else:
				print("ERROR: INDIVIDUAL: US17: " + person[0].id + " Name " + person[0].name + " is married to her child " + person[1].id)
		self.assertTrue(len(Error) == 0, "US17: Completed")


# Unittest for US18
# Author: Ritvik Tiwari
class TestUS18(unittest.TestCase):

	def test_US18_individuals(self):
		Error = sprint3.US18()

		for person in Error:
			print("ERROR: INDIVIDUAL: US18: " + person[0].id + " Name " + person[0].name + " is married to sibling " + person[1].id)
		
		self.assertTrue(len(Error) == 0, "US18: Completed")


if __name__ == '__main__':
	main_parser.outputTable('gedcomTests/sprint1_test.ged')
	print("")
	unittest.main()
