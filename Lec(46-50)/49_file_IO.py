#f = open(r'D:\Documents\Python\Lec(46-50)\myfile.txt', 'r')
f = open('myfile2.txt', 'r')
#f.write('Hello World')
text = f.read()
print(text)
f.close()