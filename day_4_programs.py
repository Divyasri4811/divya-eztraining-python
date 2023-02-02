DAY-4:

#dictionary comprehension:

d={n:n*n for n in range(1,5)}
print(d)
{1: 1, 2: 4, 3: 9, 4: 16}

#calculating product price for 5 units

old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for (product,price) in old.items()}
print(new)

#with checks

real={'sam':24,'angel':18,'kumar':35}
new={name:age for (name,age) in real.items() if age>20}
print(new)

#to check whether particular char is present in string:

n=input("enter:")
print("the string is :",n)
x=input("enter x:")
print("the char is :",x)
chr==n.find(x)
if x in (n):
      print("char is present in string")
else:
      print("char is not present in string")

#iteration logic

s=input("enter:")
char=input("enter:")
for i in s:
   if i==char:
         flag=1
         break
   else:
         flag=0
if flag==1:
      print("present")
else:
      print("not present")

#logic3

str=input("enter the string:")
char=input("enter the char:")
a="yes" if char in str else "no"
print(a)

#palindrome:

n=input("enter:")
print("the name is :")
if n==n[::-1]:
    print("it is palindrome")
else:
    print("it is not palindrome")

#to count spaces in a string:

s=input("enter a string:")
count=0
for i in s:
    if i==" ":
        count+=1
print(count)

#list of 8 customers to print as dict using random function:

import random
cust=["divya","venu","roopa","sudha","rohitha","lakshmi","venky","satya"]
cust_dict={names:random.randint(1,100) for names in cust}
print(cust_dict)

#vowels:

l=['a','e','i','o','u']
s=input("enter string:")
print("the string is:",s)
count=0
for i in s:
  if i in l:
      count=count+1
print("the no.of vowels in string are:",count)

#students names and percentage using random and zip:

import random
stud_names=list(map(str,input("Enter name:").split()))
marks=[]
for i in range(len(stud_names)):
    a = (random.randint(300,500)/500)*100
    marks.append(a)
my_dict={x:y for (x,y) in zip(stud_names,marks)}    
print(my_dict)

#2ndmethod

import random
stud_names=list(map(str,input("Enter name:").split()))
marks=[]
for i in range(len(stud_names)):
    a = (random.randint(300,500))
    print(a)
    b=(a/500)*100
    marks.append(d)
my_dict={x:y for (x,y) in zip(stud_names,marks)}    
print(my_dict)

#mutable and immutable:

l=[1,2,3]
print(l)
print(id(l))
l.append(45)
print(l)
print(id(l))

#immutable (int,float,string,bool,tuple)

x=300
print(x)
print(id(x))
x=x+30
print(x)
print(id(x))

#string

s="divya"
print(s.upper())
print(s.lower())  #s.lower() or s.casefold()
print(s.capitalize())
print(s.replace('a','e'))
print(s.strip())
print(s.split("v"))
print(s.center(7,'*'))
print(s.replace('v','a',))
print(s.count('a'))
print(s.count('a',3,len(s)))
print(s.endswith('a',0,len(s)))
print(max(s))
print(min(s))
print(s.startswith('hello',0,len(s)))
print(s.rfind('a',0,len(s)))

#mathmodule

import math
print("CEIL 12.5:",math.ceil(12.5))
print("FLOOR 12.5:",math.floor(12.5))
print("SQRT 345:",math.sqrt(345))
print("FACTORIAL 3:",math.factorial(3))
print("POWER 2,3:",math.pow(2,3))
print("REMAINDER 10,3:",math.fmod(10,3))
a,b=divmod(10,3)
print(a,b)





         
     

