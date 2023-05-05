status = "incorrect"
list_username = {"Sabig","Afham"}
list_password = {"0850","1969"}
while status == "incorrect":
    username = str(input("user name :"))
    password = str(input("password :"))
    if username in list_username:
        print("username pass")
        if password in list_password:
            status = "correct"
print("link start ..")
print("############")
print("<<<< wellcome to system >>>>")


