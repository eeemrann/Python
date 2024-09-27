names= "Harry, I am good"

print(len(names))#16
print(names[0:6])#Harry,
print(names[2:6])#rry,
print(names[:6])#Harry,
print(names[:])#???
print(names[0:-3])# --> print(names[0: len(names)-3 ])
print(names[-1:6])#(16-1):(6)-->15:6 doesn't make any sense
print(names[-8:15])#(16-8):15-->8:15 makes sense
print(names[-4:-1])#(16-4):(16-1)-->12:15

print()
pagla="Pagla khepa matha noshto"
print(len(pagla))
print(pagla[1:20])