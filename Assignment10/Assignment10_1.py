import os
from sys import *

def func(dirname,ext):
	
	bool = os.path.isabs(dirname)
	if(bool == False):
		path = os.path.abspath(dirname)
		#print(path)
	
	exists = os.path.isdir(dirname)
	cnt=0
	
	if exists:
		for folder,subfolder,fname in os.walk(dirname):
			pass
			
			for subf in subfolder:
				pass
			
			for filen in fname:
				if(filen.endswith(argv[2])):
					print("file inside : "+folder+" is : "+filen)
					cnt = cnt+1
	if(cnt==0):
		print(argv[2]+" extension files doesn't exist in the folder"+dirname)		                
	
	
def main():
	if(len(argv) != 3):
		print("ERROR : Invalid no of arguments\n")
		print("enter -h as argv[1] for help\n")
	
	if(argv[1]=='-h'):
		print("HELP : The script shows all the files of extension given in argv[1]")
	
	if(argv[1]=='-u'):
		print("USAGE : Application_name.py dir_name extention")

	if((len(argv)) <1 or len(argv)>3):
		print("ERROR : Invalid No of Arguments!!")

	try:
		func(argv[1],argv[2])
		
	except Exception as E:
		print("Exception found : ",E)
			
if __name__ == "__main__":
	main()
