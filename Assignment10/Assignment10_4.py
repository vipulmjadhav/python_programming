import os
from sys import *

def func(dir1,dir2):
	
	bool = os.path.isabs(dir1)
	if(bool == False):
		path = os.path.abspath(dir1)
		#print(path)
	
	exists = os.path.isdir(dir1)
	
	check = os.path.isdir(dir2)
	
	if(check):
		print('ERROR : Directory already exists !!!')
		print('Exiting....')
		os.system('ls')
		exit()	
		
	os.system('mkdir '+dir2)
	
	if exists:
		for folder,subfolder,fname in os.walk(dir1):
			for subf in subfolder:
				pass
			
			for filen in fname:
				if(filen.endswith(argv[3])):
					modpath = os.path.abspath(os.path.dirname(dir1))
					newpath = os.path.dirname(os.path.relpath(filen))+folder
					filepath = modpath+"/"+newpath+"/"+filen 
					os.system('cp '+filepath+" "+dir2+"/")
					
		print("Successfully copied "+argv[3]+" files to "+argv[2]+" from "+argv[1])	
					
	
def main():
	if(len(argv) != 4):
		print("ERROR : Invalid no of arguments\n")
		print("enter -h as argv[1] for help\n")
	
	if(argv[1]=='-h'):
		print("HELP : The script copies all files from dir1 to dir2")
	
	if(argv[1]=='-u'):
		print("USAGE : Application_name.py dir_name dir_name2")

	if((len(argv)) <1 or len(argv)>4):
		print("ERROR : Invalid No of Arguments!!")

	try:
		func(argv[1],argv[2])
		
	except Exception as E:
		print("Exception found : ",E)
			
if __name__ == "__main__":
	main()
