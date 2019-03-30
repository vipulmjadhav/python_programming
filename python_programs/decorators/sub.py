def sub(a,b):
	print(a-b)

sub(5,10)

def DecSub(fptr):
	
	def innerFunc(a,b):
		if(b>a):
			a,b = b,a
			return fptr(a,b)
	return innerFunc
	
sub = DecSub(sub)

#sub(10,5)
sub(5,10)

