class Circle:

	Pi = 3.14
	
	def __init__(self):
		self.Radius = 0
		self.Area = 0.0
		self.Circumference = 0.0
		
	def Accept(self,Radius):
		self.Radius = Radius
		
	def CalculateArea(self):
		self.Area = Circle.Pi*self.Radius*self.Radius  #(pi * r * r)
		
	def CalculateCircumference(self):
		self.Circumference = 2*Circle.Pi*self.Radius #(2 * pi * r)
	
	def Display(self):
		print('Radius : {}'.format(self.Radius))
		print('Area : {} '.format(self.Area))
		print('Circumference : {} '.format(self.Circumference))
	
	
	
obj1 = Circle()
obj2 = Circle()

obj1.Accept(4)
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

print('--------------------------')

obj2.Accept(5)
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()
