def BMI(weight,height):
    bmi = weight / ((height/100)**2)
    return bmi
def WT(weight):
    #WVPD is water volume per day
    WVPD = weight * 2.2 * 30/2
    return WVPD

print("what you want use function bmi/b water/w")
Ft_select = str(input(" : "))

if Ft_select == "bmi"or Ft_select =="b":
    print("user what to use BMI function")

    weight = float(input("how much your weight [kg]= "))
    height = float(input("how your thall [cm]= "))
    print("your BMI is :",BMI(weight,height))
elif Ft_select == "water" or Ft_select == "w":
    print("user what to use water function") 
    weight = float(input("how much your weight [kg] = "))
    print("The amount of water you should drink per day is",WT(weight),"mL")
    
print("end program")
