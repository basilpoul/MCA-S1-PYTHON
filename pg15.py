string=input("Enter a string ")
unique=set(string)

for i in unique:
    print(f"The character {i} appears {string.count(i)} times in {string}")

