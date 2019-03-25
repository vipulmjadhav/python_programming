import sys

print("Enter the count of numbers");
sz = int(input())

arr = list()

for i in range(sz):
	num = int(input("Number : "))
	arr.append(num)

minelement = sys.maxsize-1
secondmin =  sys.maxsize

for i in arr:
	if(i < minelement):
		secondin = minelement
		minelement = i
		
	elif(i < secondmin and i > minelement):
		secondmin = i
	
	
print("Minimum : ",minelement)
print("SecondLastMinimum : ",secondmin)	

