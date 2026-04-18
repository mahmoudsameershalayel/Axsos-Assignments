import random
def randInt(min=0 , max= 100 ):
    if min > max:
        min, max = max, min 
    num = random.random() * (max - min) + min
    return round(num)
print(randInt(min=10, max=-50))        