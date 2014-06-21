n = 0
bin_val = 0

while 1:
    answer = raw_input("Please give your Binary String\n")
    try:
        number = int(answer)
    except ValueError:
        print'%s is not numeric data' % (answer)
        
    else:
          break
answer = answer[::-1]
b_value = 1
i = range(0, len(answer))
for val in i:
    a = answer[n]
    print a
    bin_val += (b_value*int(a))
    n = n+1
    b_value *= 2
print 'your decimal value is:%d' % (bin_val)
print 'your Hex value is:%#x' % (bin_val)    
print 'your Octat value is:%#o' % (bin_val)
