import random

doubles = ("Can't Happen", "Snake Eyes!", "Little Joe!", "HARD SIX",
           "Hard Eight!", "Rain Forst", "SHUT_it")

def Rollem():
    dice = (random.randrange(1,7), random.randrange(1,7))
    print dice
    if dice[0] == dice[1]:
        print doubles[dice[0]]
    
while True:
    if raw_input("Are you ready") == 'q':
        break
    Rollem()
    

