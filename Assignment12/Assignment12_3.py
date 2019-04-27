import psutil
import os
import time
from sys import *


def createProcessLog(dir_name):
	
	bool = os.path.isabs(dir_name)
	
	if(bool == False):
		dir_name = os.path.abspath(dir_name)
	
	print(dir_name)
		
	exists = os.path.isdir(dir_name)
	
	if(exists == False):
		try:
			os.mkdir(argv[1])
		except:
			pass

	seperator = "-"*80
	log_path = os.path.join(dir_name,"process%sLog"%(time.ctime()))
	fd = open(log_path,'w')
	fd.write(seperator+"\n")
	fd.write("Current Process Running log %sLog"%(time.ctime())+"\n")
	fd.write(seperator+"\n")
	
	listprocess = []
	
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs = ['pid','name','username'])
			pinfo['vms'] = proc.memory_info().vms/(1024*1024)
			
			listprocess.append(pinfo)
		
		except Exception as E:
			pass
		
	for i in listprocess:
		fd.write("%s\n"%i)
		
	

def main():
	if(len(argv) != 2):
		print("ERROR : Invalid no of arguments\n")
		print("enter -h as argv[1] for help\n")
		print("enter -u as argv[1] for usage\n")
		exit()
	
	if(argv[1]=='-h'):
		print("HELP : The script shows all the files of extension given in argv[1]")
		exit()
		
	if(argv[1]=='-u'):
		print("USAGE : Application_name.py dir_name extention")
		exit()
		
	if((len(argv)) <1 or len(argv)>3):
		print("ERROR : Invalid No of Arguments!!")

	try:
		createProcessLog(argv[1])
		
	except Exception as E:
		print("Exception found : ",E)
			
		
		
if __name__ == "__main__":
	main()
