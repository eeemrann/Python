info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

ep1={122:45, 123:89, 567:69, 670:69}
ep2={222:67, 566:90}

ep1.update(ep2)
print(ep1)

ep1.clear()
print(ep1)
empt = {}
print(empt)

ep1.clear()
ep1.popitem(122)
del ep1["122"]