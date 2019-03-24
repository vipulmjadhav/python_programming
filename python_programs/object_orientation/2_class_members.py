class Demo:
	
	i = 10              #class variables
	j = 20
	add = 0
	def __init__(self): #initialization
		self.c = 34 #instance variable	
		
	def fun(self):      #instance method
	
		print("Inside instance method")
		
		self.a = 1  
		self.b = 2
		self.add = self.a+self.b
		
		print("Addition is : ",self.add)
	
	@classmethod	
	def gun(cls):       #class method
		
		print("Inside class method")
		
		Demo.add = Demo.i+Demo.j   #class variables
		print("Addition : ",Demo.add)
	
	@staticmethod
	def sun():          #static method
		print("Inside Static method")
		pass

print("class variable : ",Demo.i)   #class var is accessible by everyone ie class member and objects
obj = Demo()
print("instance variable : ",obj.c) #instance var is accessible is every object of that class 

obj.fun()
Demo.gun()
Demo.sun()

