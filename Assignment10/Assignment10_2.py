import os
from sys import *
from os.path import join


def func(dirname,ext1,ext2):
	
	bool = os.path.isabs(dirname)
	if(bool == False):
		path = os.path.abspath(dirname)
		#print(path)
	
	exists = os.path.isdir(dirname)
	
	if exists:
		for folder,subfolder,fname in os.walk(dirname):
			pass
			
			for subf in subfolder:
				pass
			
			for filen in fname:
				if(filen.endswith(argv[2])):
					#path = os.path.relpath(filen)
					#pwd = os.getcwd()
					#print(pwd)
					#print(path)
					
					#print( filen )
					
					modpath = os.path.abspath(os.path.dirname(dirname))
					
					newpath = os.path.dirname(os.path.relpath(filen))+folder
					
					filepath = modpath+"/"+newpath+"/"+filen 
					#print(filepath)
					
					fl, ext = os.path.splitext(filepath)
				        
					os.system('mv '+filepath+" "+fl+argv[3])
					
				        #os.system('mv '+os.path.relpath(filen)+" "+fl+argv[3])
				        #print(os.path.relpath(filen))
					
					#os.rename(join(os.path.abspath(filen)), join(os.path.abspath(filen) + argv[3]))
				
					#fl, ext = os.path.splitext(filen)
					#os.rename(os.path.abspath(filen), os.path.abspath(fl + argv[3]))
				else:
					pass	
					
					#base = os.path.splitext(filen)[0]
					#os.rename(filen,base+argv[3])
					
					#for filename in os.listdir(path):

					 
	
def main():
	if(len(argv) != 4):
		print("ERROR : Invalid no of arguments\n")
		print("enter -h as argv[1] for help\n")
	
	if(argv[1]=='-h'):
		print("HELP : The script changes extenstion from argv[1] to argv[2]")
	
	if(argv[1]=='-u'):
		print("USAGE : Application_name.py dir_name extention1 ext2")

	if((len(argv)) <1 or len(argv)>4):
		print("ERROR : Invalid No of Arguments!!")

	try:
		func(argv[1],argv[2],argv[3])
		
	except Exception as E:
		print("Exception found : ",E)
			
if __name__ == "__main__":
	main()
	
