class Calculator:
	
	def __init__(self,num1,num2):
		self.no1 = num1
		self.no2 = num2
		self.ans = 0
	
	def add(self):
		self.ans = self.no1+self.no2
		
	def sub(self):
		self.ans = self.no1-self.no2
	
	def mult(self):
		self.ans = self.no1*self.no2
	
	def div(self):
		self.ans = self.no1/self.no2
	
			
	
			
def main():
	obj1 = Calculator(10,20)
	obj1.add()
	print(obj1.ans)
	
	obj2 = Calculator(10,20)
	obj2.sub()
	print(obj2.ans)
	
	obj3 = Calculator(10,20)
	obj3.mult()
	print(obj3.ans)
	
	obj4 = Calculator(10,20)
	obj4.div()
	print(obj4.ans)
	
	
	
if __name__ == "__main__":
	main()
