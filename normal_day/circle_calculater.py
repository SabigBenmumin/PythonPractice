def circle_area(PI,status):
    radius = float(input("input radius: "))
    print(f"area is: {PI * radius ** 2}\n")
    status = True
    loop_status = "Y"
    while status:
        if loop_status == "N":
            return "home page now"
        print("you need to use circle area calculater now?")
        status = input("yes[Y] no[N]: ")
        print("")
        if status.upper() == "Y":
            loop_status = circle_area(PI,status)
        elif status.upper() == "N":
            return "N"
        else:
            print("Sorry input again\n")


def circle_circum(PI):
    print("this function is not update now")
    print("thank you for your requirment")
    print("")

def main():
    PI = 3.14
    status = True
    while status:
        print("select your choice for using function")
        print("1 Circle area calculater")
        print("2 Circle circumference")
        print("3 Stope this program")
        select = input("Enter your choice number: ")
        print("")
        if select == "1":
            circle_area(PI,status)
        elif select == "2":
            circle_circum(PI)
        elif select == "3":
            return 0
        else:
            print("your input is out of choice\n")

main()
