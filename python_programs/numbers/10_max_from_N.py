import sys
cnt = int(input("numbers to enter:"))

max = -sys.maxsize-1
num = 0

for i in range(cnt):
	num = int(input("num : "))
	if(num>max):
		max = num

print("maximum is : ",max)	
			
