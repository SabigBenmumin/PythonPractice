def main():
    
    population = float(input('Input number of population (Million): '))
    infile = open('UN.txt', 'r')
    data = [line.rstrip().split(',') for line in infile]
    infile.close()
    
    for i in range(len(data)):
        data[i][2] = float(data[i][2])
    
    data_population = [item for item in data if item[2] >= population]
    
    outfile = open("Populatipn.txt", 'w')
    for item in data_population:
        item[2] = str(item[2])
        item = ",".join(item) + '\n'
        outfile.write(item)
    outfile.close()
    print('The data were written to Population.txt.')

main()

