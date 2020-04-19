import unittest
import datetime
import main_parser
import sprint4

# Unittest for US19
# Author: Himanshu Tanwar
class TestUS19(unittest.TestCase):

    def test_US19_individuals(self):
        errorList = sprint4.US19()
        for fam in errorList:
            print("ERROR: FAMILY: US19: In Family id "+ fam.id + " Husband " + fam.husbandId + " Married to first cousin, Wife " +fam.wifeId)
        self.assertTrue(len(errorList) == 0 , "US19: No first cousins are married!")

# Unittest for US20
# Author: Himanshu Tanwar
class TestUS20(unittest.TestCase):

    def test_US20_individuals(self):
        errorList = sprint4.US20()
        for fam in errorList:
            print("ERROR: FAMILY: US20: "+ fam.id + " Marriage is between Aunt/Uncle and Niece/Nephew!")
        self.assertTrue(len(errorList) == 0 , "US20: Marriages are correct and no one is married to an Aunt or Uncle!")
	
# Author: Rajit Gohel
class TestUS21(unittest.TestCase):

    def test_US21_individuals(self):
        errorList = sprint4.US21()
        for err in errorList:
            print("ERROR: FAMILY: US21: Family id {} do not have correct genders assigned for Husband/Wife!".format(err.id))
        self.assertTrue(len(errorList) == 0 , "US21: User story Complete")

# Author: Rajit Gohel
class TestUS22(unittest.TestCase):

    def test_US22_individuals(self):
        indList, famlist = sprint4.US22()
        for err in indList:
            print("ERROR: INDIVIDUAL: US22: More than one person with id {}".format(err))
        for err in famlist:
            print("ERROR: FAMILY: US22: More than one family with id {}".format(err))
        self.assertTrue(len(indList) == 0 and len(famlist) == 0, "US22: User story Complete")

#Author Ritvik Tiwari
class TestUS23(unittest.TestCase):

    def test_US23_individuals(self):
        errorList = sprint4.US23()
        for err in errorList:
            print("ERROR: INDIVIDUAL: US23: More than one individual with birthday {} and name {}".format(err[0],err[1]))
        self.assertTrue(len(errorList) == 0 , "US23: User story Complete")

#Author Ritvik Tiwari
class TestUS24(unittest.TestCase):

    def test_US24_individuals(self):
        errorList = sprint4.US24()
        for err in errorList:
            print("ERROR: FAMILY: US24: More than one family with same Spouse {} and marriage date {}".format(err[0],err[1]))
        self.assertTrue(len(errorList) == 0 , "US24: User story complete ")


if __name__ == '__main__':
	main_parser.outputTable('gedcomTests/main_test.ged')
	print("")
	unittest.main()
