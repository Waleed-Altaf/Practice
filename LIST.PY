MARKS = [4,5,3,7,"harry"]
print (MARKS[len(  MARKS  )-4])
print(MARKS[len(MARKS)-3])
print(MARKS[2:5])


lst = [ i*i for i  in range(10) if i % 2 ==0]
print(lst)


# sort list
l = [4,3,5,7,2]
l.sort()
print(l)
 
#  if we need decending
l = [4,3,5,7,2]
l.sort(reverse=True)
print(l)
 
# reverse list

l =[4,6,3,2,6,6,9]
# print(l.count(6)) 
l.reverse()
print(l)





lst = [i for i in range(10)if i % 2==0]
print(lst)

l = [5,7,6,3,8,9]
l.sort(reverse=True)
print(l)


# PRINT 5 NUMBERS

number = []
for i in range(5):
    num =  int(input(f"enter number {i+1}"))
    number.append(num)
    total = sum(number)
    print("num", number)
    print("sum",total)

