def normal():
    fruit = {"mango", "orange", "mayom"}
    enimal = {"Anaconda", "Birt", "Zebraa", "Monkey",43,True}

def constructor():
    fish = set(["Shark", "Nemo", "Nill"]) # set(List)

# valiableName = {elements} equal to valiableName = set([element])

def addElement():
    fish = set(["Shark", "Nemo", "Nill"]) # set(List)
    print(fish)    
    fish.add("Kraben")
    print(fish)

def addElements():
    fish = set(["Shark", "Nemo", "Nill"]) # set(List)
    lis = ["Pla1", "Pla2", "Pla3"] #element in list for add to set(fist)
    fish.update(lis)
    print(fish)

def addElements_2(): #add more elements,but with out list for add to set line
    fish = set(["Shark", "Nemo", "Nill"]) # set(List)
    fish.update(["Pla1", "Pla2", "Pla3"])
    print(fish)
    
def forAndSet():
    fish = {'Pla2', 'Nemo', 'Nill', 'Pla3', 'Pla1', 'Shark'}
    for item in fish:
        print(item)

def countElement():
    fish = {'Pla2', 'Nemo', 'Nill', 'Pla3', 'Pla1', 'Shark'}
    print(len(fish))

def checkElementInSet():
    fish = {'Pla2', 'Nemo', 'Nill', 'Pla3', 'Pla1', 'Shark'}
    print("Pla1" in fish)
    print("Tiger" in fish)

def removeElementInSet():
    fish = {'Pla2', 'Nemo', 'Nill', 'Pla3', 'Pla1', 'Shark'}
    print(f"before remove {fish}")
    fish.remove("Nemo")
    print(f"after remove {fish}")

def removeElementInSet_2():
    fish = {'Pla2', 'Nemo', 'Nill', 'Pla3', 'Pla1', 'Shark'}
    element = input("Enter element name for remove: ")
    if element in fish:
        fish.remove(element)
        print("remove success")
        print(f"updated your set: {fish}")
    else:
        print(f"{element} did't in fish set")

fish = {'Pla2', 'Nemo', 'Nill', 'Pla3', 'Pla1', 'Shark'}

def removeElementInSet_3(fish):
    element = input("Enter element name for remove: ")
    try:
        fish.remove(element)
        print("remove success")
        print(f"updated your set: {fish}")
    except KeyError:
        print(f"{element} did't in fish set")

def removeElementInSet_4(fish): 
    element = input("Enter element name for remove: ")
    fish.discard(element)
    print(f"updated your set: {fish}")

"""
we can remove element in set by 2 methonds
1) remove 
    use case setvar.remove(x) this method we can remove x element if x in setvar 
    but if x not in setvar program is print KeyError
2) discard
    use case setvar.discard(x) this method we can remove x element if x in setvar
    but if x not in setvar program is not error and this line is not effect for your program
"""
    
removeElementInSet_4(fish)