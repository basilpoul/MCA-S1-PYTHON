string=input("Enter a string ")
l=input("Enter the letter ")
k=0
for i in string:
    if i==l:
        k+=1

print(f"The character {l} appears {k} times in {string}")        
