string=input("Enter a string : ")
if string[-3:]=="ing":
    print(string[:-3]+"ly")
else:
    print(string+"ing")
