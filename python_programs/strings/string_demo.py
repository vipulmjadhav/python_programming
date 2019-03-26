text = 'Abc Def Ghi Jkl Mno Pqr Stu Vwx $'

spl = text.split('$')

print(spl[::-1]) #reverse string
print(spl[-1])

spl[-1] = spl[-1].split('$')[0] # spl[-1] is $ so splitted into ['',''] and then [0] fills '' in 											spl[-1]

print(spl[-1]) #prints last word

arr = list()

arr = (10,20,39,40,56,3,90)

i=56

if i in spl:                 #checks for presence  working of if like for bacause of in keyword which is iterator
	print("present")



