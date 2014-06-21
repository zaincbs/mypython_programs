#lab2-Ex2

while 1:
        answer = raw_input('Enter your number to be converted to H and O\n')
           
        try:
            number = int(answer)
            
        except ValueError:
            print 'Invalid input: %s is not a number you fool' %  (answer)
         
        else:
            break

value = int(number)

print "Value in Deciaml:%5d\n" % (value)
print "Value in Octal  :%#5o"  % (value)
print "Value in Octal  :%#5x"  % (value)
