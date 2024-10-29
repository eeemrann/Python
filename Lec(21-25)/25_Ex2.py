countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries = tuple(temp)
print(countries)


countries1 = ("Pakistan", "Afghanistan", "Bangladesh","Srilanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries1+countries2
print(southEastAsia)


tuple1 = (0, 1, 2, 3, 4, 3, 2, 3, 1, 2, 4, 3)
res = tuple1.count(3)
print(res)