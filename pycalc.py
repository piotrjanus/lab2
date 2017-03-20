import abc
from math import log

class notIntNotFloat(Exception):
	def __str__(self):
		return repr("not int nor float")

class divisionByZero(Exception):
	def __str__(self):
		return repr("division by zero!")

class abstractCalc(object):
	__metaclass__  = abc.ABCMeta
	@abc.abstractmethod
	def add(self, x, y):
		pass

	@abc.abstractmethod
	def divide(self, x, y):
		pass

	@abc.abstractmethod
	def ln(self, x, y):
		pass
#TODO
#add derivative

class calc(abstractCalc):

	def add(self, x, y):
		self.isIntOrFloat(x)
		self.isIntOrFloat(y)
		return x+y

	def divide(self, x, y):
		self.isIntOrFloat(x)
		self.isIntOrFloat(y)
		return x/y
	
	def ln(self, x):
		return math.log(x)

	def isZero(self, x):
		if x == 0:
			raise divisionByZero()
	
	def isIntOrFloat(self, x):
		if not isinstance(x,(int, float)):
			raise notIntNotFloat()







