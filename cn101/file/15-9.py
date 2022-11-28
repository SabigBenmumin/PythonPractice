import csv

def main():

    with open('Exam-scores.csv', mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',') 
        data = [row for row in csv_reader]

    for item in data:
        print(item)

main()

