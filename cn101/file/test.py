def main():
    outfile = open('test.txt','w')
    outfile.write('line 1')
    outfile.write('line 2')
    outfile.write('line 3')
    outfile.write('line 4')
    list1 = ['Line 1','Line 2','Line 3','Line 4']
    outfile.writeline(list1)
    outfile.close()
main()
