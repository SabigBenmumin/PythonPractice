# ID: 6510742064, Name: Natchanon jaikla
import csv
def get_school_names(data):
    ...

def get_religion_names(data):
    ...

def add_school_data(data):
    NameSchool = input('Input name school: ')
    YearTerm = '2565/1'

    print('\nPlease select religion:')
    print('1. ศริสต์')
    print('2. พราหมณ์/ฮินดู')
    print('3. พุทธ')
    print('4. อิสลาม')        
    print('5. อื่นๆ')
    choiceReligion = input('Your choice: ')
    if choiceReligion == '1':
        Religion = 'ศริสต์'
    elif choiceReligion == '2':
        Religion = 'พราหมณ์/ฮินดู'
    elif choiceReligion == '3':
        Religion = 'พุทธ'
    elif choiceReligion == '4':
        Religion = 'อิสลาม'
    elif choiceReligion == '5':
        Religion = 'อื่นๆ'

    print('\nPlease select level name:')
    print('P1 P2 P3 P4 P5 P6')
    print('M1 M2 M3 M4 M5 M6')
    Level = input('Input Level name: ')
    Total = input('Input number of students: ')

    School = [NameSchool, Religion, Level, YearTerm, Total]

    print(NameSchool, YearTerm, Religion, Level ,Total)

    with open('school-religion.csv', mode='a', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(School)

    data.append(School)

def search_school_data(data):
    print(id(data))
    n = 0
    for school in data:
        n = n+1
        print(n, school[0])


    school = float(input('Input name school: '))

    with open('school-stat.csv.csv', mode='a', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',') 
        data = [row for row in csv_reader]
    
    for i in range(len(data)):
        data[i][0] = float(data[i][0])
    
    data_school = [item for item in data if item[0] == school]

    print(data_school)


def delete_school_data(data):
    delete_school = input('Input school to remove: ')
    for i, school in enumerate(data):
        if school[0] == delete_school:
            del data[i]

# Find conclude data and write it to file
def conclude_school_data(data):
    print(id(data))
    for school in data:
        print(school)

def main():

    # DO NOT CHANGE THE FOLLOWING LINES IN MAIN()

    with open('school-stat.csv', encoding='utf-8-sig') as infile:
        csv_reader = csv.reader(infile, delimiter=',')
        data = [row for row in csv_reader]

    while True:
        # school_names = get_school_names(data)
        print('\nPlease select:')
        print('1. Add school data')
        print('2. Delete school data')
        print('3. Search school data')
        print('4. Print and save conclusion school data')        
        print('5. Exit')
        choice = input('Your choice: ')
        if choice == '1':
            add_school_data(data)
        elif choice == '2':
            delete_school_data(data)
        elif choice == '3':
            search_school_data(data)
        elif choice == '4':
            conclude_school_data(data)
        elif choice == '5':
            print('Goodbye!')
            break

main()