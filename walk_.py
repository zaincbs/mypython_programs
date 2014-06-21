#!/usr/bin/env python
"""walk_.py -- Demonstrates the os.path.walk function, one of many
very useful things given to us in the os module"""

import time  
import os 
        
def Func(anything, dirname, fnames):
    print anything, os.path.abspath(dirname)
    for file_name in fnames:
        whole_name = os.path.join(dirname, file_name)
        if os.path.isdir(whole_name):
            print '    directory:', file_name
        else:
            print '    %s:\n        %s' % (file_name, time.ctime( 
                os.path.getmtime(whole_name)))
            
if __name__ == '__main__':
    os.path.walk('cats', Func, 'Walking:')

"""$ walk_.py
Walking: /home/marilyn/python/mm/labs/lab_10_File_IO/cats
    cats.txt:
        Thu Jun 18 16:21:33 2009
    more_cats.txt:
        Thu Jun 18 16:21:33 2009
    directory: deep_cats
Walking: /home/marilyn/python/mm/labs/lab_10_File_IO/cats/deep_cats
    cats.txt:
        Thu Jun 18 16:21:33 2009
    more_cats.txt:
        Thu Jun 18 16:21:33 2009
    directory: deeper_cats
Walking: /home/marilyn/python/mm/labs/lab_10_File_IO/cats/deep_cats/deeper_cats
    cats.txt:
        Thu Jun 18 16:21:33 2009
    more_cats.txt:
        Thu Jun 18 16:21:33 2009
$
"""
