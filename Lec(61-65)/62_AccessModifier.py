#Public Access Modifier
class Employee:
    def __init__(self):
        self.name = "Harry"

a = Employee()
print(a.name)



#Private Access Modifier
class Employee:
    def __init__(self):
        self.__age = 134

a = Employee()
#print(a.__age)           #Can't be accessed directly
print(a._Employee__age)   #Can be accessed directly



#Protected Access Modifier
