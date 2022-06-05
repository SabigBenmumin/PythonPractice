
def Grade(score,name):
    if score >= 80:
        grade = "A"
    elif score <80 and score >=70:
        grade = "B"
    elif score <70 and score >=60:
        grade = "C"
    elif score <60 and score >= 50:
        grade = "D"
    else
        grade = "F"
    out = name+" your grade is :"+grade
    return out

name = str(input("your name :"))
score = int(input("your score : "))

print(Grade(score,name))
