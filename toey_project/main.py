def minus(n1, n2):
    return n1 - n2

def add(n1 ,n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def mod(n1, n2):
    return n1 % n2
    
def main():
    still_run = True
    while still_run:
        print("Select operator for calculate.")
        print("[1] add")
        print("[2] minus")
        print("[3] multiply")
        print("[4] divide")
        print("[5] modulus")
        print("[6] stop application")
        choice = input("Enter your choice: ")
        if choice == "1":
            n1 = int(input(">> "))
            print(" + ", end= '')
            n2 = int(input())
            result = add(n1, n2)
            print("= ", result)
        elif choice == "6":
            break

main()