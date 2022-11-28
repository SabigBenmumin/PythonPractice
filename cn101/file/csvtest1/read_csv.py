import csv

def read():
    file_name = "username-password-recovery-code.csv"
    with open(file_name,mode='r') as csvfile:
        read_data = csv.reader(csvfile,delimiter=';')
        item = []
        for row in read_data:
            print(row)
        return
     
def writing():    
    file_name = "username-password-recovery-code.csv"
    with open(file_name,mode='a',newline='\n') as csvwriter:
        wf = csv.writer(csvwriter)
        wf.writerow(["pohmung",555])


writing()