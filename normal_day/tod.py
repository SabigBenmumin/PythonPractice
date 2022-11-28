def disemvowel(string_): 
    list_cha = ['a','A','e','E','i','I','o','O','u','U']
    for cha in list_cha:
        string_ = string_.replace(cha,'') 
    return string_

def main():
    stirng = input("Enter your stiring: ")
    result = disemvowel(stirng)
    print(result)

main()
