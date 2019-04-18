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
	
	if(exists):
		for dirname,subf,fileList in os.walk(path):
			for filen in fileList:
				path = os.path.join(dirname,filen)
				file_hash = hashfile(path)
				
				print("filename : "+path+" Checksum -> "+file_hash)
		
def main():
	if(len(argv) < 2 or len(argv)>2):
		print("ERROR : Invalid no of arguments \nType -h for help \nType -u for usage")
		exit()
	
	if(argv[1] == "-h"):
		print("HELP : This script displays checksum of files in directory")
		exit()	
	
	if(argv[1] == "-u"):
		print("USAGE : application.py  dir_name")
		exit()
	
	try:
		DisplayChecksum(argv[1])	
	
	except Exception as E:
		
		print("EXCEPTION : ",E)	
		
if __name__ == "__main__":
	
	main()
