#quiz1 lab 4

def find_my_grade(int_input):
    if int_input >= 90:
        return 'A'
    if int_input < 90 and int_input >= 80:
        return 'B'
    if int_input < 80 and int_input >= 70:
        return 'C'
    if int_input < 70 and int_input >= 60:
        return 'D'
    if int_input < 60:
        return 'F'
    


myinput = (raw_input("Whats your Name:"), int(raw_input("Whats your Score:"))) 

mygradeis = find_my_grade(myinput[1])

print "%s your grade is %s" % (myinput[0], mygradeis)
