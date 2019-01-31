a=int(input())
n=int(input())
d=int(input())
h=(n+((a-1)*d))
avg=((n+h)//2)
ng=((h-n)//d)+1
sum=avg*ng
print(sum)
