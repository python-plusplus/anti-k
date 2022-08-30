import math

def check(string):
    n = len(string)
    last = string[-1]
    if n > 4:
        for i in range(-1, -(int(n/2)+2), -1):
            if i == -1:
                pass
            elif i == -2:
                if last != string[-2]:
                    pass
                else:
                    return False
            else:
                if last == string[i]: 
                    if string[i+1:-1] != string[i+(i+2):i]:
                        pass
                    else:
                        #print("repeat found")
                        #print(string)
                        #print(i)
                        #print(n+i)
                        #print(string[i+1:-1])
                        #print(string[i+(i+2):i])
                        return False
        return True
    else:
        return string[-1] != string[-2] and string[2:] != string[:2]

def showDup(string):
    n = len(string)
    last = string[-1]
    if n > 4:
        for i in range(-1, -(int(n/2)+2), -1):
            if i == -1:
                pass
            elif i == -2:
                if last != string[-2]:
                    pass
                else:
                    return False
            else:
                if last == string[i]: 
                    if string[i+1:-1] != string[i+(i+2):i]:
                        pass
                    else:
                        print("repeat found")
                        print(string)
                        print(i)
                        print(n+i)
                        print(string[i+1:-1])
                        print(string[i+(i+2):i])
                        return False
        return True
    else:
        return string[-1] != string[-2] and string[2:] != string[:2]



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
            return Trur
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

    '''
    if len(string) < 100:
        print('deadEnd')
        print(len(string))
        print(string)
        for symbol in symbols:
            if symbol  == currSymbol:
                pass
            else:
                showDup(string+symbol)
    '''
    if len(string) > 980:
        print(str(len(string)) + string) 
        showDup(string+'A')
        showDup(string+'B')
        showDup(string+'C')



recFunc('A')

