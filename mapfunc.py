def square(n):
    return n*n

def add(a):
    return a+a
l=[4,6,8,9,7]
result=map(square,l)
addition=map(add,l)

print("Square",list(result))
print("Addition",list(addition))