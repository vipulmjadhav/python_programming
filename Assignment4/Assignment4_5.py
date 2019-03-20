from functools import reduce #reduce is not defined ERROR so imported functools 

def ChkPrime(no):
	var=int(no/2)
	div=0
	for i in range(1,var+1):
		if(no%i==0):
			div=div+1
	if(div>1):
		return False
	else:
		return True

def maximum(no1,no2):
	if(no1>no2):
		return no1
	else:
		return no2
	
def callerfunc():
	Input_List = [2,70,11,10,17,23,31,77]

	List_after_filter = list(filter(ChkPrime,Input_List))

	print("List After Filter : ",List_after_filter)

	List_after_map = list(map(lambda x:2*x,List_after_filter))

	print("List After Map : ",List_after_map)

	opreduce = reduce(maximum,List_after_map)

	print("output of reduce :{}".format(opreduce))

callerfunc()
