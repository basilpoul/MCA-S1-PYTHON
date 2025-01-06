dict = {}

n = int(input("Enter the number of elements: "))

for i in range(n):
    key = input(f"Enter the key of {i+1}: ")
    value = input(f"Enter the value of {i+1}: ")
    dict[key] = value

keys = list(dict.keys())
keys.sort()

for key in keys:
    print(f"{key}: {dict[key]}")

print("\nReverse Order:")

keys.sort(reverse=True)
for key in keys:
    print(f"{key}: {dict[key]}")
