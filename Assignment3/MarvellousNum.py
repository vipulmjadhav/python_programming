def chkPrime(no):
	fact = 0
	if(no==1):
		return False
		
	for i in range(1,int(no//2+1)):
		if(no%i == 0):
			fact=fact+1
	if(fact>1):
		return False
	else:
		return True
