def acceptElements():
	no = int(input("Enter no of elements:"))
	print("Enter Elements:")
	list = []
	max=0
	for i in range(0,no):
		num = int(input("num :"))
		list.append(num)
	
	for i in list:
		if(i>max):
			max = i
			
	return max

def callerFunc():
	
	ret = acceptElements()
	print("Maximum No is : ",ret)

callerFunc()
