contin=True

while(contin is True):
    num1=float(input("Enter a number : "))
    num2=float(input("Enter another number : "))
    choice=int(input("What do you want to do\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division "))

    if (choice==1):
        result=num1+num2
        print(f"The sum of {num1} and {num2} is {result}")
    elif (choice==2):
        result=num1-num2
        print(f"The difference of {num1} and {num2} is {result}")
    elif (choice==3):
        result=num1*num2
        print(f"The product of {num1} and {num2} is {result}")
    elif (choice==4):
        if num2==0:
            print("Cannot divide by zero")
        else:    
            result=num1/num2
            print(f"The result of division of {num1} and {num2} is {result}")
    else:
        print("Enter a valid choice")

    c=input("Do you want to continue Y/N")

    if c.upper()=='N':
        contin=False
        
        
    
