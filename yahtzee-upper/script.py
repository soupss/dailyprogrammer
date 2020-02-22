from random import randint

def getArr():
    arr = []
    for _ in range(6):
        arr.append(randint(1, 6))
    return arr

def y_u(arr): # yahtzee_upper
    saved = 0
    
    print(arr)
    
    for i in range(1, 7):
        temp = 0
        if i in arr:
            for a in arr:
                if i == a:
                    temp += i
        if temp > saved:
            n = i   # save number that you scored the highest on
            saved = temp
            
    print(f'You scored {saved} on {n}\'s')

y_u(getArr())
