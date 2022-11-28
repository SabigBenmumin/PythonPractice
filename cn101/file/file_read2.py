def main():
    # Open a file named test2.txt
    infile = open('user.txt', 'r')

    # Read the file's contents.
    file_contents = infile.read()

    # Close the file.
    infile.close()

    # Print the data that was read intomemory.
    print(file_contents)

main()

