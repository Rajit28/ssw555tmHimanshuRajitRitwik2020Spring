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
            print("ERROR: FAMILIES: US19: "+ fam.husbandId + " Married to first cousin " + fam.wifeId)
        self.assertTrue(len(errorList) == 0 , "US19: No first cousins are married!")

# Unittest for US20
# Author: Himanshu Tanwar
class TestUS20(unittest.TestCase):

    def test_US20_individuals(self):
        errorList = sprint4.US20()
        for fam in errorList:
            print("ERROR: FAMILIES: US20: "+ fam.id + " Marriage is with Uncle/Aunt!")
        self.assertTrue(len(errorList) == 0 , "US20: Marriages are correct and no one is married to an Aunt or Uncle!")


if __name__ == '__main__':
	main_parser.outputTable('gedcomTests/main_test.ged')
	print("")
	unittest.main()