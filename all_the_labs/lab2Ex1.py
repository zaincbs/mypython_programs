# lab2 Ex1 
from __future__ import division

while 1:
        answer = raw_input('What is your first Number\n')
           
        try:
            number = int(answer)
            
        except ValueError:
            print 'Invalid input: %s is not a number you fool' %  (answer)
         
        else:
            break

while 1:
        answer2 = raw_input('What is your second Number\n')


    
        try:
            number2 = int(answer2)
        except ValueError:
            print 'Invalid input: %s is not a number you fool' %  (answer2) 
         
        else:
            break

mod = number2 % number

if mod > 0:
    print "%d is not a Multiple of %d" % (number2,number)
else:
    print "%d is a Multiple of %d" % (number2,number)



