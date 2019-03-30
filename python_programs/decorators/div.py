def Div(a,b):
	print(a/b)

Div(2,10)

def DivDec(fptr):
	
	def innerFunc(a,b):
		if(a<b):
			a,b = b,a
		if(b==0):
			print('Exception handled D==0')
			return None
		else:			
			return fptr(a,b)
			
	return innerFunc

Div = DivDec(Div)
Div(2,10)
Div(5,0)

