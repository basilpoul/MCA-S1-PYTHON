import csv

with open(r'C:\Users\cacet\OneDrive\Desktop\subi\s1-Python\file_programs\file1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    data = list(reader)

for col in zip(*data): 
    for i in col:
        print(i,end=" ")  
    print("\n")