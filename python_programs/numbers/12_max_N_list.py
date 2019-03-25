#inbuilt function max...

import sys

print("Enter the count of numbers");
sz = int(input())

arr = list()

for i in range(sz):
	num = int(input("Number : "))
	arr.append(num)

maxelement = -sys.maxsize-1

for i in arr:
	if(i>maxelement):
		maxelement = i
	
print("Maximum without inbuilt function : ",maxelement)	
print("Maximum using inbuilt function : ",max(arr))	
