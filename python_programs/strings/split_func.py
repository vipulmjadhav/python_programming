text = 'AbcDefGhiJklMnoPqrStuVwx'

print(text[:-1]) # prints except last character
print(text[-1])

print([text[i:i+3] for i in range(0,len(text),3)])	

print(text.split('i'))
