class BankAccount:
	
	ROI = 10.5
	
	def __init__(self,name,amount):
		self.name = name
		self.amount = amount
	
	def Deposit(self,amount):
		self.amount = self.amount + amount
				
	def Withdraw(self,amount):
		self.amount = self.amount - amount
		
	def CalculateIntrest(self):
		return (self.amount*BankAccount.ROI*1)//100
		
	def Display(self):
		print('name : ',self.name)
		print('amount : ',self.amount)
	
	
obj1 = BankAccount('vipul jadhav',1000)

obj1.Deposit(500)
obj1.Withdraw(300)
obj1.Display()	
print('Intrest : ',obj1.CalculateIntrest())

print('-------------------------------------')

obj2 = BankAccount('amol magar',2000)
obj2.Deposit(500)
obj2.Withdraw(300)
obj2.Display()	
print('Intrest : ',obj2.CalculateIntrest())
	
		
		
	
