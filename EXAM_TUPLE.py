tuple = (4,6,4)
if 4 in tuple:
    print("it is")

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

for day in days:
    print(day)


countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple (temp)
print(countries)
print(type(tuple))