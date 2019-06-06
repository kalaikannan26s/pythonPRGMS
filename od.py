a,c=input().split()
b=[]
d=''
for i in range(int(a)+1,int(c)):
    if(i%2==0):
        b.append(i)
for i in range(len(b)-1):
    d+=str(b[i])+" "
print(d+str(b[-1]))    
        

