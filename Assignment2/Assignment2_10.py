def addDigits(no):
	temp = no
	cnt=0	
	rem=0
	sum=0	
	while(temp!=0):
		rem=temp%10
		sum=sum+rem
		temp = temp//10
		cnt = cnt+1	
	return sum

	
def AcceptNo():
	num = int(input())
	ret = addDigits(num)
	print(ret)
AcceptNo()
