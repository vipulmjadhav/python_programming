def Pattern(no):
	for i in range(1,no+1):
		for j in range(1,no+1):
			print(j,end=' ')
		print()



def AcceptNo():
	num = int(input())
	Pattern(num)

AcceptNo()
