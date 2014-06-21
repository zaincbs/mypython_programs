"""
   This is lab7_1. 
"""
"""
   Formating:
   1.variable_labels
   2.CONSTANT_LABELS
   3.FunctionLabels
   4.Class Name
   5.modules_labels.py
"""
base = ("abc","def","ghi","jkl","mno", "pqrs","tuv","wxyz")


def CharToNum(char):
    integer = 0
    while 1:
        for ch in base:
            if char in ch:
                break
            else:
                integer = integer + 1
        break
                
    return str(integer+2)

def StringToNumber(in_put):
     string = ''
     for ch in in_put:
         if ch == ' ':
             pass
         else:
             string = string + CharToNum(ch)
     return string
        
            


        
        
    
    















    
