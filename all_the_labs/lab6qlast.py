# lab 6_4 optional

"""
   This is lab6_6. This program converts a string into
   a pig latin string.
"""
"""
   Formating:
   1.variable_labels
   2.CONSTANT_LABELS
   3.FunctionLabels
   4.Class Name
   5.modules_labels.py
"""

vowels = ('a','e','i','o','u','A','E','I','O','U')

def Index(s):    
     """
     This function calculates the position of a vowel  in
     a word starting from the begining of a word. 
     """
     index_er = 0                                               #int for count starting from zero very important.
     while True:                                                
         if index_er >= len(s):                                 #incase no vowel is found and all string is searched than break
            break
         if s[index_er] in vowels:                              #if a vowel is found break
            break
         else:
            index_er+=1                                         #if consonent found increment indexer
     return index_er                                             

def PigLatin(s):
    """
    This function takes in a string or a sentence and conv
    erts it into a Pig Latin format. 
    """
    global vowels
    string = ''                                                 #creating a string: for holding pigLatin words.
    parts = s.split()                                           # returns a list of strings. I will triverse through each word and check
    for ch in parts:
        if ch[0] in vowels:                                      
            string = string + ch + 'way '                       #As this word starts with vowel add way to end of the first word. Create string
        if ch[0] not in vowels:
            string = string+ch[(Index(ch)):]+ch[0:Index(ch)]    #if first word = consonent than we need to extract alp till vowel is detected. 
            if index(ch) < len(ch):                             #this is for taking care of no vowel words. What if no vowel after consonent?
                string = string +'ay'                           #if their is a vowel it will add ay
            string = string + ' '                               #if it is not a vowel add ay else will add space.If index returns len(ch) than no vowel found 
    print string                                                #either their are no words without a vowel or I am too dumb cuz at the moment cant thing\
                                                                #of a word without vowel! lol

    
    
                
    


PigLatin("eyes as eyes")
