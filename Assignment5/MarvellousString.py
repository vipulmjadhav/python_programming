from itertools import permutations

def reverseString(string): #reverses the string
	st = ''
	for i in string:
		st  = i + st
	
	return st

def retWords(string):     # returns count of words
	cnt = 0
	string.strip()
	wordscount = len(string.split())
		
	return wordscount


def strpermutations(str): # returns the object which holds permutations of string
	permlist = list(permutations(str))
	
	return permlist

def removeChar(string,pos): # returns modified string
	lst = list(string)
	lst[pos-1] = ''
	string = ''.join(lst)
	return string

def retAsciiAvg(string):   # returns average of ascii values of characters
	avg=0
	
	for i in string:
		avg+=ord(i)
	
	return avg/(len(string))
