import time
import os
import do_swap

def Func(anything, dirname, fnames):
    
    for file_name in fnames:
        whole_name = os.path.join(dirname, file_name)
        if os.path.isdir(whole_name):
            print '    directory:', file_name
        else:
            do_swap.file_open(whole_name)
            




if __name__ == '__main__':
    os.path.walk('cats', Func, 'Walking:')
    
