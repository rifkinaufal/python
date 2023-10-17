#list ordering
list_org = ["gedang", "apel"];

list_cpy = list_org
print (list_cpy)
print (list_org)

#list mutable
mylist  = [1,2]
b = [i+i for i in mylist]

print(mylist)
print(b)

#tuple
mytaple = ("i", "k")
print(mytaple.count ('k') )

#dictio
dicti  = {"name":"rifki", "age":19 }
print(dicti)

dicti.popitem ()
print(dicti)

#unoredered dicti
dicti  = {"name":"rifki", "age":19 }
print(dicti)

try:
    print(dicti["Lastname"])
except:
    print("error")

#set
myset =  {1, 2, "gedang", True}

print(myset)
#set lenght
myset = {1, 2, "gedang"}

print(len(myset))

myset = {1, 2, "gedang"}
print ("gedang" in myset)
#statement
a = 1
b = 9
if b == a:
    print("b is gretaer than a")
elif a == b:
    print("a and b are equal")
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")   

#and
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

#not
a = 77
b  = 74
if not  a >  b:
    print("a is NOT greater than b")

a = 22
b = 222

if b > a:
    pass

#while
i = 1
while i < 6:
    print(i)
    i += 1

#continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#range
for x in range(2, 6):
    print(x)

#funct
def my_function():
    print("Hello from a function")

my_function()

#argument funct
def my_function (fname, iname):
    print (fname + "" + iname)

my_function("emil", "rifki")

#lambda
x = lambda a, b : a * b
print (x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#class
class MyClass:
    x = 1

#object
p1 = MyClass()
print(p1.x)

#scope
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

#global scope
x = 300

def myfunc():
    print(x)

myfunc()

print(x)


#set
myset = set()

myset.add(3)
myset.add(2)

if 2 in myset:
    print("yoi")

#string
my_string = "oit"
print(my_string)

#ittertools
from itertools import product
a = [1,2]
b = [3,4]
p = product(a,b)
print(list(p))

#exception 
try :
    a = 8/0
    b = a  = 4
except ZeroDivisionError as e:
    print(e)

#logging
import logging
logging.warning('warning')

#json
import json
x =  '{ "age":30}'
y = json.loads(x)
print(y["age"])

#random
import random

mylist = list("ABC")
a = random.choice(mylist)
print (a)