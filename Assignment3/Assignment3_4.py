def acceptElements():
	no = int(input("Enter no of elements:"))
	print("Enter Elements:")
	list = []
	freq = 0
	for i in range(0,no):
		num = int(input("num :"))
		list.append(num)
	key = int(input("enter element to search: "))
	
	for i in list:
		if(key==i):
			freq=freq+1
			
	return freq

def callerFunc():
	
	ret = acceptElements()
	print("count is : ",ret)

callerFunc()
