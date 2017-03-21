import unittest
import mock

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

	def test_derivative_when_no_function_is_given(self):
		self.assertRaises(notFunction, self.c.der, 2, 2, 2)

	@mock.patch('pycalc.calc.der', return_value=1)
	def test_derivative_for_long_calculations(self, mock_der):
		def f(x):
			pass
		expected_value=1
		self.assertEqual(calc.der(f,0,0.001),expected_value)

if __name__ == '__main__':
	unittest.main()
