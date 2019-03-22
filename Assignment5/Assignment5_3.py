from MarvellousString import strpermutations 

def callerFunc():
	a = input("Enter the string:")
	ret = strpermutations(a)
	
	for i in ret:
		print(''.join(i))
	
callerFunc() 
