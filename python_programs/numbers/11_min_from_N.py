import sys
cnt = int(input("numbers to enter:"))

min = sys.maxsize
num = 0

for i in range(cnt):
	num = int(input("num : "))
	if(num<min):
		min = num

print("minimum is : ",min)	
			

