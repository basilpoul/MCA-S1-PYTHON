fact=1
num1=int(input("Enter a number : "))

for i in range(num1,0,-1):
    fact*=i

print(f"The factorial of {num1} is {fact}")    
