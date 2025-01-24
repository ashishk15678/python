n1 = int(input("n1: "))
n2 = int(input("n2: "))
i = 1
while(i<=10):   # Number of lines
    j = n1
    while(j<=n2):
        print("(",j,"*",i,"=",i*j,")",end="")
        j+=1
    print("\n")
    i+=1
