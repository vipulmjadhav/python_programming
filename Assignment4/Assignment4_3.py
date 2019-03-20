from functools import reduce

def callerfunc():
	input_list = [4,34,36,76,68,24,89,23,86,90,45,70]

	List_after_filter = list(filter(lambda no:no>=70 and no<=90,input_list))

	print("List After Filter : ",List_after_filter)

	List_after_map = list(map(lambda no:no+10,List_after_filter))

	print("List After Map : ",List_after_map)

	opreduce = reduce(lambda no1,no2:no1*no2,List_after_map)

	print("output of reduce :",opreduce)

callerfunc()
	
