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

import lab7_ex1

def main():
    while True:
        your_string = raw_input("Give me some letter and see the magic:")
        print lab7_ex1.StringToNumber(your_string)
    
    
if __name__ == '__main__':
    main()
