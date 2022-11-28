def login():
    infile = open("user.txt","r")
    user_list = [user.rstrip().split(',') for user in infile]

    print(user_list)
        
    #user_name = input("User name: ")
    user_name = "sabig@dome.com"
    password = "sabi555"
    #password = input("Password: ")
    x = True
    while x:
        if user_name in user_list[1:][0]:
            print("pass")
    infile.close()


login()