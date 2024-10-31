letter = "Hey my name is {} and I am from {}"
country = "Bangladesh"
name = "Emran"

print(letter.format(country,name))
print(letter)
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")


txt = "For only {price:.2f} dollars"
print(txt.format(price=49.09099))

price1=78.089
txt1 = f"For only {price1:.2f} dollars"
print(txt1)

print(f"{2*30}")
print(type(f"{2*30}"))