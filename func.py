

def BMI(wheight,height):
    bmi = wheight/((height/100)**2)
    return bmi

wheight = float(input("your weight = "))
height = float(input("how much your thall = "))
print("your BMI is",BMI(wheight,height))
    
