class BookStore:
	NoOfBooks = 0
	
	def __init__(self,name,author):
		self.name = name
		self.author = author
		BookStore.NoOfBooks+=1
	
	def Display(self):
		print("Name of Book : ",self.name)
		print('Name of Author:',self.author)
		print('NoOfBooks : ',BookStore.NoOfBooks)
	
print('-------------------------------------------------')
Obj1=BookStore('Linux System Programming', 'Robert Love')
Obj1.Display()

print('-------------------------------------------------')

Obj2=BookStore('C Programming', 'Dennis Ritchie')
Obj2.Display()
