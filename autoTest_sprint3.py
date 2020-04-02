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

if __name__ == '__main__':
	main_parser.outputTable('gedcomTests/sprint1_test.ged')
	print("")
	unittest.main()