"""
   This is Assignment:7.(Draft). In this module we are importing
   module ass1_d which has a function validIdentifier. We are
   promting the user to give a string for testing that the
   identifier is good or bad?
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
    """
    prompts the user for a string for testing identifier. Entering a space
    will lead us to help command on ass1_d which shows all the stuff related
    to the previous module
    """
    your_string = ""
    while your_string != ' ':
        your_string = raw_input("\n  (Space+Return for Help)\nWrite your Python Identifier:->")
        if your_string == '':
            continue
        print "***  %s  ***" %(ass1_d.IsValidIdentifier(your_string)[1])
    help(ass1_d)
    
    
if __name__ == '__main__':
    main()
