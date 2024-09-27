import time


t= time.strftime('%H:%M:%S')
print(t)
t1= time.strftime('%H')
print(t1)
t2= time.strftime('%M')
print(t2)
t3= time.strftime('%S')
print(t3)

if(6<=int(t1)<=12):
    print("Good Morning.")
elif(12<int(t1)<=15):
    print("Good Noon.")
elif(15<int(t1)<=18):
    print("Good Afternoon.")
elif(18<int(t1)<=21):
    print("Good Evening.")

else:
    print("Good Night.")
    
x=time.strftime('%a--%A--%b--%B--%c--%d')
print(x)    
x1=time.strftime('%I--%j--%m--%p')
print(x1)