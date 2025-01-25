# Calculator using functions

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y


a = int(input("Write your choice: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division"))
if (a!=1 or a!=2 or a!=3 or a!=4):
    print("ERROR : Wrong choice")
    exit(-1)
b = int(input("First number: "))
c = int(input("Second number: "))
res = 0
if(a == 1):
    res = add(b,c)
elif a == 2:
    res = sub(b,c)
elif a == 3:
    res = mul(b,c)
elif a == 4:
    res = div(b,c)
else :
    print("ERROR : Wronng Choice")
    exit(-1)
print("Result:",res)