import math
from check import check
def checkDup(string):
    l = len(string)
    for i in range(1,math.floor(l/2)):
        print(string[-i:])
        print(string[-i*2:-i])
        if string[-i:] == string[-i*2:-i]:
            return True
    return False

def checkDuplicates(string):
    l = len(string)
    for i in range(2, l+1 ,2):
        
        if (string[l-i:l-int(i/2)] == string[l-int(i/2):l]):
            return True
    return False



def ZA(symbols={'A', 'B', 'C'},k=2):
    s = ""
    for j in range(100):
        print(s)
        if not checkDuplicates(s+'A'):
            s += 'A'
        elif not checkDuplicates(s+'B'):
            s += 'B'
        elif not checkDuplicates(s+'C'):
            s += 'C'
        else:

            A=set({s[-1], s[-2]})
            g = [x for x in symbols - A]
            s = s[:-1] + g[0]

#print(recFunc(''))


#print(checkDup('AA'))

def recFunc(string, symbols={'A', 'B', 'C'}, k=2):
    #print(string)
    currSymbol = string[-1]
    for symbol in symbols:
        if symbol  == currSymbol:
            pass
        else:
            if check(string+symbol):
                recFunc(string+symbol)
    if len(string) > 980:
        print(str(len(string)) + string) 



recFunc('A')

