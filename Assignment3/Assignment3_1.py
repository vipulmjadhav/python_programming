def acceptElements():
	no = int(input("Enter no of elements:"))
	print("Enter Elements:")
	list = []
	sum=0
	for i in range(0,no):
		num = int(input("num :"))
		list.append(num)
	
	for i in list:
		sum+=i	
	return sum

def callerFunc():
	
	ret = acceptElements()
	print("Addition is : ",ret)

callerFunc()
