num1=input("Enter a number : ")
temp=num1
digits=0
c=False

if float(num1)==0:
    print(f"There are 0 digits in {num1}")
else:
    for i in num1:
        if i==".":
            c=True
        digits+=1

    if c is True:
        digits-=1
    print(f"There are {digits} digits in {temp}")   
