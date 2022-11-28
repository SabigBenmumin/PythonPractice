def apply():
    infile = open("user.txt","r")
    ram = infile.read()
    outfile = open("user.txt","w")
    user_name = input("enter your user name: ")
    password = input("enter your password: ")
    confirm = input("confirm your password: ")
    success = False
    while confirm != password:
        print("fail")
        confirm = input("confirm your password again: ")
    success = True
    if success:
        outfile.write(f'{ram}\n')
        outfile.write(f'{user_name},{password}')
        print("your apply is success")
    outfile.close()

apply()

