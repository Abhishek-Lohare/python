num1=int(input("Enter a starting number "))
num2=int(input("Enter last number "))
#i=1
while num1<=num2:
    if num1*num1<num2:
       p=num1*num1
       print(p)
       num1=num1+1
       continue
    break
