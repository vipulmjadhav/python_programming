def acceptElements():
	no = int(input("Enter no of elements:"))
	print("Enter Elements:")
	list = []
	min=99999999999999999999999999999
	for i in range(0,no):
		num = int(input("num :"))
		list.append(num)
	
	for i in list:
		if(i<min):
			min = i
			
	return min

def callerFunc():
	
	ret = acceptElements()
	print("Minimum no is : ",ret)

callerFunc()
