a=int(input())
b=0
for i in range(0,3):
  c=a%10
  b=(b*10)+c
  a=a//10
print(b)  
