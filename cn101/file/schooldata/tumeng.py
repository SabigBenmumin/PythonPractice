import csv

def add_school_data(data):
    ...

def delete_school_data(data): 
    list_school_name = []
    N = 1
    printed = []
    for row in data[1:]:
        list_school_name.append(row[0])
        if row[0] not in printed:
            print(f"{N}. {row[0]}")
            printed.append(row[0])
            N += 1
    selected_school_ID = input("Input school id: ")
    
    print("Please select level name:")
    print("M1,M2,M3,M4,M5,M6")
    level_name = input("Input level name: ")
    school_by_select_data = []
    for row in data[1:]:
        if row[0] == printed[int(selected_school_ID)-1]:
            if row[2] == level_name:
                school_by_select_data.append(row)
    '''
    school_by_select_data geb list nei wai
    [['โรงเรียนปทุมวิไล', 'คริสต์', 'M1', '2565/1', '3'],
     ['โรงเรียนปทุมวิไล', 'พุทธ', 'M1', '2565/1', '597'],
     ['โรงเรียนปทุมวิไล', 'อิสลาม', 'M1', '2565/1', '7'],
     ['โรงเรียนปทุมวิไล', 'อื่นๆ', 'M1', '2565/1', '1']]
    '''

    with open('first_edit.csv','w',encoding='utf-8',newline='\n') as outfile:
        csvwriter = csv.writer(outfile)
        for row in data:
            if row[0] != printed[int(selected_school_ID)-1]:
                if row[2] != level_name:
                    csvwriter.writerow(row) 

def search_school_data(data):
    list_school_name = []
    N = 1
    printed = []
    for row in data[1:]:
        list_school_name.append(row[0])
        if row[0] not in printed:
            print(f"{N}. {row[0]}")
            printed.append(row[0])
            N += 1
    selected_school_ID = input("Input school id: ")

    print("Please select level name:")
    print("M1,M2,M3,M4,M5,M6")
    level_name = input("Input level name: ")
    school_by_select_data = []
    for row in data[1:]:
        if row[0] == printed[int(selected_school_ID)-1]:
            if row[2] == level_name:
                school_by_select_data.append(row)

    '''
    school_by_select_data geb list nei wai
    [['โรงเรียนปทุมวิไล', 'คริสต์', 'M1', '2565/1', '3'],
     ['โรงเรียนปทุมวิไล', 'พุทธ', 'M1', '2565/1', '597'],
     ['โรงเรียนปทุมวิไล', 'อิสลาม', 'M1', '2565/1', '7'],
     ['โรงเรียนปทุมวิไล', 'อื่นๆ', 'M1', '2565/1', '1']]
    '''

    list_religion = ["คริสต์","พุทธ","อิสลาม","อื่นๆ"]
    n = 1
    for p in list_religion:
        print(f"{n}. {p}")
        n += 1
    selected_religion_ID = input("select religion ID: ")
    print(f"ศาสนา{list_religion[int(selected_religion_ID)-1]} มีผู้นับถือ {school_by_select_data[int(selected_religion_ID)-1][4]} คน")


def conclude_school_data(data):
    ...

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