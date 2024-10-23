def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print("First number is greater.")
    else:
        print("Second number is gtreater.")        

a = 9
b = 8
calculateGmean(a, b)
isGreater(a, b)    

c = 7
d = 8
calculateGmean(c, d)
isGreater(c, d)