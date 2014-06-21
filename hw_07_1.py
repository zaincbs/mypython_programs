"""
   This is lab7_2. 
"""
"""
   Formating:
   1.variable_labels
   2.CONSTANT_LABELS
   3.FunctionLabels
   4.Class Name
   5.modules_labels.py
"""

import ass1_d

def main():
    your_string = ""
    while True:
        your_string = raw_input("\n  Type (H)elp or Press Enter to Exit \nWrite your Python Identifier:->")
        if not your_string:
            return
        elif your_string is not 'H':
            print "***  %s  ***" %(ass1_d.IsValidIdentifier(your_string)[1])
        elif your_string == 'H':
            help(ass1_d)
        
        
        
    help(ass1_d)    
    
if __name__ == '__main__':
    main()
""""
$hw_07_1.py

  Type (H)elp or Press Enter to Exit 
Write your Python Identifier:->_x
***  Valid!  ***

  Type (H)elp or Press Enter to Exit 
Write your Python Identifier:->x2
***  Valid!  ***

  Type (H)elp or Press Enter to Exit 
Write your Python Identifier:->lastbutnotleast
***  Valid!  ***

  Type (H)elp or Press Enter to Exit 
Write your Python Identifier:->123
***  Invalid: First symbol must be alphabetic or underscore  ***

  Type (H)elp or Press Enter to Exit 
Write your Python Identifier:->zai,n
***  Invalid:',' is not allowed   ***

  Type (H)elp or Press Enter to Exit 
Write your Python Identifier:->x2_657
***  Valid!  ***

  Type (H)elp or Press Enter to Exit 
Write your Python Identifier:->H
Help on module ass1_d:

NAME
    ass1_d

FILE
    c:\python27\ass1_d.py

DESCRIPTION
    This is Assignment:7.(Draft). This assignment is about
    writing a function that checks if the defined identif-
    ier is invalid or valid

FUNCTIONS
    IsValidIdentifier(pro_string)
        IsValidIdentifier(y) <==> this function receives a
        string that returns a tuple (True or False, reason string).
        Reason String can be as follow:
        -Invalid: First symbol must be alphabetic or underscore
        -Invalid Name: This is a keyword
        -Invalid:'%s' is not allowed. Where %s displays the disallowed character.
        -Valid!
    
    main()

DATA
    ALPHA_NUMERIC = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkl.....
    ALPHA_STRING = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv...c...
    DATA = ('x', '_x', '2x', 'x,y', 'yield', 'is_this_good')



  Type (H)elp or Press Enter to Exit 
Write your Python Identifier:->
"""
