fname = input("Enter the filename : ")

fd = open(fname,mode = "r",encoding = "UTF-8")

print(fd.read())


