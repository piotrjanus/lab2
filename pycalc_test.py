import unittest
from pycalc import calc


class test_calc(unittest.TestCase):
	def test_adding_int_string(self):
		c = calc()
		self.assertEqual(c.add(2,2),4)

if __name__ == '__main__':
	unittest.main()
