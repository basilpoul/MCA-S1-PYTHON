a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(b>a):
    a,b=b,a
if b!=0:
    rem=1
    while(rem!=0):
        rem=a%b
        a=b
        b=rem
print("gcd is:",a)


