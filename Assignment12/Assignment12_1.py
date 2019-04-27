import psutil

def ProcInfo():
	
	listprocess = []
	
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs = ['pid','name','username'])
		
			listprocess.append(pinfo)
		
		except Exception as E:
			pass
		
	return listprocess
	

def main():
	
	listprocess = ProcInfo()

	for i in listprocess:
		print(i)

if __name__ == "__main__":
	main()
