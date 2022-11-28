def main():
    # Open a file named 
    outfile = open('test2.txt', 'w')

    # Write lines by write() method
    outfile.write('Line 1\n')
    outfile.write('Line 2\n')
    outfile.write('Line 3\n')

    # Write lines by writelines() method
    list1 = ['Line 4\n', 'Line 5\n', 'Line 6\n']
    outfile.writelines(list1)

    # Close the file.
    outfile.close()

main()

