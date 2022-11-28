def main():
    # Open a file named 
    outfile = open('test1.txt', 'w')

    # Write lines by write() method
    outfile.write('Line 1')
    outfile.write('Line 2')
    outfile.write('Line 3')

    # Write lines by writelines() method
    list1 = ['Line 4', 'Line 5', 'Line 6']
    outfile.writelines(list1)

    # Close the file.
    outfile.close()

main()

