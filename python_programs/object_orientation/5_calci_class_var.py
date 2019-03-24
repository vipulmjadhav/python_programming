class Calculator:

	no1 = 0
	no2 = 0
	ans = 0
		
	def __init__(self):
		pass
		
	def add(self):
		Calculator.ans = Calculator.no1+Calculator.no2
		
	def sub(self):
		Calculator.ans = Calculator.no1-Calculator.no2
	
	def mult(self):
		Calculator.ans = Calculator.no1*Calculator.no2
	
	def div(self):
		Calculator.ans = Calculator.no1/Calculator.no2
	
						
def main():
	
	Calculator.no1 = 10
	Calculator.no2 = 20
	
	obj = Calculator()
	
	obj.add()
	print(obj.ans)
	
	obj.sub()
	print(obj.ans)
	
	obj.mult()
	print(obj.ans)
	
	obj.div()
	print(obj.ans)
	
	
	
if __name__ == "__main__":
	main()
