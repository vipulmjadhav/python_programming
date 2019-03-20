def Pattern(no):
	for i in range(0,no):
		for j in range(i,no):
			print('* ',end=' ')
		print( )

def AcceptNo():
	num = int(input())
	Pattern(num)

AcceptNo()
