import math

a=float(input("Enter a : "))
b=float(input("Enter b : "))
c=float(input("Enter c : "))

inside_root=(b*b)-(4*a*c)

if inside_root<0:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(inside_root)) / (2 * a)
    solution1 = f"{real_part} + {imaginary_part}i"
    solution2 = f"{real_part} - {imaginary_part}i"
    print(f"The complex solutions are {solution1} and {solution2}")
else:
    solution1=(-b+math.sqrt(inside_root))/(2*a)
    solution2=(-b-math.sqrt(inside_root))/(2*a)
    print(f"The solutions for the problem are {solution1} and {solution2}")

    
    
