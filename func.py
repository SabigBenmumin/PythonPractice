def BMI(weight,height):
    bmi = weight / ((height/100)**2)
    return bmi

print("what you what bro (bmi)")
Ft_select = str(input(" : "))

if Ft_select == "bmi":
    print("user what to use BMI function")

weight = float(input("how much your weight = "))
height = float(input("how your thall = "))
print("your BMI is :",BMI(weight,height))
