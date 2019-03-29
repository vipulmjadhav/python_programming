class Demo:
	value = 100
	
	def __init__(self,no1,no2):
		self.no1 = no1
		self.no2 = no2
	
	def fun(self):
		print('--------Inside fun method------')
		print(self.no1)
		print(self.no2)
		#print('class var : {}'.format(Demo.value))
		
	def gun(self):
		print('--------Inside gun method------')
		print(self.no1)
		print(self.no2)
		#print('class var : {}'.format(Demo.value))

obj1 = Demo(11,21)
obj2 = Demo(51,201)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()

#print('-----------class variable------------')
#Demo.value

		
