n=int(input("Enter the limit"))
# series=[0,1]
# a,b=1,0
# for i in range(1,n-1):
#     c=a+b
#     series.append(c)
#     b=a
#     a=c

# for i in series:
#     print(i,end=" ")
f1=0
f2=1
f3=0
for i in range(0,n):
    f3=f1+f2
    print(f1)
    f1=f2
    f2=f3

    
    
