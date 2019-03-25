#inbuilt function min()...

import sys

print("Enter the count of numbers");
sz = int(input())

arr = list()

for i in range(sz):
	num = int(input("Number : "))
	arr.append(num)

minelement = sys.maxsize

for i in arr:
	if(i<minelement):
		minelement = i
	
print("Minimum without inbuilt function : ",minelement)	
print("Minimum using inbuilt function : ",min(arr))	
