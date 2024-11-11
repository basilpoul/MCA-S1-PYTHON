n=int(input("Enter the limit"))
series=[0,1]
a,b=1,0
for i in range(1,n-1):
    c=a+b
    series.append(c)
    b=a
    a=c

for i in series:
    print(i,end=" ")

    
    
