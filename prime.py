b=int(input())
c=0
for i in range(1,b+1,1):
    if(b%i==0):
        c=c+1
if(c==2):
    print("yes")
else:
    print("no")
