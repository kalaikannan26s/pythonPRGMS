a=input()
b=0
for i in a:
    if not((65<=ord(i)<=90)or(97<=ord(i)<=122)or(48<=ord(i)<=57)):
        b=b+1
print(b)
