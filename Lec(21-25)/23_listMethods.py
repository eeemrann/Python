l = [ 1, 24, 32, 4, 24]
print(l)

l.append(7)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(4))
print(l.count(24))

l.insert(1,899)
print(l)

m = [900, 1000, 1100]
l.extend(m)
print(l)

k = l + m
print(k)