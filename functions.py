# ✅ 1. Positional Arguments
'''def greet(name,age):

    print(f"hello {name},you are {age} years old")
greet("waleed",14)

# ✅ 2. Default Arguments

def greet(name= "guest"):
    print("hello",name)     
greet("ddwdw")


#  Keyword Arguments

def student(name,roll):
  print(f"name :{name},roll :{roll }")
student(roll=45, name="waleed")

# Arbitrary Arguments (*args)
def total_marks(*marks):
      print("total:",sum(marks))
total_marks(45,3,4)
'''
countries = ("spain","russia","india","iran")
temp = list(countries)
temp.append("afg")
temp.pop(2)
temp[2]= "finland"

countries= tuple(temp)
print(  countries)  