f = open('myfile2.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)    