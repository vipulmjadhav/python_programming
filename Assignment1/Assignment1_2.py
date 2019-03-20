def ChkNum(No):
	ans = No%2
	if(ans==0):
		print("Even Number")
	else:
		print("Odd Number")

def AcceptNum():
	Num = int(input())
	ChkNum(Num)

AcceptNum()
