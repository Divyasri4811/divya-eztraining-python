size=int(input("size:"))
l=[]
for i in range(size):
    element=int(input("element:"))
    l.append(element)
print("list is:",l)

for j in l:
  if j%2==0:
    print(j)
