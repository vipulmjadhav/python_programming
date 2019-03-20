from functools import reduce #reduce is not defined ERROR so imported functools 

def callerfunc():
	Input_List = [5,2,3,4,3,4,1,2,8,10]

	def chkEven(no):
		return (no%2==0)

	def Square(no):
		return no*no

	def add(no1,no2):
		return(no1+no2)

	List_after_filter = list(filter(chkEven,Input_List))

	print("List After Filter : ",List_after_filter)

	List_after_map = list(map(Square,List_after_filter))

	print("List After Map : ",List_after_map)

	opreduce = reduce(add,List_after_map)

	print("output of reduce :{}".format(opreduce))

callerfunc()
