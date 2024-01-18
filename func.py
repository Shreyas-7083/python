def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y

print("Enter two Value")
x=int(input("x= "))
y=int(input("y= "))

opr=int(input("""Enter The Operation
              1=+
              2=-
              3=*
              4=/"""))

if (opr==1):
    print("Addition=",add(x,y))
elif(opr==2):
   print("Substraction=",sub(x,y))
elif(opr==3):
    print("Multiplication=",mult(x,y))
elif(opr==4):
    print("Division=",div(x,y))
else:
    print("Invalid Operation")
