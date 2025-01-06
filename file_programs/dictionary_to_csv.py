import csv

my_dict = [
    {'Name': 'John', 'Age': 25, 'City': 'New York'},
    {'Name': 'Alice', 'Age': 30, 'City': 'Boston'},
    {'Name': 'Bob', 'Age': 22, 'City': 'Chicago'}
]

csv_filename = 'output.csv'

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=my_dict[0].keys())
    writer.writeheader()  
    writer.writerows(my_dict)  

with open(csv_filename, mode='r', newline='') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)
