

import random
import csv
import string

data = []
alphabet = string.ascii_uppercase
for i in range(1, 10001):
    row = {'Customer': alphabet[5*random.randint(0, 5)]}
    if i <= 2000:
        row['Data1'] = random.randint(1, 10) 
        row['Data2'] = random.randint(1, 10)
        row['Data3'] = random.randint(1, 10)
        row['Data4'] = None
        row['Data5'] = None
        row['Data6'] = None
        row['Data7'] = None
        row['Data8'] = None
        row['Data9'] = None
        row['Data10'] = None
    elif i <= 3000:
        row['Data1'] = random.randint(1, 10) 
        row['Data2'] = random.randint(1, 10)
        row['Data3'] = random.randint(1, 10)
        row['Data4'] = random.randint(1, 10)
        row['Data5'] = None
        row['Data6'] = None
        row['Data7'] = None
        row['Data8'] = None
        row['Data9'] = None
        row['Data10'] = None
    elif i <= 4500:
        row['Data1'] = random.randint(1, 10) 
        row['Data2'] = random.randint(1, 10)
        row['Data3'] = random.randint(1, 10)
        row['Data4'] = random.randint(1, 10)
        row['Data5'] = random.randint(1, 10)
        row['Data6'] = None
        row['Data7'] = None
        row['Data8'] = None
        row['Data9'] = None
        row['Data10'] = None
    elif i <= 5500:
        row['Data1'] = random.randint(1, 10) 
        row['Data2'] = random.randint(1, 10)
        row['Data3'] = random.randint(1, 10)
        row['Data4'] = random.randint(1, 10)
        row['Data5'] = random.randint(1, 10)
        row['Data6'] = random.randint(1, 10)
        row['Data7'] = None
        row['Data8'] = None
        row['Data9'] = None
        row['Data10'] = None
    elif i <= 7000:
        row['Data1'] = random.randint(1, 10) 
        row['Data2'] = random.randint(1, 10)
        row['Data3'] = random.randint(1, 10)
        row['Data4'] = random.randint(1, 10)
        row['Data5'] = random.randint(1, 10)
        row['Data6'] = random.randint(1, 10)
        row['Data7'] = random.randint(1, 10)
        row['Data8'] = None
        row['Data9'] = None
        row['Data10'] = None
    elif i <= 8000:
        row['Data1'] = random.randint(1, 10) 
        row['Data2'] = random.randint(1, 10)
        row['Data3'] = random.randint(1, 10)
        row['Data4'] = random.randint(1, 10)
        row['Data5'] = random.randint(1, 10)
        row['Data6'] = random.randint(1, 10)
        row['Data7'] = random.randint(1, 10)
        row['Data8'] = random.randint(1, 10)
        row['Data9'] = None
        row['Data10'] = None
    elif i <= 9000:
        row['Data1'] = random.randint(1, 10) 
        row['Data2'] = random.randint(1, 10)
        row['Data3'] = random.randint(1, 10)
        row['Data4'] = random.randint(1, 10)
        row['Data5'] = random.randint(1, 10)
        row['Data6'] = random.randint(1, 10)
        row['Data7'] = random.randint(1, 10)
        row['Data8'] = random.randint(1, 10)
        row['Data9'] = random.randint(1, 10)
        row['Data10'] = None
    else:
        row['Data1'] = random.randint(1, 10) 
        row['Data2'] = random.randint(1, 10)
        row['Data3'] = random.randint(1, 10)
        row['Data4'] = random.randint(1, 10)
        row['Data5'] = random.randint(1, 10)
        row['Data6'] = random.randint(1, 10)
        row['Data7'] = random.randint(1, 10)
        row['Data8'] = random.randint(1, 10)
        row['Data9'] = random.randint(1, 10)
        row['Data10'] = random.randint(1, 10)
    data.append(row)

with open('data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['Customer', 'Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7', 'Data8', 'Data9', 'Data10'])
    csv_writer.writeheader()
    csv_writer.writerows(data)