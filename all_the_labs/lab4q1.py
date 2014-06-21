import random
# 1 for head and 0 for tail

def Coin():                                     #
     if random.randrange(0,2) == 1:             # 
         return "head"                          #
     else:
         return "tails"

def Experiment():
    head = count = 0
    while head <3:
        count +=1
        if Coin() == "head":
            head += 1
        else:
            head = 0
    return count

#################################################

total = 0
for ch in range(10):
    flips = Experiment()
    total += flips
    
print " It took |%-10.1f| coin flipes to get 3 in a row" % (total / 10)
