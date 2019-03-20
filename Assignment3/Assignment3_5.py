import MarvellousNum as mo

def ListPrime():
	no = int(input("Enter no of elements:"))
	print("Enter Elements:")
	list = []
	ret = 0
	sum=0

	
	for i in range(0,no):
		num = int(input("num :"))
		list.append(num)
	
	for i in list:
		ret = mo.chkPrime(i)
		if(ret == True):
			sum+=i
	return sum
		
def callerFunc():
	
	ret = ListPrime()
	print("sum of prime numbers:",ret)

callerFunc()
