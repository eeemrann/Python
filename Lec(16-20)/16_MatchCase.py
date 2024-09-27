
x=int(input("Enter the value of x: "))
match x:
    case 0:
        print("The value is 0")
    case 3:
        print("The value is 3")   
    case 5:
        print("The value is 5")
    case _ if x!=90:
        print("Value is not 90")    
    case _ if x!=80:
        print("Value is not 80") 
    case _:
        print("Value didn't match")         

