#testing dictionary:

py_dict = {}

def StarMenu(choices):
    choice_list = sorted(choices)
    return "Choose" + ",".join(['(%s)%s' % (m[0],m[1:]) for m in choice_list]) + "(enter to quit):"
  
def CollectEntries():
    while True:
        word = raw_input("Word/Key:")
        if not word:
            return
        meaning = raw_input("Meaning:")
        if not meaning:
            return
        else:
            py_dict[word] = meaning
 
def FindDefinations():
    while True:
        fin_d = raw_input("Word to find")
        if not fin_d:
            return
        try:
            print '%s: %s' %(fin_d, py_dict[fin_d])
        except KeyError:
            print '%s not in the dicton' % fin_d

def keyfunc(x):
    return py_dict[x]

def Definations():
    mylist = sorted(py_dict,key=keyfunc)
    for ch in mylist:
        print "%s:%s" % (ch,py_dict[ch])
def Definations2():
    string = [(v,k) for (k,v) in py_dict.items()]
    string.sort()
    for (v,k) in string:
        print v, ":" , k
    

def PrintEntries():
    for ch in py_dict:
        print "%s : %s" % (ch, py_dict[ch])

def main():
    choices = {'add': CollectEntries, 'find': FindDefinations, 'print': PrintEntries,'definations':Definations,'Definations':Definations2}
    prompt = StarMenu(choices)
    
    while True:
        user_choice = raw_input(prompt)
        for be_choice in choices:
            if be_choice[0] == user_choice:
                choices[be_choice]()
        

    






if __name__ == '__main__':
    main()
