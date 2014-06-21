#!/usr/bin/ python
#Assignment 1 draft
"""
   This is Assignment:7.(Draft). This assignment is about
   writing a function that checks if the defined identif-
   ier is invalid or valid
"""
"""
   Formating:
   1.variable_labels
   2.CONSTANT_LABELS
   3.FunctionLabels
   4.Class Name
   5.modules_labels.py
"""
import string
import keyword

DATA = ('x', '_x', '2x', 'x,y', 'yield', 'is_this_good')
ALPHA_STRING = string.letters+'_'
ALPHA_NUMERIC = string.digits + string.letters+'_' 

def IsValidIdentifier(pro_string):
    """
       IsValidIdentifier(y) <==> this function receives a
       string that returns a tuple (True or False, reason string).
       Reason String can be as follow:
       -Invalid: First symbol must be alphabetic or underscore
       -Invalid Name: This is a keyword
       -Invalid:'%s' is not allowed. Where %s displays the disallowed character.
       -Valid!
    """
    if pro_string[0] not in ALPHA_STRING:
        return (False, "Invalid: First symbol must be alphabetic or underscore")
    elif keyword.iskeyword(pro_string):
        return (False, "Invalid Name: This is a keyword")
    for rem_words in pro_string[1:]:
        if rem_words not in ALPHA_NUMERIC:
            return (False, '''Invalid:'%s' is not allowed '''%rem_words)
    else:
        return (True, "Valid!")

def main():
    for identifiers in DATA:
        return_value = IsValidIdentifier(identifiers)[1]
        print "%12.12s -> %s" %(identifiers,IsValidIdentifier(identifiers)[1])
    
if __name__ == '__main__':
    main()
