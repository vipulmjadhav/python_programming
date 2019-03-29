class Numbers:
	
	def __init__(self,value):
		self.value = value
	
	def ChkPrime(self):
		
		fact=0
		
		if(self.value == 1):
			return False
			
		for i in range(1,int(self.value/2+1)):
			if(self.value % i == 0):
				fact+=1
			
		if(fact==1):
			return True
		else:
			return False
				
		
	def SumFactors(value):
		arr = list()
		arr = Numbers.Factors(value)
		return sum(arr)
	
	def Factors(value):
		
		arr = list()
		
		for i in range(1,int(value/2+1)):
			if(value % i == 0):
				arr.append(i)
		
		print('Factors : ',arr)
		return arr
			
	def ChkPerfect(self):
	
		ret = Numbers.SumFactors(self.value)
		
		if(self.value == ret):
			return True
		
		else:
			return False
		
					
			
obj1 = Numbers(6)

print('Number : ',6)
print('PRIME : ',obj1.ChkPrime())
print('PERFECT : ',obj1.ChkPerfect())
	
print('--------------------------------------')
obj2 = Numbers(13)

print('Number : ',13)
print('PRIME : ',obj2.ChkPrime())
print('PERFECT : ',obj2.ChkPerfect())

print('--------------------------------------')
obj1 = Numbers(56)

print('Number : ',56)
print('PRIME : ',obj1.ChkPrime())
print('PERFECT : ',obj1.ChkPerfect())
	
print('--------------------------------------')
obj2 = Numbers(67)

print('Number : ',67)
print('PRIME : ',obj2.ChkPrime())
print('PERFECT : ',obj2.ChkPerfect())
	
