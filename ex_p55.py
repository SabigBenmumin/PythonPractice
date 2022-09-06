quantity = int(input("enter the number of packages purchased:"))
before_discount = quantity * 99
if quantity >= 10 and quantity <= 19:
    discount = 10
elif quantity >= 20 and quantity <= 49:
    discount = 20
elif quantity >= 50 and quantity <= 99:
    discount = 30
else:
    discount = 40
after_discount = before_discount * discount / 100
print("your discount is:",discount,"%")
print("purchased after the discount is:",after_discount)

