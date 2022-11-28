def main():

    population = float(input('Input number of population (Million): '))

    infile = open('UN.txt', 'r')
    data = [line.rstrip().split(',') for line in infile]
    infile.close()

    for i in range(len(data)):
        data[i][2] = float(data[i][2])

    data_population = [country for country in data if country[2] >= population]

    for country in data_population:
        print(f'{country[0]}, {country[1]}: {country[2]}')

main()

