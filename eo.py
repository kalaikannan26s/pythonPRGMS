try:
    a=input()
    if(int(a)%2==0):
        print("the number is even")
    else:
        print("the number is odd")
except ValueError:
    print("invalid")
