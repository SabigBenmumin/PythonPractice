def main():

    infile = open('UN.txt', 'r')
    
    data = []
    for line in infile:
        data.append(line.rstrip())
    
    infile.close ()
    print(data)

main()

