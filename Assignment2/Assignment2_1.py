import Assignment2_1Module as calci


def callModule(): 
	Num1 = input()
	Num2 = input()

	Ret = calci.Add(Num1,Num2)
	print(Ret)

	Ret = calci.Sub(Num1,Num2)
	print(Ret)

	Ret = calci.Mult(Num1,Num2)
	print(Ret)

	Ret = calci.Div(Num1,Num2)
	print(Ret)

callModule()


