from MarvellousString import reverseString
	
def callerFunc():
	string = str(input("Enter String to Reverse : "))
	retStr = reverseString(string)
	print("Output is : {}".format(retStr))	
	
callerFunc()
