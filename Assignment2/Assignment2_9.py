def cntDigits(no):
	temp = no
	cnt=0		
	while(temp!=0):
		temp = temp//10
		cnt = cnt+1	
	return cnt

	
def AcceptNo():
	num = int(input())
	ret = cntDigits(num)
	print(ret)
AcceptNo()
