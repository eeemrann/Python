class Details():
    name = "Emran"
    age = 20
    def info(obj2):
        print(f"My name is {obj2.name} and I'm {obj2.age}")

obj = Details()

#print(obj.name)
#print(obj.age)
obj.info()




class Person: 
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    def info(obj):
        print(f"{obj.name} is a {obj.occupation}")

a = Person()
b = Person()
a.name = "Shubham"
b.name = "Nikita"
a.occupation = "Accountant"
b.occupation = "HR"
#print(a.name, a.occupation)
a.info()  
b.info()