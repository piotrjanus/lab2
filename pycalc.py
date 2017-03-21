import abc
from scipy.misc import derivative
from math import log
from inspect import isfunction

from calcExceptions import *

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
		self.isIntOrFloat(x)
		self.isZero(precision)
		self.isNegative(precision)
		self.isFunction(function)
		return derivative(function, x, precision)
		pass
		
	def isFunction(self, f):
		if not isfunction(f):
			raise notFunction()

	def isNegative(self, x):
		if x < 0:
			raise negativeNumber()

	def isZero(self, x):
		if x == 0:
			raise divisionByZero()
	
	def isIntOrFloat(self, x):
		if not isinstance(x,(int, float)):
			raise notIntNorFloat()







