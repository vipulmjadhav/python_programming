def addFactors(no):
	sum=0
	var=int(no/2)	

	for i in range (1,var+1):
		if(no%i == 0):
			sum = sum+i
	return sum

def AcceptNo():
	num = int(input())
	ret = addFactors(num)
	print(ret)

AcceptNo()
