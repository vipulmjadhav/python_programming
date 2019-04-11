import sys
key = input("enter the key : ")

fd = open(sys.argv[1],mode = 'r',encoding = "UTF-8");

txt = fd.read()

cnt = txt.count(key)

#print("count of {} is {}",format(str(key),int(cnt)));
print(cnt)
