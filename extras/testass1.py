#!/usr/bin/env python
"""hw07_1.py identifier
tells you if identifier is a valid Python identifier."""

import keyword



def IsValidIdentifier(name):



if __name__ == "__main__":
    DATA = ("x", "_x", "2x", "x,y", "yield", "is_this_good")
    for word in DATA:
        answer_tuple = IsValidIdentifier(word)
        print "%20s -> %s" % (word, answer_tuple[1])
"""
       IsValidIdentifier(y) <==> this function receives a
       string that returns a tuple (True or False, reason string).
       Reason String can be as follow:
       -Invalid: First symbol must be alphabetic or underscore
       -Invalid Name: This is a keyword
       -Invalid:'%s' is not allowed. Where %s displays the disallowed character.
       -Valid!
    """
