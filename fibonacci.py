count=2
limit=int(input("Enter the terms you want to get from series "))
#intializing first two statement
t1,t2=0,1
print("0"+ ":"+ str(t1))
print("1"+ ":"+ str(t2))
t3 = t1 + t2
while count<=limit:
    print(str(count) +":"+ str(t3))
    t1=t2
    t2=t3
    t3=t1+t2
    count+=1