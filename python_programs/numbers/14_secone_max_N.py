import sys

print("Enter the count of numbers");
sz = int(input())

arr = list()

for i in range(sz):
	num = int(input("Number : "))
	arr.append(num)

maxelement = -sys.maxsize
secondmax = -sys.maxsize-1

for i in arr:
	if(i > maxelement):
		secondmax = maxelement
		maxelement = i
		
	elif(i > secondmax and i < maxelement):
		secondmax = i
	
	
print("Maximum : ",maxelement)
print("SecondMaximum : ",secondmax)	

