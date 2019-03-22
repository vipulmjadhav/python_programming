from MarvellousString import removeChar

def callerFunc():
	string = str(input("Enter String to remove : "))
	pos = int(input("Enter position of character to remove:"))
	
	ret = removeChar(string,pos)
	print("Output: {}".format(ret))
	
callerFunc()
