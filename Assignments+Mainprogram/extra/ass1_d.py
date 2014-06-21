#!/usr/bin/ python
# -*- coding: cp1252 -*-
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

import keyword

DATA = ('x', '_x', '2x', 'x,y', 'yield', 'is_this_good')


def IsValidIdentifier(name):
    """
       IsValidIdentifier(y) <==> this function receives a
       string that returns a tuple (True or False, reason string).
       Reason String can be as follow:
       -Invalid: First symbol must be alphabetic or underscore
       -Invalid Name: This is a keyword
       -Invalid:'%s' is not allowed. Where %s displays the disallowed character.
       -Valid!
    """
    if name in keyword.kwlist:
        return (False, "Invalid: this is a keyword!")
    if not name[0].isalpha() and not name[0] == "_":
        return (False, "Invalid: first symbol must be alphabetic or underscore")
    for char in name:
        if not char.isalnum() and not char == "_":
            return (False, "Invalid: ’%s’ is not allowed." % char)
        
    return (True, "Valid!")    
    
    
def main():
    for identifiers in DATA:
        return_value = IsValidIdentifier(identifiers)[1]
        print "%12.12s -> %s" %(identifiers,IsValidIdentifier(identifiers)[1])
    
if __name__ == '__main__':
    main()
"""
$ass1_d.py
x -> Valid!
          _x -> Valid!
          2x -> Invalid: First symbol must be alphabetic or underscore
         x,y -> Invalid:',' is not allowed 
       yield -> Invalid Name: This is a keyword
is_this_good -> Valid!
"""
