class notFunction(Exception):
	def __str__(self):
		return repr("not a function")

class notIntNorFloat(Exception):
	def __str__(self):
		return repr("not int nor float")

class divisionByZero(Exception):
	def __str__(self):
		return repr("division by zero!")

class negativeNumber(Exception):
	def __str__(self):
		return repr("negative number")
