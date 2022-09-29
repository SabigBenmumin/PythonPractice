r = float(input())
while r < 0:
    print("Invalid input.")
    r = float(input())
point = 0
for y in range(1,int(r)+1):
    point += int((r**2-y**2)**0.5)

print(point)
