import random

def question():
    n = random.randint(2,5)
    list_q = []
    q = ''
    for i in range(n):
        num_int = random.randint(1,10)
        list_q.append(num_int)
        q += f" + {num_int}"
    prob = q.lstrip(" + ")
    ans = int(input(f"{prob} = "))
    if ans != sum(list_q):
        print(f"Wrong! The answer was {sum(list_q)}")
        return False
    else:
        return True
 
def play():
    HP = 3
    score = 0
    while HP > 0:
        if question():
            score += 1
        else:
             HP -= 1
    print(f"You earned {score}")
play()