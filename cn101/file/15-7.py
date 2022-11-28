import csv

def main():
    
    population = float(input('Input number of population (Million): '))

    with open('UN.txt', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',') 
        data = [row for row in csv_reader]
    
    for i in range(len(data)):
        data[i][2] = float(data[i][2])
    
    data_population = [item for item in data if item[2] >= population]

    with open('Population2.txt', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for item in data_population:
            csv_writer.writerow(item)

    print('The data were written to Population2.txt.')

main()

