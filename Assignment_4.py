import math

def my_calculator(n1,n2,operation):
    if operation==1:
        print("Addition is : ",n1+n2)
    elif operation==2:
        print("Squares of number are : ",n1**2,n2**2)
    elif operation==3:
        print("Expoenential of numbers are :",math.exp(n1),math.exp(n2))
        
def accept_input():
    flag = 'y'
    while(flag =='y'):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        opr =  int(input("Select the operation you want to perform:"+
                "\n 1. for Addition "+
                "\n 2. for Finding Square of a numbers"+
                "\n 3. for exponential of numbers"))
        my_calculator(num1,num2,opr)
        flag=input("Do you Wish to continue(Y/N): ").lower()
        if(flag == 'n'):
            print("Out of Service!!!")
            break

accept_input()



    