# practising file open tempelate:


def file_open(filename):
    fd = open(filename)
    try:
        for ch in fd:
            print ch
    except IOError, msg:
        print msg
    except KeyboardInterrupt:
        print "Exiting"
    finally:
        try:
            fd.close()
        except NameError:
            pass
            

def main(filename):
    try:
        file_open(filename)
    except IOError, msg:
        print msg



if __name__ == '__main__':
    main("my.txt")
