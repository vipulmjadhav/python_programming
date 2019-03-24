#duck typing is a concept:

'''
below example states that if someone is asking a waiter : do yo have indian food
waiter calls a class -> Food(Indian) and gets answer : indian food contains raw masala ...so we have this type of food for indian category

then if customer confirms for that type of food is Indian then it is Indian Food.

----------------------

if a bird is walking like a duck..
if a bird is talking like a duck..
if a bird is flying like a duck..
	then it is a duck..

we are comparing the input with the exisitng ones...

example2:
	security agents checkig for suspicous person
		they know the qualities of suspicious person
	so they compares this qualities with the persons they are observing and then they confirms 
	by asking them some questions...

'''

class Indian:
	def info(self):
		print("indian food contains raw masala ")


class Italian:
	def info(self):
		print("italian food contains raw veggies ")

class American:
	def info(self):
		print("american food contains raw sausage ")

class Food:
	def __init__(self,type):
		type.info()

def main():
	indobj = Indian()
	obj = Food(indobj)
	
	itobj = Italian()
	obj = Food(itobj)
	
	amobj = American()
	obj = Food(amobj)
	
if __name__ == "__main__":
	main()
