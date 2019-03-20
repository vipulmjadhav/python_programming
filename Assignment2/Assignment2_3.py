
def Fact(no):
	ans = 1
	while(no>0):
		ans = ans*no
		no=no-1	
	return ans		


def AcceptNo():
	num = int(input())
	ret = Fact(num)	
	print(ret)

AcceptNo()


