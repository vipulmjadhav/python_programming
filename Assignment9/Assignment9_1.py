import os

fname = input("Enter file name to check : ")

boolval = os.path.isfile(fname)

if(boolval):
	print("file exists!!!")
else:
	print("file does not exists!!!")

