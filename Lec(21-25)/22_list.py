marks=[5,6,9,"Harry",True]

print(marks)
print(type(marks))
print(marks[0])
print(marks[4])
print(marks[3])

print(marks[-3]) #len(marks)-3=5-3=2 no index

if 7 in marks:
    print("Yes")
else:
    print("No")    


if "arry" in "Harry":
    print("yes")
else:
    print("No")        


print(marks[1:3]) #1,2
print(marks[2:4]) # 2,3
print(marks[1:-1]) # 1,2,3

print(marks[:])
print(marks[0:5:2]) #skipping 2 index

lst = [i for i in range(4)]
print(lst)