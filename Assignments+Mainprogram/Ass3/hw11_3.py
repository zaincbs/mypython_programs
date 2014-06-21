#!/usr/bin/env python
"""
This is assignmnet number 3 part 4. This checks for Palindromize sentences
the files in the directory structure
"""
import string
import os
import sys
sys.path.insert(0, '..')
import utils.hw11_2 as hw11_2




def file_open(file_name, fail_on_read = False):
    """
	opens a file and reads the data inside and check the words for pali
    """

    open_obj = open(file_name, "r")
    
    try:
        for lines in open_obj:
            lines = lines.strip("\n")
            if hw11_2.Palindromize(lines):
                print hw11_2.Palindromize(lines)
                if fail_on_read:
                    raise IOError, "Failed while Reading"
            
    except IOError, msg:
        print msg
    except KeyboardInterrupt, msg:
        print "Key Board Interrupt"
    finally:
        try:
            file_obj.close()
        except NameError:
            pass

    
def Func(anything, dirname , fnames):
    """
	triverses through the directory structure
    """
    for file_name in fnames:
        whole_name = os.path.join(dirname, file_name)
        if not os.path.isdir(whole_name):
            file_open(whole_name)
                   

def main():
    """
        This is the main program does testing also. 
    """
    userin = raw_input("(Enter for Default)Tell your directory name:")
    if userin:
        #this is when the user inputs the whole path
        if os.path.isdir(userin) and os.path.dirname(userin) != "":
            os.chdir(os.path.dirname(userin))
            os.path.walk(os.path.basename(userin), Func, 'Walking:')
        #this is when the user gives the name of the directory in the working
        #directory
        elif os.path.isdir(os.getcwd()+"\\"+userin):
            os.chdir(os.path.dirname(os.getcwd()+"\\"+userin))
            os.path.walk(os.path.basename(os.getcwd()+"\\"+userin), Func, 'Walking:')
        else:
            print "%s is not a directory. Invalid path" % userin
    else:
        os.path.walk("testing", Func, 'Walking:')


if __name__ == '__main__':
    main()


"""
(Enter for Default)Tell your directory name:C:\Users\zain\Desktop\Assignment3\Application\driver\testing
nevereven
murderforajarofredrum
12321
abcba
>>> ================================ RESTART ================================
>>> 
(Enter for Default)Tell your directory name:testing
nevereven
murderforajarofredrum
12321
abcba
>>> ================================ RESTART ================================
>>> 
(Enter for Default)Tell your directory name:
>>> ================================ RESTART ================================
>>> 
(Enter for Default)Tell your directory name:
nevereven
murderforajarofredrum
12321
abcba
"""
