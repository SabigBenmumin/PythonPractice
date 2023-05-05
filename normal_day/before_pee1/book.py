a = input("Enter your first name and last name : ")

b = list(a)
n = len(b) - 1 
if n >= 10:
    print("'"+a+"'" ,"ชื่อแม่งยาว")
else :
    print("'"+a+"'" ,"ชื่อแม่งสั้น")