def check(user_name,password):
    infile = open('user.txt','r')
    data = [line.rstrip().split(',') for line in infile]
    infile.close()
    if user_name in data[1:][0]:
       user = True
    else:
        user = False
    if user_name in data[1:][1]:
        passw = True
    else:
        passw = False
    return [user,passw,data[0]]

def login():
    user_name = input("user name: ")
    password = input("password: ")
    recheck = check(user_name,password)
    while recheck[0] == False:
        print("unknow your user name!!")
        print("please login again!!")
        user_name = input("user name: ")
        password = input("password: ")
        while recheck[1] == False:  
            print("it's not your password!!")
            password = input("password: ")
            recheck = check(user_name,password)
    print(f'welcome {user_name}')
        

login()