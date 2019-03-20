def ChkDiv(iNo):
	if(iNo%5==0):
		return 'true'
	else:
		return 'false'
def AcceptNum():
	iNum = int(input())
	bRet = ChkDiv(iNum)
	print(bRet)

AcceptNum()
