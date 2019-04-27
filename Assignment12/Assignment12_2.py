import psutil
from sys import *

def ProcInfo(procname):
	
	listprocess = []
	
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs = ['pid','name','username'])	
			if(pinfo['name'] == procname ):
				listprocess.append(pinfo)
		
		except Exception as E:
			pass

	return listprocess
	

def main():
	
	if(len(argv)!=2):
		print('Invalid no of arguments')
		exit()
	
	if(argv[1]=='-h'):
		print('HELP : shows info of specific running process')
		exit()
	
	if(argv[1]=='-u'):
		print('USAGE : shows info of specific running process')
		exit()
	
	process = argv[1]
	
	listprocess = ProcInfo(process)
	
	print(listprocess)
	
if __name__ == "__main__":
	main()
