f=open("tmp/foo.txt","r")

for line in f:
    print(line,end='')

f.close()