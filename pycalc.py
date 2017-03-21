import abc
from math import log
from calcExceptions import *
from scipy.misc import derivative

class abstractCalc(object):
	__metaclass__  = abc.ABCMeta
	@abc.abstractmethod
	def add(self, x, y):
		pass

	@abc.abstractmethod
	def divide(self, x, y):
		pass

	@abc.abstractmethod
	def ln(self, x):
		pass

	@abc.abstractmethod
	def der(self, function, x, precision):
		pass
	

class calc(abstractCalc):

	def add(self, x, y):
		self.isIntOrFloat(x)
		self.isIntOrFloat(y)
		return x+y

	def divide(self, x, y):
		self.isIntOrFloat(x)
		self.isIntOrFloat(y)
		self.isZero(y)
		return x/y
	
	def ln(self, x):
		self.isIntOrFloat(x)
		self.isZero(x)
		self.isNegative(x)
		return math.log(x)

	def der(self, function, x, precision):
		pass
		

	def isNegative(self, x):
		if x < 0:
			raise negativeNumber()

	def isZero(self, x):
		if x == 0:
			raise divisionByZero()
	
	def isIntOrFloat(self, x):
		if not isinstance(x,(int, float)):
			raise notIntNorFloat()







