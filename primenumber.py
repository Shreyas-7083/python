num=int(input("Enter The Number:"))
if num>1:
    for i in range (num,2):
        if(num%i)==0:
            print(num,"is not a prime number")
            break
        else:
          print(num,"is prime number")
else:
    print(num,"is not a prime number")