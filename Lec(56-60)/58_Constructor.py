class Person:
    def __init__(self, n, o):
        print("Hey I am a learner")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

obj1 = Person("Harry", "Developer")
obj2 = Person("Nikita", "HR")
obj1.info()
obj2.info()