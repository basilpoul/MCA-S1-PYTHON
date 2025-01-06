import csv

with open(r'C:\Users\cacet\OneDrive\Desktop\subi\s1-Python\file_programs\file1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        for i in row:
            print(i,end=" ")
        print("\n")