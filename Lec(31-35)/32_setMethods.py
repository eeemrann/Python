s1 = {1, 2, 3, 7}
s2 = {5, 9, 2, 6}

print(s1.union(s2))
print(s1,s2)

s1.update(s2)
print(s1,s2)

print(s1.intersection(s2))
print(s1,s2)

print(s1.difference(s2))
print(s1,s2)