numbers=[]
largest=0

num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))
num3=float(input("Enter the third number : "))

numbers.append(num1)
numbers.append(num2)
numbers.append(num3)

for i in numbers:
    if i>largest:
        largest=i

print(f"Largest number is {largest}")

