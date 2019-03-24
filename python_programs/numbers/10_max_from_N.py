cnt = int(input("numbers to enter:"))

max = 0
num = 0

for i in range(cnt):
	num = int(input("num : "))
	if(num>max):
		max = num

print("maximum is : ",max)	
			

