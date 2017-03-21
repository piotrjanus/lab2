import unittest
from pycalc import calc
from calcExceptions import *


class test_calc(unittest.TestCase):

	def setUp(self):
		self.c = calc()
		pass

	def test_adding_int_and_string(self):
		self.assertRaises(notIntNorFloat, self.c.add,"sd", 2)
	
	def test_division_by_zero(self):
		self.assertRaises(divisionByZero, self.c.divide, 2, 0)
	
	def test_division_by_string(self):
		self.assertRaises(notIntNorFloat, self.c.divide, 2, "ab")
	
	def test_ln_from_negative_number(self):
		self.assertRaises(negativeNumber, self.c.ln, -2)

	def test_derivative(self):
		def f(x):
			return x**3 + x**2
		self.c.der(f, 5, 1e-6)
		self.assertEqual(2,2)

if __name__ == '__main__':
	unittest.main()
