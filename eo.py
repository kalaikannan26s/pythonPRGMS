try:
    q=input()
    if(int(q)%2==0):
        print("even")
    else:
        print("odd")
except ValueError:
    print("invalid")
