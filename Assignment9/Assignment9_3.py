import sys
fname = sys.argv[1];

fd = open(fname,mode = "r",encoding="UTF-8")

txt = fd.read()

cname = sys.argv[2]

fd1 = open(cname,mode = "x+");

fd1.write(txt)

print('Reading newly created file!!!');

fd1.seek(0)
print(fd1.read())
