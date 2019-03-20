def ChkPrime(no):
	var=int(no/2)
	div=0
	for i in range(1,var+1):
		if(no%i==0):
			div=div+1
	return div
				


def AcceptNo():
	num = int(input())
	ret = ChkPrime(num)
	if(ret == 1):
		print('It is Prime Number')
	else:
		print('It is Not Prime Number')
			
		

AcceptNo()
