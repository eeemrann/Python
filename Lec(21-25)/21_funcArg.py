def average(a=9, b=6):
    print("The average is",(a+b)/2)

average(4, 5)
average()
average(5) 
average(b=5)   


def name(fname,mname="John",lname="Watson"):
    print("Hello,",fname,mname,lname)

name("Amy","Kock")



def average1(*numbers):
    for i in numbers:
        sum = 0
        sum = sum + i
    print("Average is: ",sum/len(numbers))    

average1(5,7,12,89,12,34,122)    