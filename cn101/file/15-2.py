def main():

    infile = open('UN.txt', 'r')
    data = [line.rstrip().split(',') for line in infile]
    infile.close()

    print(data)

main()

