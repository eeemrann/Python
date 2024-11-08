a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")


try:
    for i in range(1,11):
        print(f"{int(a)}*{i} = {int(a)*i}")
except Exception as e:
    print("Invalid input!")
    print("Error:",e)


print("Some imp lines of code")  
print("End of Program")  


try:
    b = int(input("Enter an integer: "))
    c = [6,9,3,4]
    print(c[b])
except ValueError as V:
    print(V)
except IndexError as I:
    print(I)        
