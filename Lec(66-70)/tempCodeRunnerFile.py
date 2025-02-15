class Dog:
    # Class variable
    species = 'Canis familiaris'

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Creating instances of the Dog class
dog1 = Dog('Buddy', 2)
dog2 = Dog('Lucy', 3)

# Accessing class variable
print(f"Dog1 is a {dog1.species}")
print(f"Dog2 is a {dog2.species}")

# Accessing instance variables
print(f"Dog1's name is {dog1.name} and age is {dog1.age}")
print(f"Dog2's name is {dog2.name} and age is {dog2.age}")

# Modifying instance variable
dog1.age = 4
print(f"Dog1's new age is {dog1.age}")

# Modifying class variable
Dog.species = 'Canis lupus'
print(f"Dog1 is now a {dog1.species}")
print(f"Dog2 is now a {dog2.species}")




