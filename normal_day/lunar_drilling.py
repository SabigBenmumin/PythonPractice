def drill(canvas):
    canvas = canvas.lstrip("´`:")
    canvas = canvas.rstrip(".")
    power = 0
    speed = 0
    surface = []
    cycle = 0
    for item in canvas:
        if item == '-':
            power += 1
        elif item == '=':
            power += 2
        elif item == ">":
            speed += 1
        elif item == ".":
            surface.append(0)
        elif item == "*":
            surface.append(1)
        elif item == "x":
            surface.append(2)
        elif item == "X":
            surface.append(3)
        elif item == "@":
            surface.append(4)
    atk = power * speed
    print(surface)
    while surface != []:
        print("enter surface loop is success /")
        cycle += 1
        if surface[0] == 0:
            surface.pop(0)
        else:
            surface[0] -= atk
            if surface[0] <= 0:
                surface.pop(0)
    return cycle,surface,power,speed,atk

def main():
    canvas = '´`:===>@@@.......'
    result = drill(canvas)
    print(f"cycle is {result[0]}")
    print(f"power is {result[2]}")
    print(f"speed is {result[3]}")
    print(f"atk is {result[4]}")

main()