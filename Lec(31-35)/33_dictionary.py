dic = {
    344: "Harry",
    56: "Watson",
    678: "Zakir",
    567: "Neha"
}
print(dic[567])
print(dic.get(567))

info = {
    'name': "Emran",
    'age': 22,
    'eligible': True
}
print(info['name'])
print(info.get('name2'))
print(info.get('name'))

print(dic.keys())
print(info.keys())

for key in dic:
    print(dic[key])
for key in info:
    print(info[key])    

for key in dic:
    print(f"The value corresponding to the key {key} is {dic[key]}")
for key in info:
    print(f"The value corresponding to the key {key} is {info[key]}")


print(info.items())     
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")   