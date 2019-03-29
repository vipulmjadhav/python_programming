class Arithmetic:
	
	def __init__(self):
		self.value1 = 0.0
		self.value2 = 0.0
		self.result = 0.0
		
	def Accept(self):
		self.value1 = float(input('Enter value 1 : '))
		self.value2 = float(input('Enter value 2 : '))
		
	def Addition(self):
		self.result = self.value1 + self.value2
		return self.result
		
	def Subtraction(self):
		self.result = self.value1 - self.value2
		return self.result
		
	def Multiplication(self):
		self.result = self.value1 * self.value2
		return self.result
		
	def Division(self):
		self.result = self.value1 // self.value2
		return self.result
		
	
obj1 = Arithmetic()
obj2 = Arithmetic()

obj1.Accept()

print('--------------------------')

print('Addition : ',obj1.Addition())

print('Subtraction : ',obj1.Subtraction())

print('Multiplication : ',obj1.Multiplication())

print('Division : ',obj1.Division())

print('--------------------------')

obj2.Accept()

print('--------------------------')

print('Addition : ',obj2.Addition())

print('Subtraction : ',obj2.Subtraction())

print('Multiplication : ',obj2.Multiplication())

print('Division : ',obj2.Division())

