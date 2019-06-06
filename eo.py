try:
    q=input()
    if(int(q)%2==0):
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("invalid")
