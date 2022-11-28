import csv
import random

#read file
def read_data(file_name):
    with open(file_name,mode="r") as f:
        reader = csv.reader(f,delimiter=',')
        data = [row for row in reader]
        return data

#read_data()
def read_from_username(data):
    username = input("Enter your username for search your info: ")
    for row in data:
        if row[0] == username:
            print(f"Name: {row[4]} {row[5]}")
            print(f"ID: {row[1]}")
            print(f"Department: {row[6]}")
            print(f"Location: {row[-1]}")  

def write_user(data):
    print("Enter your infomation")
    user_name = input("Username: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    department = input("Department: ")
    location = input("Location: ")

    list_id = []
    list_OTP = []
    list_RC = []
    L1 = True
    L2 = True
    L3 = True
    for row in data:
        list_id.append(row[1])
        list_OTP.append(row[2])
        list_RC.append(row[3])
            
    identifier = ''
    while L1:
        for i in range(0,4):
            num = random.randint(0,9)
            identifier += str(num)
        if identifier not in list_id:
            L1 = False
        else:
            identifier = ''

    onetime_password = ''
    while L2:
        for c in range(0,6):
            if c>1 and c<4:
                cha = random.randint(97,122)
                onetime_password += chr(cha)
            else:
                num = random.randint(0,9)
                onetime_password += str(num)
        if onetime_password not in list_OTP:
            L2 = False
        else:
            onetime_password = ''

    recovery_code = ''
    while L3:
        for r in range(0,6):
            if r < 2:
                cha = random.randint(97,122)
                recovery_code = recovery_code+chr(cha)
            else:
                num = random.randint(0,9)
                recovery_code =  recovery_code+str(num)
        if recovery_code not in list_RC:
            L3 = False
        else:
            recovery_code = ''

    list_info = [user_name,identifier,onetime_password,recovery_code,first_name,last_name,department,location]
    return list_info

def main():
    file_name = "username-password-recovery-code.csv"
    data = read_data(file_name)
    print("What you what to do in this program?")
    print("please press your choise [1-3]")
    print("1. search user info by username")
    print("2. write info for new user")
    print("3. delete user")
    choise = input("your choise: ")
    if choise == '1':
        read_from_username(data)
    if choise == '2':
        result = write_user(data)
        with open(file_name,"a",newline="\n") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(result)
        print("\nupdate data")
        print(f"Username: {result[0]}")
        print(f"ID: {result[1]}")
        print(f"First name: {result[-4]}")
        print(f"Last name: {result[-3]}")
        print(f"Department: {result[-2]}")
        print(f"Location: {result[-1]}")

main()
