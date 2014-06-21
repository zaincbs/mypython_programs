import string

DATA_NAME = [str(x) for x in range(10) if x > 1] + ["Jack" , "Queen" , "King"]
DATA_SELF = ["Hearts","Diamonds","Tree","Spades"]
DATA_NUMBERS = [ a+' of '+ z for a in DATA_SELF for z in DATA_NAME]
print DATA_NAME
print DATA_NUMBERS
