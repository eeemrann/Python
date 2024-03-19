#Strings are immutable
a= "!!!Harry!!!! !! Harry"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","John"))
print(a.split(" "))

b="introducTion tO jS"
print(b.capitalize())
print(b.center(50))#Starts from 50 step ahead
print(a.count("Harry"))
print(a.endswith("!!!"))
print(b.endswith("tO",4,15))

c="He's a good boy.But he is foolish"
print(c.find("is"))
print(c.find("iis"))#if we use index  method instead of find then error will be shown as a perfectly run program
#print(c.index("iis"))

d="WelcomeToConsole99"
print(d.isalpha())#[A-Z],[a-z]
print(d.isalnum())#[A-Z],[a-z],[0-9]
print(d.islower()) 

e="We shall overcome\n"
f="         "
print(e.isprintable())
print(d.isprintable())
print(f.isspace())# white space-->space that is used with spacebar or tab key within " "
print(e.istitle())# returns true only if first letter of each word is capitalized
print(e.startswith("We"))
print(e.swapcase())
print(e.title())