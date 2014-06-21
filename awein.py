#!/usr/bin/ python
#Assignment 1 draft


#def IsValidIdentifier()

def AreStringsIdentifiers(*strings):
   try:
      class test(object): __slots__ = strings
   except TypeError:
      return False
   else:
      return True

print AreStringsIdentifiers('A', 'B') # -> True
print AreStringsIdentifiers('A', '_AB', 'xy') # -> False

