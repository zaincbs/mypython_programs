# IO files template


def file_open(file_name, fail_on_read = False):
    open_obj = open(file_name)
    try:
        for ch in open_obj:
            print ch,
            if fail_on_read:
                raise IOError, "Failed while Reading"
    except IOError, msg:
        print msg
    except KeyboardInterrupt, msg:
        print "CLT+C Pressed You stupid"
    finally:
        try:
            file_obj.close()
        except NameError:
            pass

def main(file_name="NEWS.txt"):
    file_open(file_name)
  
if __name__ == '__main__':
    main()
