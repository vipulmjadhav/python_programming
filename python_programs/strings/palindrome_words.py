#checks for the palindrome of words
# in->  abc def cba
# out-> abc


string = str(input("enter the string in words : "))

spl = string.split()

for i in spl:
	if(i[::-1] in spl):
		print(i)
		break

