def apply():
    infile = open("user.txt","a+")
    
    user_name = input("User name: ")
    password = input("Password: ")
    confirm_pass = input("Confirm password: ")
    hope = 5
    while confirm_pass != password:
        print("fail!! please confirm your password again")
        confirm_pass = input("Confirm password: ")
        hope -= 1
        if hope == 0:
            print("fail!! pleas enter your new password")
            passworld = input("Password: ")
            hope = 5
    infile.write(f"\n{user_name},{password}")
    
    print("your apply is success//")
    print(f"Wellcome {user_name} to Bigbook//")
apply()