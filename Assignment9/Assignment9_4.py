import sys

try:
	fd = open(sys.argv[1],mode = "r",encoding="UTF-8")

except FileNotFoundError:
	print("{} not present .".format(sys.argv[1]))
	sys.exit()	

		
txt = fd.read()

try:
	fd1 = open(sys.argv[2],mode = "r")

except FileNotFoundError:
	print("{} not present .".format(sys.argv[2]))
	fd.close()

		
bxt = fd1.read()
	
if(txt == bxt):
	print("content is same!!");
	print(txt)
else:
	print("Content is mismatch!!")
	
