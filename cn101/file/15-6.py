import csv

with open('UN.txt', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'{row} --> {",".join(row)}')


