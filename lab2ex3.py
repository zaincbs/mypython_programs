#lab2 exerecise 3

number = 5

print "Think of a number betweeb 1 and 10 and I will try to Guess\n"
while 1:
    string = raw_input("Is your number %d?\n" % (number))

    if string == 'y' or string == 'Y':
         break
    elif string == 'n' or string == 'N':
        while 1:
               zain = raw_input("No? Than please press: \n'h' if %d is higher than your number\n'l' if %d is lesser than your number " % (number, number))
               if zain == 'l':
                     number = number - 1
                     last = raw_input("Is your number %d?\n" % (number))
                     if last == y:
                             break
               if zain == 'h':
                     number = number + 1
                     last = raw_input("Is your number %d?\n" % (number))
                     if last == y:
                             break
    elif last == 'y':
        break
        
    
    else:
         print "%s is and invalid input"
         
    
print "Hurray!!!"
