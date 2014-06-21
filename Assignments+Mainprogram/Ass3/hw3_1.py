#assignment 3
"""
This is first part of the assignment 3 in this we print the ascii
letters acccording to the range provided or without a range. 
"""

def GiveAsciiChart():
    """(Fucntion Readiable: YES)Function returns a string when printed prints an Ascii table between 32-126"""
    string=" "
    for the_val in range(32,127):
        if not the_val%4:
            string= string + "\n"
        string = string + "%-3d: %-4s" % (the_val,chr(the_val))
    else:
        return string
    
def GiveAsciiChart2(st=32,ed=127):
    """(Fucntion Readiable: YES) Function returns a string when printed prints an Ascii table between 32-126 needs an input for specific range"""
    string=" "
    for the_val in range(st,ed):
        if not the_val%4:
            string= string + "\n"
        string = string + "%-3d: %-4s" % (the_val,chr(the_val))
    else:
        return string
        
def GiveAsciiChart3():
    """(Fucntion Readiable: NO) Function returns a string when printed prints an Ascii table between 32-126"""
    return "\n".join(["".join(["%-3d: %-4s" % (x,chr(x)) for x in range(32+n,36+n)]) for n in range(0,92,4)])+ "\n" + "".join(["%-3d: %-4s" % (z,chr(z)) for z in range(124,127)])

def GiveAsciiChart4(st, ed):
    """(Fucntion Readiable: NO) Function returns a string when printed prints an Ascii table between 32-126 needs an input for specific range"""
    return "\n".join([''.join(["%-3d: %-4s" %(st+n,chr(st+n)) for n in range(0+m,4+m)]) for m in range(0,((ed-st)/4)*4,4)])+"\n"+"".join(["%-3d: %-4s" % (z,chr(z)) for z in range(ed-((ed-st)%4),ed)])

def main():
    print "********Solution with no range and readible code************"
    print GiveAsciiChart()
    print "********Solution no range and readible code************"
    print GiveAsciiChart2(32,127)
    print "********Solution with no range and not a readible code************"
    print GiveAsciiChart3()
    print "********Solution with range and readible code************"
    print GiveAsciiChart4(32,127)

if __name__ == '__main__':
    main()



"""
********Solution with no range and readible code************
 
32 :     33 : !   34 : "   35 : #   
36 : $   37 : %   38 : &   39 : '   
40 : (   41 : )   42 : *   43 : +   
44 : ,   45 : -   46 : .   47 : /   
48 : 0   49 : 1   50 : 2   51 : 3   
52 : 4   53 : 5   54 : 6   55 : 7   
56 : 8   57 : 9   58 : :   59 : ;   
60 : <   61 : =   62 : >   63 : ?   
64 : @   65 : A   66 : B   67 : C   
68 : D   69 : E   70 : F   71 : G   
72 : H   73 : I   74 : J   75 : K   
76 : L   77 : M   78 : N   79 : O   
80 : P   81 : Q   82 : R   83 : S   
84 : T   85 : U   86 : V   87 : W   
88 : X   89 : Y   90 : Z   91 : [   
92 : \   93 : ]   94 : ^   95 : _   
96 : `   97 : a   98 : b   99 : c   
100: d   101: e   102: f   103: g   
104: h   105: i   106: j   107: k   
108: l   109: m   110: n   111: o   
112: p   113: q   114: r   115: s   
116: t   117: u   118: v   119: w   
120: x   121: y   122: z   123: {   
124: |   125: }   126: ~   
********Solution no range and readible code************
 
32 :     33 : !   34 : "   35 : #   
36 : $   37 : %   38 : &   39 : '   
40 : (   41 : )   42 : *   43 : +   
44 : ,   45 : -   46 : .   47 : /   
48 : 0   49 : 1   50 : 2   51 : 3   
52 : 4   53 : 5   54 : 6   55 : 7   
56 : 8   57 : 9   58 : :   59 : ;   
60 : <   61 : =   62 : >   63 : ?   
64 : @   65 : A   66 : B   67 : C   
68 : D   69 : E   70 : F   71 : G   
72 : H   73 : I   74 : J   75 : K   
76 : L   77 : M   78 : N   79 : O   
80 : P   81 : Q   82 : R   83 : S   
84 : T   85 : U   86 : V   87 : W   
88 : X   89 : Y   90 : Z   91 : [   
92 : \   93 : ]   94 : ^   95 : _   
96 : `   97 : a   98 : b   99 : c   
100: d   101: e   102: f   103: g   
104: h   105: i   106: j   107: k   
108: l   109: m   110: n   111: o   
112: p   113: q   114: r   115: s   
116: t   117: u   118: v   119: w   
120: x   121: y   122: z   123: {   
124: |   125: }   126: ~   
********Solution with no range and not a readible code************
32 :     33 : !   34 : "   35 : #   
36 : $   37 : %   38 : &   39 : '   
40 : (   41 : )   42 : *   43 : +   
44 : ,   45 : -   46 : .   47 : /   
48 : 0   49 : 1   50 : 2   51 : 3   
52 : 4   53 : 5   54 : 6   55 : 7   
56 : 8   57 : 9   58 : :   59 : ;   
60 : <   61 : =   62 : >   63 : ?   
64 : @   65 : A   66 : B   67 : C   
68 : D   69 : E   70 : F   71 : G   
72 : H   73 : I   74 : J   75 : K   
76 : L   77 : M   78 : N   79 : O   
80 : P   81 : Q   82 : R   83 : S   
84 : T   85 : U   86 : V   87 : W   
88 : X   89 : Y   90 : Z   91 : [   
92 : \   93 : ]   94 : ^   95 : _   
96 : `   97 : a   98 : b   99 : c   
100: d   101: e   102: f   103: g   
104: h   105: i   106: j   107: k   
108: l   109: m   110: n   111: o   
112: p   113: q   114: r   115: s   
116: t   117: u   118: v   119: w   
120: x   121: y   122: z   123: {   
124: |   125: }   126: ~   
********Solution with range and readible code************
32 :     33 : !   34 : "   35 : #   
36 : $   37 : %   38 : &   39 : '   
40 : (   41 : )   42 : *   43 : +   
44 : ,   45 : -   46 : .   47 : /   
48 : 0   49 : 1   50 : 2   51 : 3   
52 : 4   53 : 5   54 : 6   55 : 7   
56 : 8   57 : 9   58 : :   59 : ;   
60 : <   61 : =   62 : >   63 : ?   
64 : @   65 : A   66 : B   67 : C   
68 : D   69 : E   70 : F   71 : G   
72 : H   73 : I   74 : J   75 : K   
76 : L   77 : M   78 : N   79 : O   
80 : P   81 : Q   82 : R   83 : S   
84 : T   85 : U   86 : V   87 : W   
88 : X   89 : Y   90 : Z   91 : [   
92 : \   93 : ]   94 : ^   95 : _   
96 : `   97 : a   98 : b   99 : c   
100: d   101: e   102: f   103: g   
104: h   105: i   106: j   107: k   
108: l   109: m   110: n   111: o   
112: p   113: q   114: r   115: s   
116: t   117: u   118: v   119: w   
120: x   121: y   122: z   123: {   
124: |   125: }   126: ~
"""


