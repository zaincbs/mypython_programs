#file io

def PrintFile(f_name):
    open_file = open(f_name)
    try:
        for line in open_file:
            print line,
    finally:
        open_file.close()

def main(f_name):
    try:
        PrintFile(f_name)
    except IOError, msg:
        print msg
        

if __name__== '__main__':
    import sys
    try:
        main(sys.argv[1])
    except IndexError:
        main()
