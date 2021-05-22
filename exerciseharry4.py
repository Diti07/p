n=int(input("no of rows="))
a=int(input("type 1 for simple pattern and 0 for revers pattern="))
if (a==0):
    for i in range(n + 1):
        for j in range(n):
            print("*", end="")
        n = n - 1
        print("")
elif (a==1):
    for i in range(n + 1):
        for j in range(i):
            print("*", end="")
        print("")
elif (a==2):
    for i in range(n+1):
        for j in range(i):
            print(n,end="")
        n=n-1
        print("")
elif (a==3):
    for i in range(n+1):
        for j in range(i):
            print(i,end="")
        print("")
elif (a==4):
    for i in range(n):
        for j in range(n):
            print(n,end="")
        n=n-1
        print("")