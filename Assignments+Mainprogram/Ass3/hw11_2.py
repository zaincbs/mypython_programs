#!/usr/bin/env python

import string
import time  
import os 

Data = ("Murder for a jar of red rum", 232,"nope", "abcbA", 3443, "what","Never odd or even", "Rats live on no evil star")
mystring = string.punctuation + " "

def Palindromize2(text):
    """
     returns the lowercase version of the phrase with whitespace and punctuation removed if the phrase is a palindrome
    """
    text=str(text)
    if len(text)<=3:
        return
    final = "".join([x for x in text if x not in mystring]).lower()
    if final == final[::-1]:
        return final
    else:
        return


def Palindromize(text):
    """
     returns the lowercase version of the phrase with whitespace and punctuation removed if the phrase is a palindrome
    """
    text = str(text)
    if len(text)<=3:
        return
    final=""
    for word in text:
        word = word.strip(mystring).lower()
        final += word
    if final == final[::-1]:
        return final
    else:
        return
    
def main():
    """
    Main Function Uses both functions.
    """
    print "\n********using  list comprehensions************\n"
    for specs in Data:
        if Palindromize2(specs):
            print Palindromize2(specs)
    print "\n*******Not using  list comprehensions*********\n"
    for specs in Data:
        if Palindromize(specs):
            print Palindromize(specs)
    

if __name__ == '__main__':
    main()



"""
********using  list comprehensions************

murderforajarofredrum
12321
abcba
3443
neveroddoreven
ratsliveonnoevilstar

*******Not using  list comprehensions*********

murderforajarofredrum
12321
abcba
3443
neveroddoreven
ratsliveonnoevilstar
"""

