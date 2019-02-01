c=input()
b=[]
a=""
for i in c:
  b.append(i)
d=len(b)
for j in range(d):
  a=a+b[d-1]
  d=d-1
print(a)
