steps=int(input("Enter number of steps : "))
lis=[]
for i in range(1,steps+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print("\n")    
    