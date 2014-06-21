from __future__ import division
import random


def give_num():
    tu_num = (int(random.randrange(0,13)), int(random.randrange(0,13)))
    my_ans = int(raw_input("What is %d time %d:" % tu_num))
    if my_ans == (tu_num[0] * tu_num[1]):
        print "Right!"
        praise()
        return 1
    else:
        print "Wrong! The right Answer is %d" % (tu_num[0] * tu_num[1])
        return 0

def Quiz(n):
    right = 0
    for ch in range(n):
        value = give_num()
        if value == 1:
            right += 1
        else:           
            right -= 1
        if right < 0:
            right = 0
    return ((right/n)*100)

def Feedback(p):
    if p == 100:
        print "Perfect!"
    if p >= 90 and p< 100:
        print "Excellent"
    if p >= 80 and p< 90:
        print "Very Good"
    if p <80:
        print "You need more practise"

def praise():
    spray = ("Way to go","You are good","Alright!!",
             "Keep doing here comes the hard one"
             ,"OMG Now i will make it hard")
    print spray[random.randrange(0,6)]
        
givevalue = Quiz(3)
print Feedback(givevalue)




