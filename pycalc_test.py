import unittest
from pycalc import calc
from pycalc import notIntNotFloat


class test_calc(unittest.TestCase):

	def test_adding_int_and_string(self):
		c = calc()
		self.assertRaises(notIntNotFloat,c.add,"sd",2)
	
	def test_division_by_zero(self):
		pass

if __name__ == '__main__':
	unittest.main()
