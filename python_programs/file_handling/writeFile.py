file = open('demo.txt','r+')

file.write('program for writinng in file')

for i in file:
	print(i)

file.close()
