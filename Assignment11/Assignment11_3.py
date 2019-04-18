from sys import *
import os
import hashlib

def hashfile(path,blocksize = 1024):
	fd = open(path,'rb')
	hasher = hashlib.md5()
	buf = fd.read(blocksize)
	
	while(len(buf)>0):
		hasher.update(buf)
		buf = fd.read(blocksize)
		
	fd.close()
	return hasher.hexdigest()
		
	
def DisplayChecksum(path):
	
	flag = os.path.isabs(path)
	
	if(flag==False):		
		path = os.path.abspath(path)
			
	exists = os.path.isdir(path)
	
	dups = {}
	
	if(exists):
		for dirname,subf,fileList in os.walk(path):
			for filen in fileList:
				path = os.path.join(dirname,filen)
				file_hash = hashfile(path)
				
				if(file_hash in dups):
					dups[file_hash].append(path)
				
				else:
					dups[file_hash] = [path]
		return dups	

def printDuplicates(dict1):
	results = list(filter(lambda x:len(x)>1 , dict1.values()))
	values = {}
	
	if(len(results)>0):
		print("duplicates found removing...")
		
		fd = open('log.txt','w')
		
		icnt=0
		for result in results:
			for subresult in result:
				icnt+=1
				if(icnt>=2):
					os.remove(subresult)
					fd.write('removed '+subresult+'\n')
			icnt=0	
					
	else:
		print("No Duplicates found")			
def main():
	if(len(argv) < 2 or len(argv)>2):
		print("ERROR : Invalid no of arguments \nType -h for help \nType -u for usage")
		exit()
	
	if(argv[1] == "-h"):
		print("HELP : This script deletes the files with same checksum and writes the removed file names into log")
		exit()	
	if(argv[1] == "-u"):
	
		print("USAGE : application.py  dir_name")
		exit()
	
	try:
		ret = {}	
		ret = DisplayChecksum(argv[1])
		printDuplicates(ret)	
	
	except Exception as E:
		
		print("EXCEPTION : ",E)	
		
if __name__ == "__main__":
	
	main()
