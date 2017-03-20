import abc

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
		return x+y

	def divide(self, x, y):
		return x/y
	
	def ln(self, x, y):
		pass
