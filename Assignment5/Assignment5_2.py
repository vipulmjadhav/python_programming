from MarvellousString import retWords
	
def callerFunc():
	string = str(input("Enter String to count words : "))
	ret = retWords(string)
	print("Output: {}".format(ret))	
	
callerFunc()
